import datetime

from app import models
from app import app
from app import db

from flask import jsonify
from flask import request

@app.route('/api/timetable', methods=['GET'])
def get_timetable():
    timetables = models.Timetable.query.all()
    dict_list = [item.get_json() for item in timetables]
    return jsonify(dict_list)

@app.route('/api/timetable/<int:record_id>', methods=['GET'])
def get_record_by_id(record_id):
    record = models.Timetable.query.get(record_id)
    if record == None:
        return jsonify({"Error" : "404"})
    return jsonify(record.get_json())

@app.route('/api/timetable', methods=['POST'])
def create_record():
    if not request.json or not 'doctor_id' in request.json or not 'polyclinic_id' in request.json:
        return jsonify({'Error': 400, "Message" : "Fields doctor_id and polyclinic_id are mandatory!"}), 400
    try:
        doctor = models.Doctor.query.get(int(request.json['doctor_id']))
    except ValueError:
        doctor = models.Doctor.query.first()
    if doctor == None:
        doctor = models.Doctor.query.first()

    try:
        poly = models.Polyclinic.query.get(int(request.json['polyclinic_id']))
    except ValueError:
        poly = models.Polyclinic.query.first()
    if doctor == None:
        poly = models.Polyclinic.query.first()

    try:
        patient = models.User.query.get(int(request.json.get('patient_id', "Not")))
    except ValueError:
        patient = None

    if not 'time' in request.json:
        time = None
    else:
        try:
            time = datetime.datetime.strptime(request.json.get('time', "25-10-1900 15:55"), '%d-%m-%Y %H:%M')
        except ValueError:
            time = None


    try:
        record = models.Timetable(doctor=doctor,
                                  polyclinic=poly,
                                  patient=patient,
                                  time=time,
                                  room_number=request.json.get("room_number", "Default"),
                                  departure=bool(request.json.get("departure", "False"))
                               )
        db.session.add(record)
        db.session.commit()
    except:
        record = None

    if record == None:
        return jsonify({'Error': 500, 'Message': 'Record is None'}), 500

    return jsonify(record.get_json()), 201

@app.route('/api/timetable/<int:id>', methods = ['DELETE'])
def delete_record(id):
    record = models.Timetable.query.get(id)
    if record == None:
        return jsonify({"Error": "404", "Message": "Record with this id in timetable is not existing."})
    json = jsonify(record.get_json())
    db.session.delete(models.Timetable.query.get(id))
    db.session.commit()
    return json

@app.route('/api/timetable/<int:record_id>', methods=['PUT'])
def update_record(record_id):
    if not request.json or not 'doctor_id' in request.json or not 'polyclinic_id' in request.json:
        return jsonify({'Error': 400, "Message" : "Fields doctor_id and polyclinic_id are mandatory!"}), 400
    record = models.Timetable.query.get(record_id)
    if record == None:
        return jsonify({"Error": "404", "Message": "Record with this id in timetable is not existing."})
    cache_json = record.get_json()
    try:
        doctor = models.Doctor.query.get(int(request.json['doctor_id']))
    except ValueError:
        doctor = models.Doctor.query.first()
    if doctor == None:
        doctor = models.Doctor.query.first()

    try:
        poly = models.Polyclinic.query.get(int(request.json['polyclinic_id']))
    except ValueError:
        poly = models.Polyclinic.query.first()
    if doctor == None:
        poly = models.Polyclinic.query.first()

    try:
        patient = models.User.query.get(int(request.json.get('patient_id', "Not")))
    except ValueError:
        patient = None

    if not 'time' in request.json:
        time = None
    else:
        try:
            time = datetime.datetime.strptime(request.json.get('time', "25-10-1900 15:55"), '%d-%m-%Y %H:%M')
        except ValueError:
            time = None


    try:
        record.doctor=doctor
        record.polyclinic=poly
        record.patient=patient
        record.time=time
        record.room_number=request.json.get("room_number", "Default")
        record.departure=bool(request.json.get("departure", "False"))
        db.session.add(record)
        db.session.commit()
    except:
        record = None

    if record == None:
        return jsonify({'Error': 500, 'Message': 'Record is None'}), 500

    result_json = {}
    result_json["before"] = cache_json
    result_json["after"] = record.get_json()

    return jsonify(result_json), 201

