import unittest
from src.app import StudentMarksSystem

class TestSprint2(unittest.TestCase):

    def test_calculate_grade_A_plus(self):
        sms = StudentMarksSystem()
        sms.add_student(201, "Ravi")
        sms.add_marks(201, "Math", 95)
        self.assertEqual(sms.calculate_grade(201), "A+")

    def test_calculate_grade_A(self):
        sms = StudentMarksSystem()
        sms.add_student(202, "Maya")
        sms.add_marks(202, "Math", 85)
        self.assertEqual(sms.calculate_grade(202), "A")

    def test_calculate_grade_B(self):
        sms = StudentMarksSystem()
        sms.add_student(203, "John")
        sms.add_marks(203, "Math", 75)
        self.assertEqual(sms.calculate_grade(203), "B")

if __name__ == "__main__":
    unittest.main()

