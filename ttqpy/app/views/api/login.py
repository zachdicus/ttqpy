from flask import Blueprint, abort, request, jsonify
from ttqpy.db import db
from ttqpy.db.dao import UserDao
from functools import wraps

login_api = Blueprint('login_api', 'login_api', url_prefix='/api/v1/login')


@login_api.route('/', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user_dao = UserDao(db.session)
    if username is None or password is None:
        abort(400, "Username/Password is required")  # missing arguments
    user = user_dao.find_by_username(username)
    if user is None:
        abort(400, "Username not passed or incorrect")  # existing user
    if not user.verify_password(password):
        abort(400, "Password is incorrect")
    if not user.email_verified:
        abort(400, "Email has not been verified")
    user.generate_auth_token()
    return jsonify({'validated': True, "token": user.token})


def login_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        user_dao = UserDao(db.session)
        try:
            auth_type, token = request.headers['Authorization'].split(
                None, 1)
            if token is None:
                json = jsonify({"loginRequired": True, "message": "Empty token supplied"})
                json.status_code = 400
                return json
            else:
                user = user_dao.find_by_token(token)
                if user is None:
                    json = jsonify({"loginRequired": True, "message": "Bad token or expired token"})
                    json.status_code = 400
                    return json
        except Exception as e:
            json = jsonify({"loginRequired": True, "message": "No token passed {}".format(e)})
            json.status_code = 400
            return json
        return func(*args, **kwargs)
    return decorated