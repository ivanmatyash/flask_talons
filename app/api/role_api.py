from app import models
from app import app
from app import db
from flask import jsonify
from flask import request
from flask.ext.login import login_required

@app.route('/api/roles', methods=['GET'])
def get_roles():
    roles = models.Role.query.all()
    dict_list = [item.get_json() for item in roles]
    return jsonify(dict_list)

@app.route('/api/roles/<int:role_id>', methods=['GET'])
def get_role_by_id(role_id):
    role = models.Role.query.get(role_id)
    if role == None:
        return jsonify({"Error" : "404"})
    return jsonify(role.get_json())

@app.route('/api/roles', methods=['POST'])
@login_required
def create_role():
    if not request.json:
        return jsonify({'Error': 400, "Message" : "Request must to have JSON."}), 400

    try:
        role = models.Role(role_name=request.json['role_name'])
        db.session.add(role)
        db.session.commit()
    except:
        role = None

    if role == None:
        return jsonify({'Error': 500, 'Message': 'Role is None'}), 500

    return jsonify(role.get_json()), 201

@app.route('/api/roles/<int:id>', methods = ['DELETE'])
@login_required
def delete_role(id):
    role = models.Role.query.get(id)
    if role == None:
        return jsonify({"Error": "404", "Message": "Role with this id is not existing."})
    json = jsonify(role.get_json())
    db.session.delete(models.Role.query.get(id))
    db.session.commit()
    return json