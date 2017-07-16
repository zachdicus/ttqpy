import enum
from collections import OrderedDict


class QCounter:
    def __init__(self):
        self.data = None
        self.index = 0

    def get_next(self):
        item = self.data[self.index]
        self.index += 1
        return item


class AToZ(QCounter):

    def __init__(self):
        super().__init__()
        self.data = [chr(x) for x in range(ord('A'), ord('Z') + 1)]


class OneToX(QCounter):
    def __init__(self):
        super().__init__()
        self.data = range(1, 1000)


class Question:

    def __init__(self, question, correct_answer, manually_graded=False):
        self.question = question
        self.correct_answer = correct_answer
        self.user_answer = None
        self.manually_graded = manually_graded
        self.options = None

    def is_correct(self):
        if self.manually_graded:
            raise ValueError("This questions is manually graded")

        user_answer = self.user_answer.lower()

        if isinstance(self.correct_answer, list):
            for answer in self.correct_answer:
                if user_answer == answer.lower():
                    return True
        elif user_answer == self.correct_answer.lower():
            return True
        return False

    def provide_answer(self, user_answer):
        self.user_answer = user_answer


class MultipleChoice(Question):

    def __init__(self, question, correct_answer, options):
        super().__init__(question, correct_answer)

        self.options = OrderedDict()
        self.labels = AToZ()

        # Check the options
        if options is None:
            raise ValueError("Multiple choice questions must have options")

        for option in options:
            self.options[self.labels.get_next()] = option


class TrueFalse(Question):
    def __init__(self, question, correct_answer, options=None):
        super().__init__(question, correct_answer)
        self.options = OrderedDict({"True": True, "False": False})


class QuestionType(enum.Enum):

    def __new__(cls, *args, **kwargs):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __init__(self, question):
        self.question = question

    Calculated = Question
    Description = Question
    Essay = Question
    Matching = Question
    Embedded_Answers = Question
    Multiple_Choice = MultipleChoice
    Short_Answer = Question
    Numerical = Question
    True_False = TrueFalse
