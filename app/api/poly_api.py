from app import models
from app import app
from flask import jsonify

@app.route('/api/polyclinics', methods=['GET'])
def get_polys():
    polyclinics = models.Polyclinic.query.all()
    dict_list = [item.get_json() for item in polyclinics]
    return jsonify(dict_list)