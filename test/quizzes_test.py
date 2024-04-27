import unittest

from datetime import datetime, timedelta

from app.controllers.quizzes_controller import QuizzesController

class QuizzesTest(unittest.TestCase):

    def setUp(self):
        # Run tests on non-production data
        self.ctrl = QuizzesController('quizzes_test.py')
        
    def test_expose_failure_01(self):
        """
        Implement this function and two more that
        execute the code and make it fail.
        """
        self.assertTrue(True, 'Example assertion.')
    
    def test_add_quiz()

        self.ctrl.clear_data()
       
        quiz_id = self.ctrl.add_quiz("Quiz Name", "Quiz Details", datetime, datetime)
        # Check that we have one discussion in the list
        quizzes = self.ctrl.get_quizzes()
        self.assertEquals(len(quizzes), 1, "There is exactly one Quiz.")
        # Check that we can retrieve the added discussion
        quiz = self.ctrl.get_quiz_by_id(quiz_id)
        self.assertIsNotNone(quiz, "The Quiz can be retrieved.")

        bad_quiz_id = self.ctrl.add_quiz("Bad Quiz Name", "Bad Quiz Details", datetime.now(), datetime)
        # Check that we can retrieve the added discussion
        bad_quiz = self.ctrl.get_quiz_by_id(bad_quiz_id)
        self.assertIsNone(bad_quiz, "The Quiz can not be retrieved.")

    def test_add_question()
        quiz_id = self.ctrl.add_quiz("Quiz Name", "Quiz Details", datetime, datetime)
        # Check that we have one discussion in the list
        quizzes = self.ctrl.get_quizzes()
        self.assertEquals(len(quizzes), 1, "There is exactly one Quiz.")
        # Check that we can retrieve the added discussion
        quiz = self.ctrl.get_quiz_by_id(quiz_id)
        self.assertIsNotNone(quiz, "The Quiz can be retrieved.")

        question_id = self.ctrl.add_question( quiz_id,"Question Name", "Question Details" "Question String")
        question = self.ctrl.get_question_by_id (question_id)
        self.assertIsNotNone(question, "The Question can be retrieved.")



    def test_add_answer()
        quiz_id = self.ctrl.add_quiz("Quiz Name", "Quiz Details", datetime, datetime)
        # Check that we have one discussion in the list
        quizzes = self.ctrl.get_quizzes()
        self.assertEquals(len(quizzes), 1, "There is exactly one Quiz.")
        # Check that we can retrieve the added discussion
        quiz = self.ctrl.get_quiz_by_id(quiz_id)
        self.assertIsNotNone(quiz, "The Quiz can be retrieved.")


        question_id = self.ctrl.add_question( quiz_id,"Question Name", "Question Details" "Question String")
        question = self.ctrl.get_question_by_id (question_id)
        self.assertIsNotNone(question, "The Question can be retrieved.")

        answer_id = self.ctrl.add_answer (question_id, "Answer Detail", True)
        self.assertIsNotNone(answer_id, "The Answer can be retrieved.")



if __name__ == '__main__':
    unittest.main()