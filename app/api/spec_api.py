from app import models
from app import app
from app import db

from flask import jsonify
from flask import request
from flask.ext.login import login_required

@app.route('/api/specialities', methods=['GET'])
def get_spec():
    specs = models.Speciality.query.all()
    dict_list = [item.get_json() for item in specs]
    return jsonify(dict_list)

@app.route('/api/specialities/<int:spec_id>', methods=['GET'])
def get_spec_by_id(spec_id):
    spec = models.Speciality.query.get(spec_id)
    if spec == None:
        return jsonify({"Error" : "404"})
    return jsonify(spec.get_json())

@app.route('/api/specialities', methods=['POST'])
@login_required
def create_spec():
    if not request.json:
        return jsonify({'Error': 400, "Message" : "Request must to have JSON."}), 400

    try:
        spec = models.Speciality(speciality_name=request.json['speciality_name'])
        db.session.add(spec)
        db.session.commit()
    except:
        spec = None

    if spec == None:
        return jsonify({'Error': 500, 'Message': 'Speciality is None'}), 500

    return jsonify(spec.get_json()), 201

@app.route('/api/specialities/<int:id>', methods = ['DELETE'])
@login_required
def delete_spec(id):
    spec = models.Speciality.query.get(id)
    if spec == None:
        return jsonify({"Error": "404", "Message": "Speciality with this id is not existing."})
    json = jsonify(spec.get_json())
    db.session.delete(models.Speciality.query.get(id))
    db.session.commit()
    return json