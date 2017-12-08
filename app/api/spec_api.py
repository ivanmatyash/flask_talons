from app import models
from app import app
from flask import jsonify

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

