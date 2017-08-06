""" Answer Type Dao """
from .base_dao import BaseDao
import ttqpy.db as db


class UserDao(BaseDao):

    def __init__(self, session):
        super().__init__(session)

    def find_all(self):
        return self.session.query(db.User).all()

    def find(self, user_id):
        return self.session.query(db.User).filter(
            db.User.id == user_id).one()

    def find_by_username(self, username):
        return self.session.query(db.User).filter(
            db.User.username == username).first()

    def find_by_token(self, token):
        return self.session.query(db.User).filter(
            db.User.token == token).first()

    def create(self, username, password, first_name, last_name, email):
        new_user = db.User(username, first_name, last_name, email)
        new_user.hash_password(password)
        new_user.generate_auth_token()
        self.session.add(new_user)
        self.session.commit()
        return new_user
