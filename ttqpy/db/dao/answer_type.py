""" Answer Type Dao """
from .base_dao import BaseDao
import ttqpy.db as db


class AnswerTypeDao(BaseDao):

    def __init__(self, session):
        super().__init__(session)

    def find_all(self):
        return self.session.query(db.AnswerType).all()

    def find(self, answer_type_id):
        return self.session.query(db.AnswerType).filter(
            db.AnswerType.id == answer_type_id).one()
