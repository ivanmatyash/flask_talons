from app import models
from app import app
from flask import jsonify

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

