from flask.ext.login import login_user
from flask.ext.login import login_required
from flask.ext.login import logout_user
from flask.ext.login import current_user
from flask import request
from flask import jsonify

from app import app
from app import models

@app.route("/api/login", methods=["POST"])
def login():
    if not request.json or not 'email' in request.json or not 'password' in request.json :
        return jsonify({'Error': 400, "Message" : "Fields password and email are mandatory!"}), 400
    email = request.json["email"]
    password = request.json["password"]

    user = models.User.query.filter_by(email=email).first()
    if user == None:
        return jsonify({'Error': 404, "Message": "User with this email is not existing."}), 404
    if user.password != password:
        return jsonify({'Error': 400, "Message": "Invalid password"}), 400

    login_user(user)
    return jsonify(user.get_json())

@app.route("/api/logout")
@login_required
def logout():
    logout_user()
    return jsonify({'Info': 200, "Message": "Logout success."}), 200

@app.route("/api/user/current_user", methods=["GET"])
@login_required
def get_current_user():
    return jsonify(current_user.get_json())

@app.errorhandler(401)
def unauth(e):
    return jsonify({'Error': 401, "Message": "Unauthorized."}), 400
