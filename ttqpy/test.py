""" Test base class """
from ttqpy import QuestionType as qt
from ttqpy import OneToX


class Test:

    def __init__(self, subject, name, weight):
        self.subject = subject
        self.name = name
        self.questions = dict()
        self.weight = weight
        self.counter = OneToX()

    def add_question(self, question, answer, question_type=qt.Multiple_Choice, options=None):
        self.questions[self.counter.get_next()] = question_type.question(question, answer, options)

    def save(self, session):
