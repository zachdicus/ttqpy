""" Test base class """
from ttqpy import QuestionType as qt

class Test:

    def __int__(self, weight):
        self.questions = dict()
        self.weight = weight

    def add_question(self, question, answer, question_type=qt.Multiple_Choice, options=None):

        question_type(question, answer, options)