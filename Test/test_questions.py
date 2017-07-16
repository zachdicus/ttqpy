import unittest
from ttqpy.Question import AToZ, OneToX, Question, MultipleChoice, TrueFalse


class TestQuestions(unittest.TestCase):

    def test_counters(self):
        one_to_x_verify = range(1, 1000)
        a_to_z_verify = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                         'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                         'Y', 'Z']

        # Verify the A-Z counter
        a_to_z = AToZ()
        self.assertEqual(a_to_z.data, a_to_z_verify)

        for index in range(0, 25):
            self.assertEqual(a_to_z.get_next(), a_to_z_verify[index])

        # Verify the numeric counter
        one_to_x = OneToX()
        self.assertEqual(one_to_x.data, one_to_x_verify)

        for index in range(0, 999):
            self.assertEqual(one_to_x.get_next(), one_to_x_verify[index])

    def test_questions(self):
        question = Question("What is the widest river in the world", "nile river")

        question.provide_answer("west bend")
        self.assertEqual(question.is_correct(), False)

        question.provide_answer("nile river")
        self.assertEqual(question.is_correct(), True)

        question.provide_answer("NiLe RiVeR")
        self.assertEqual(question.is_correct(), True)

        question = Question("What is the word", ["Bird", "Turd", "Absurd"])
        question.provide_answer("curd")
        self.assertEqual(question.is_correct(), False)

        question.provide_answer("Bird")
        self.assertEqual(question.is_correct(), True)

        question.provide_answer("Turd")
        self.assertEqual(question.is_correct(), True)

        question.provide_answer("absurd")
        self.assertEqual(question.is_correct(), True)

        question = Question("None", "None", True)
        question.provide_answer("what?")
        with self.assertRaises(ValueError):
            question.is_correct()

        question = MultipleChoice("What is false", "False", ["False", "True", "Error", "True"])
        question.provide_answer("Turd")
        self.assertEqual(question.is_correct(), False)

        question.provide_answer("False")
        self.assertEqual(question.is_correct(), True)


        with self.assertRaises(ValueError):
            question = MultipleChoice("What is false", "False", None)

        question = TrueFalse("Is this true?", "True")
        question.provide_answer("False")
        self.assertEqual(question.is_correct(), False)

        question.provide_answer("True")
        self.assertEqual(question.is_correct(), True)