from flask import Blueprint, abort, request, jsonify, current_app
from ttqpy.db import db
from ttqpy.db.dao import UserDao
from flask_mail import Message

user_api = Blueprint('user_api', 'user_api', url_prefix='/api/v1/user')


@user_api.route('/', methods=['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    first_name = request.json.get('firstName')
    last_name = request.json.get('lastName')
    email = request.json.get('email')

    user_dao = UserDao(db.session)
    if username is None or password is None:
        abort(400)  # missing arguments
    if user_dao.find_by_username(username) is not None:
        abort(400)  # existing user
    new_user = user_dao.create(username, password, first_name, last_name, email)
    #msg = Message("Confirm Email",
    #              sender="ttqpynoreply@gmail.com",
    #              recipients=["zach.dicus@gmail.com"])
    #msg.body = "Please confirm your email"
    current_app.mail.send(msg)
    return jsonify({'username': new_user.username})
