from app import models
from app import app
from app import db

from flask import jsonify
from flask import request
from flask.ext.login import login_required

@app.route('/api/week_timetable', methods=['GET'])
def get_timetable_week():
    records = models.WeekTimetable.query.all()
    dict_list = [item.get_json() for item in records]
    return jsonify(dict_list)

@app.route('/api/week_timetable/<int:spec_id>', methods=['GET'])
def get_records_by_speciality(spec_id):
    records = db.session.query(models.WeekTimetable).filter(models.Doctor.speciality_id==spec_id).all()
    dict_list = [item.get_json() for item in records]
    return jsonify(dict_list)

@app.route('/api/week_timetable', methods=['POST'])
@login_required
def update_record_week():
    if not request.json or not 'doctor_id' in request.json:
        return jsonify({'Error': 400, "Message" : "Request must to have JSON. Field 'doctor_id' is mandatory"}), 400

    doctor = models.Doctor.query.get(request.json['doctor_id'])
    if doctor is None:
        return jsonify({'Error': 400, 'Message': 'Doctor with this id is not existing!'}), 400
    record = models.WeekTimetable.query.filter_by(doctor_id=request.json['doctor_id']).first()
    if record is None:
        record = models.WeekTimetable()
    record.doctor = doctor
    if 'monday' in request.json:
        record.monday = request.json['monday']
    if 'tuesday' in request.json:
        record.tuesday = request.json['tuesday']
    if 'wednesday' in request.json:
        record.wednesday = request.json['wednesday']
    if 'thursday' in request.json:
        record.thursday = request.json['thursday']
    if 'friday' in request.json:
        record.friday = request.json['friday']
    if 'saturday' in request.json:
        record.saturday = request.json['saturday']

    db.session.add(record)
    db.session.commit()

    return jsonify(record.get_json()), 201

@app.route('/api/week_timetable/<int:id>', methods = ['DELETE'])
@login_required
def delete_week_record(id):
    record = models.WeekTimetable.query.get(id)
    if record == None:
        return jsonify({"Error": "404", "Message": "Reocrd with this id is not existing."})
    json = jsonify(record.get_json())
    db.session.delete(models.WeekTimetable.query.get(id))
    db.session.commit()
    return json