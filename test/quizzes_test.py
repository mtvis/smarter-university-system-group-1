import unittest
from datetime import datetime
from app.controllers.quizzes_controller import QuizzesController
from app.utils.data_loader import save_data
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
        #Check with incorrect quiz title
        self.ctrl.add_quiz(None, "Here is some text for quiz 1", 
                                     datetime(year=2020, month=5, day=17), datetime(year=2020, month=5, day=23))
        self.ctrl.add_quiz("Quiz 1 Title", None, 
                                     datetime(year=2020, month=5, day=17), datetime(year=2020, month=5, day=23))
        quizzes = self.ctrl.get_quizzes()
        # Check that two quizzes were created
        self.assertEquals(len(quizzes), 2, "There is exactly two quizzes.")

    # Fails line 81 is add_question()
    def test_expose_failure_02(self):
        self.ctrl.clear_data()
        quiz_id = self.ctrl.add_quiz("Quiz 1 Title", "Here is some text for quiz 1", 
                                     datetime(year=2020, month=5, day=17), datetime(year=2020, month=5, day=23))
        #Check with incorrect quiz title
        question_id = self.ctrl.add_question(quiz_id, b"question title", "question text")
        self.ctrl.add_answer(question_id, "this is the correct answer", False)
        question = self.ctrl.get_question_by_id(question_id)
        # This will be loaded in the next case
        self.ctrl._save_data()

        #Check that the quiz saved
        self.assertEquals(self.ctrl.get_quiz_by_id(quiz_id), self.ctrl.get_quizzes()[0])
        #Check that the question ID matches what was returned
        self.assertEquals(question_id, question.id)

    # Fails on line 66 of add_quiz()
    def test_expose_failure_03(self):
        self.ctrl.clear_data()
        #Check with incorrect quiz text
        quiz_id = self.ctrl.add_quiz("Quiz 1 Title", b"Here is some text for quiz 1", 
                                     None, None)
        # Print the quiz
        self.ctrl.print_quiz(quiz_id)
        self.assertEquals(self.ctrl.get_quiz_by_id(quiz_id), self.ctrl.get_quizzes()[0])
        
    # Fails on line 94 of add_answer()
    def test_expose_failure_04(self):
        self.ctrl.clear_data()
        quiz_id = self.ctrl.add_quiz("Quiz 1 Title", "Here is some text for quiz 1", 
                                     datetime(year=2020, month=5, day=17), datetime(year=2020, month=5, day=23))
        question_id = self.ctrl.add_question(quiz_id, "question title", "question text")
        #Check with incorrect answer data
        self.ctrl.add_answer(question_id, b"test", b"test")
        self.assertEquals(self.ctrl.get_quiz_by_id(quiz_id), self.ctrl.get_quizzes()[0])

    # Fails on line 19 in __init__() function
    def test_expose_failure_05(self):
        #Create a fake malformed file to test the QuizzesController __init__ method
        test_text = "{'test':""} }"
        save_data("fake.json", test_text)
        self.ctrl = QuizzesController("fake.json")
        self.ctrl.add_quiz("Quiz 1 Title", None, 
                                     datetime(year=2020, month=5, day=17), datetime(year=2020, month=5, day=23))
        quizzes = self.ctrl.get_quizzes()
        # Check that one quizzes were created
        self.assertEquals(len(quizzes), 1, "There is exactly two quizzes.")


if __name__ == '__main__':
    unittest.main()
