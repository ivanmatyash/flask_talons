import datetime
from app import models
from app import app
from app import db
from flask import jsonify
from flask import request
from flask.ext.login import login_required

@app.route('/api/people', methods=['GET'])
def get_people():
    people = models.User.query.all()
    dict_list = [item.get_json() for item in people]
    return jsonify(dict_list)

@app.route('/api/people/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = models.User.query.get(user_id)
    if user == None:
        return jsonify({"Error" : "404"})
    return jsonify(user.get_json())

@app.route('/api/people', methods=['POST'])
def create_user():
    if not request.json or not 'email' in request.json\
            or not 'password' in request.json:
        return jsonify({'Error': 400, "Message" : "Fields password and email are mandatory!"}), 400

    if "parent_id" in request.json:
        parent = models.User.query.get(int(request.json["parent_id"]))
    else:
        parent = None
    try:
        user = models.User(email=request.json['email'],
                           password=request.json['password'],
                           name=request.json.get('name', "Anonym"),
                           birthday=datetime.datetime.strptime(request.json.get('birthday', "25-10-1900"), '%d-%m-%Y'),
                           parent_id=request.json.get("parent_id", -1),
                           parent=parent,
                           photo_url = request.json.get("photo_url", "https://www.b17.ru/foto/uploaded/b69a564c47110acefb8c986f768210ac.jpg")
        )
        db.session.add(user)
        db.session.commit()
    except:
        user = None

    if user == None:
        return jsonify({'Error': 500, 'Message': 'User is None'}), 500

    return jsonify(user.get_json()), 201

@app.route('/api/people/<int:id>', methods = ['DELETE'])
@login_required
def delete_user(id):
    user = models.User.query.get(id)
    if user == None:
        return jsonify({"Error": "404", "Message": "User with this id is not existing."})
    json = jsonify(user.get_json())
    db.session.delete(models.User.query.get(id))
    db.session.commit()
    return json