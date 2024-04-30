import unittest
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
    
    # Fails line 63 in add quiz
    def test_expose_failure_01(self):
        self.ctrl.clear_data()
        self.ctrl.add_quiz(None, "Here is some text for quiz 1", 
                                     datetime(year=2020, month=5, day=17), datetime(year=2020, month=5, day=23))
        self.ctrl.add_quiz("Quiz 1 Title", None, 
                                     datetime(year=2020, month=5, day=17), datetime(year=2020, month=5, day=23))
        quizzes = self.ctrl.get_quizzes()
        # Error case #1: trying to call remove_quiz when there are no quizzes to remove
        self.assertEquals(len(quizzes), 2, "There is exactly two quizzes.")

    # Fails line 81 is add_question()
    def test_expose_failure_02(self):
        self.ctrl.clear_data()
        quiz_id = self.ctrl.add_quiz("Quiz 1 Title", "Here is some text for quiz 1", 
                                     datetime(year=2020, month=5, day=17), datetime(year=2020, month=5, day=23))
        
        question_id = self.ctrl.add_question(quiz_id, b"question title", "question text")
        self.ctrl.add_answer(question_id, "this is the correct answer", False)
        question = self.ctrl.get_question_by_id(question_id)
        # This will be loaded in the next case
        self.ctrl._save_data()

        self.assertEquals(self.ctrl.get_quiz_by_id(quiz_id), self.ctrl.get_quizzes()[0])
        # Error case #2: trying to incorrectly access quiz 3
        self.assertEquals(question_id, question.id)

    # Fails on line 66 of add_quiz()
    def test_expose_failure_03(self):
        self.ctrl.clear_data()
        quiz_id = self.ctrl.add_quiz("Quiz 1 Title", b"Here is some text for quiz 1", 
                                     None, None)
        
        
        question_id = self.ctrl.add_question(None, "question title", "question text")
        self.ctrl.add_answer(question_id, 1.1, b"test")
        self.ctrl.get_quiz_by_id(None)
        self.ctrl.remove_quiz(None)
        self.ctrl.clear_data()
        # This will be loaded in the next case
        self.ctrl.print_quiz(quiz_id)
        self.assertEquals(self.ctrl.get_quiz_by_id(quiz_id), self.ctrl.get_quizzes()[0])
        
    def test_expose_failure_04(self):
        self.ctrl.clear_data()
        quiz_id = self.ctrl.add_quiz("Quiz 1 Title", "Here is some text for quiz 1", 
                                     datetime(year=2020, month=5, day=17), datetime(year=2020, month=5, day=23))
        
        
        question_id = self.ctrl.add_question(quiz_id, "question title", "question text")
        self.ctrl.add_answer(question_id, b"test", b"test")
        self.ctrl._save_data()
        self.ctrl.clear_data()
        # This will be loaded in the next case
        self.ctrl.print_quiz(quiz_id)
        self.assertEquals(self.ctrl.get_quiz_by_id(quiz_id), self.ctrl.get_quizzes()[0])   

if __name__ == '__main__':
    unittest.main()
