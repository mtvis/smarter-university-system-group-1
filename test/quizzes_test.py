import unittest
import os
from datetime import datetime

from datetime import datetime, timedelta

from app.controllers.quizzes_controller import QuizzesController

class QuizzesTest(unittest.TestCase):

    def setUp(self):
        # Run tests on non-production data
        self.ctrl = QuizzesController('quizzes_test.py')
        """
        Implement this function and two more that
        execute the code and make it fail.
        """
        self.assertTrue(True, 'Example assertion.')
    
    def test_add_quiz(self):
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
        self.ctrl.clear_data()
        self.assertIsNone(bad_quiz, "The Quiz can not be retrieved.")

    def test_add_question(self):
       
        quiz_id = self.ctrl.add_quiz("Quiz Name", "Quiz Details", datetime, datetime)
        # Check that we have one discussion in the list
        quizzes = self.ctrl.get_quizzes()
        self.assertEquals(len(quizzes), 1, "There is exactly one Quiz.")
        # Check that we can retrieve the added discussion
        quiz = self.ctrl.get_quiz_by_id(quiz_id)
        self.assertIsNotNone(quiz, "The Quiz can be retrieved.")

        question_id = self.ctrl.add_question( quiz_id,"Question Name", "Question Details" "Question String")
        question = self.ctrl.get_question_by_id (question_id)
        self.ctrl.clear_data()
        self.assertIsNotNone(question, "The Question can be retrieved.")

    def test_add_answer(self):
        self.ctrl.clear_data()
        quiz_id = self.ctrl.add_quiz("Quiz Name", "Quiz Details", datetime, datetime)
        # Check that we have one discussion in the list
        quizzes = self.ctrl.get_quizzes()
        self.assertEquals(len(quizzes), 1, "There is exactly one Quiz.")
        # Check that we can retrieve the added discussion
        quiz = self.ctrl.get_quiz_by_id(quiz_id)
        self.assertIsNotNone(quiz, "The Quiz can be retrieved.")

        self.ctrl.clear_data()
        question_id = self.ctrl.add_question( quiz_id,"Question Name", "Question Details" "Question String")
        question = self.ctrl.get_question_by_id (question_id)
        self.assertIsNotNone(question, "The Question can be retrieved.")

        answer_id = self.ctrl.add_answer (question_id, "Answer Detail", True)
        self.assertIsNotNone(answer_id, "The Answer can be retrieved.")

    # So the unit tests that Matthew wrote are below this comment while the ones Sameer wrote are above
        
    def test_expose_failure_01(self):
        self.ctrl.clear_data()
        # The following line tries to add a None type quiz, crashing at line 63 in quizzes_controller.py
        quiz_id = self.ctrl.add_quiz(None, None, 
                                     datetime(year=2020, month=5, day=17), datetime(year=2020, month=5, day=23))
        
        self.ctrl.remove_quiz(quiz_id)
        quizzes = self.ctrl.get_quizzes()
        self.assertEquals(len(quizzes), 1, "There is exactly one quiz.")

    def test_expose_failure_02(self):
    
        # Made an entire list of quizzes with questions and answers for future reference
        quiz_id_2 = self.ctrl.add_quiz("Quiz 2 Title", "Here is some text for quiz 2", 
                                     datetime(year=2022, month=7, day=21), datetime(year=2022, month=7, day=25))
        
        question_id_2 = self.ctrl.add_question(quiz_id_2, "Question 2 Title", "What is the capital of France?")
        answer_id_2_1 = self.ctrl.add_answer(question_id_2, float, False)
        answer_id_2_2 = self.ctrl.add_answer(question_id_2, "Paris", True)

        # Error case #2: This action tries to save_data containing a float, crashing at line 21 in data_loader.py 
        self.ctrl.get_quiz_by_id(None)
        self.ctrl.remove_quiz(None)
        self.ctrl.clear_data()
        self.assertEquals(self.ctrl.get_quiz_by_id(quiz_id_2), self.ctrl.get_quizzes()[1])

    def test_expose_failure_03(self):
        self.ctrl.clear_data()
        # Data loaded from the quizzes_test.json file upon creation of ctrl reads a 
        self.ctrl.add_answer(b"answer","test",True)
        # Error case #3: (correctly) causes an index out of bounds exception crash
        self.assertIsNotNone(self.ctrl.get_quizzes()[1].sections[1]) 

        
if __name__ == '__main__':
    unittest.main()
