from app import models
from app import app
from flask import jsonify

@app.route('/api/people', methods=['GET'])
def get_people():
    people = models.User.query.all()
    dict_list = [item.get_json() for item in people]
    return jsonify(dict_list)