from flask import Blueprint, jsonify
from ttqpy.db import db
from ttqpy.db.dao import AnswerTypeDao
from .login import login_required

answer_types_api = Blueprint('answer_types_api', 'answer_types_api', url_prefix='/api/v1/answertypes')


@answer_types_api.route('')
@login_required
def answer_types():
    dao = AnswerTypeDao(db.session)
    at = list()
    for item in dao.find_all():
        at.append(item.serialize())
    return jsonify(at)