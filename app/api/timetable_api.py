from app import models
from app import app
from flask import jsonify

@app.route('/api/timetable', methods=['GET'])
def get_timetable():
    timetables = models.Timetable.query.all()
    dict_list = [item.get_json() for item in timetables]
    return jsonify(dict_list)