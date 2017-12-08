from app import models
from app import app
from flask import jsonify

@app.route('/api/doctors', methods=['GET'])
def get_doctors():
    doctors = models.Doctor.query.all()
    dict_list = [item.get_json() for item in doctors]
    return jsonify(dict_list)

@app.route('/api/doctors/<int:doctor_id>', methods=['GET'])
def get_doctor_by_id(doctor_id):
    doctor = models.Doctor.query.get(doctor_id)
    if doctor == None:
        return jsonify({"Error" : "404"})
    return jsonify(doctor.get_json())