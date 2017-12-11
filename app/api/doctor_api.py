from app import models
from app import app
from app import db

from flask import jsonify
from flask import request

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

@app.route('/api/doctors', methods=['POST'])
def create_doctor():
    if not request.json or not 'speciality_id' in request.json:
        return jsonify({'Error': 400, "Message" : "Field speciality_id is mandatory!"}), 400
    try:
        speciality = models.Speciality.query.get(int(request.json['speciality_id']))
    except ValueError:
        speciality = models.Speciality.query.first()
    if speciality == None:
        speciality = models.Speciality.query.first()
    try:
        doctor = models.Doctor(name=request.json.get('name', "Anon Doctor"),
                               speciality = speciality,
                               photo_url = request.json.get("photo_url", "https://www.combankmed.com/wp-content/uploads/2015/06/Male-Doctor-Avatar.png")
                               )
        db.session.add(doctor)
        db.session.commit()
    except:
        doctor = None

    if doctor == None:
        return jsonify({'Error': 500, 'Message': 'Doctor is None'}), 500

    return jsonify(doctor.get_json()), 201

@app.route('/api/doctors/<int:id>', methods = ['DELETE'])
def delete_doctor(id):
    doctor = models.Doctor.query.get(id)
    if doctor == None:
        return jsonify({"Error": "404", "Message": "Doctor with this id is not existing."})
    json = jsonify(doctor.get_json())
    db.session.delete(models.Doctor.query.get(id))
    db.session.commit()
    return json