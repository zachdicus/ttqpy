""" Base Dao class """
import logging


class BaseDao:
    def __init__(self, session):
        self.logger = logging.Logger(__name__)
        self.session = session
