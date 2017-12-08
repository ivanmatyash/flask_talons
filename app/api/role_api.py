from app import models
from app import app
from flask import jsonify

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