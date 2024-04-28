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

    # So the unit tests that Matthew wrote are below this comment while the ones Sameer wrote are above
        
    def test_expose_failure_01(self):
        self.ctrl.clear_data()

        quiz_id = self.ctrl.add_quiz("Quiz 1 Title", "Here is some text for quiz 1", 
                                     datetime(year=2020, month=5, day=17), datetime(year=2020, month=5, day=23))
        quizzes = self.ctrl.get_quizzes()
        self.ctrl.remove_quiz(quiz_id)
        quizzes = self.ctrl.get_quizzes()
        self.ctrl.remove_quiz(quiz_id)
        quizzes = self.ctrl.get_quizzes()
        # Error case #1: trying to call remove_quiz when there are no quizzes to remove
        self.assertEquals(len(quizzes), 1, "There is exactly one quiz.")

    def test_expose_failure_02(self):
        self.ctrl.clear_data()

        # Made an entire list of quizzes with questions and answers for future reference
        quiz_id = self.ctrl.add_quiz("Quiz 1 Title", "Here is some text for quiz 1", 
                                     datetime(year=2020, month=5, day=17), datetime(year=2020, month=5, day=23))
        quiz_id_2 = self.ctrl.add_quiz("Quiz 2 Title", "Here is some text for quiz 2", 
                                     datetime(year=2022, month=7, day=21), datetime(year=2022, month=7, day=25))
        quiz_id_3 = self.ctrl.add_quiz("Quiz 3 Title", "Here is some text for quiz 3", 
                                     datetime(year=2024, month=9, day=25), datetime(year=2024, month=10, day=3))
        
        question_id = self.ctrl.add_question(quiz_id, "Question 1-1 Title", "What color is that?")
        answer_id_1_1 = self.ctrl.add_answer(question_id, "Orange", True)
        answer_id_1_2 = self.ctrl.add_answer(question_id, "Blue", False)
        question_id_1_2 = self.ctrl.add_question(quiz_id, "Question 1-2 Title", "What is your favorite color?")
        answer_id_1_2_1 = self.ctrl.add_answer(question_id_1_2, "Blue", True)
        answer_id_1_2_2 = self.ctrl.add_answer(question_id_1_2, "Gray", False)

        question_id_2 = self.ctrl.add_question(quiz_id_2, "Question 2 Title", "What is the capital of France?")
        answer_id_2_1 = self.ctrl.add_answer(question_id_2, "Versailles", False)
        answer_id_2_2 = self.ctrl.add_answer(question_id_2, "Paris", True)
        
        # This will be loaded in the next case
        self.ctrl._save_data()

        self.assertEquals(self.ctrl.get_quiz_by_id(quiz_id), self.ctrl.get_quizzes()[0])
        self.assertEquals(self.ctrl.get_quiz_by_id(quiz_id_2), self.ctrl.get_quizzes()[1])
        # Error case #2: trying to incorrectly access quiz 3
        self.assertEquals(self.ctrl.get_quiz_by_id(quiz_id_3), self.ctrl.get_quizzes()[1])

    def test_expose_failure_03(self):
        # Data loaded from the quizzes_test.json file
        self.ctrl._load_data()
        self.assertEquals(len(self.ctrl.get_quizzes()), 3)
        a_quiz = self.ctrl.get_quizzes()[1]
        a_question = a_quiz.sections[0]
        print(a_quiz)
        print(a_question)
        self.assertEquals(self.ctrl.get_question_by_id(a_question.id), a_question)
        self.assertEquals(self.ctrl.get_quiz_by_id(a_quiz.id), a_quiz)
        # Error case #3: (correctly) causes an index out of bounds exception crash
        self.assertIsNotNone(self.ctrl.get_quizzes()[1].sections[1]) 

        
if __name__ == '__main__':
    unittest.main()
