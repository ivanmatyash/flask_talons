from app import models
from app import app
from app import db
from flask import jsonify
from flask import request
from flask.ext.login import login_required

@app.route('/api/polyclinics', methods=['GET'])
def get_polys():
    polyclinics = models.Polyclinic.query.all()
    dict_list = [item.get_json() for item in polyclinics]
    return jsonify(dict_list)

@app.route('/api/polyclinics/<int:poly_id>', methods=['GET'])
def get_poly_by_id(poly_id):
    poly = models.Polyclinic.query.get(poly_id)
    if poly == None:
        return jsonify({"Error" : "404"})
    return jsonify(poly.get_json())

@app.route('/api/polyclinics', methods=['POST'])
@login_required
def create_poly():
    if not request.json:
        return jsonify({'Error': 400, "Message" : "Request must to have JSON."}), 400

    try:
        poly = models.Polyclinic(polyclinic_number=int(request.json.get("polyclinic_number", -1)),
                                 address=request.json.get("address", "Novinki"))
        db.session.add(poly)
        db.session.commit()
    except:
        poly = None

    if poly == None:
        return jsonify({'Error': 500, 'Message': 'Polyclinic is None'}), 500

    return jsonify(poly.get_json()), 201

@app.route('/api/polyclinics/<int:id>', methods = ['DELETE'])
@login_required
def delete_poly(id):
    poly = models.Polyclinic.query.get(id)
    if poly == None:
        return jsonify({"Error": "404", "Message": "Polyclinic with this id is not existing."})
    json = jsonify(poly.get_json())
    db.session.delete(models.Polyclinic.query.get(id))
    db.session.commit()
    return json