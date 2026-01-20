import unittest
from src.app import StudentMarksSystem

class TestSprint1(unittest.TestCase):

    def test_add_student_success(self):
        sms = StudentMarksSystem()
        sms.add_student(101, "Asha")
        self.assertIn(101, sms.students)

    def test_add_student_duplicate(self):
        sms = StudentMarksSystem()
        sms.add_student(101, "Asha")
        with self.assertRaises(ValueError):
            sms.add_student(101, "Asha Again")

    def test_add_marks_success(self):
        sms = StudentMarksSystem()
        sms.add_student(101, "Asha")
        sms.add_marks(101, "Math", 88)
        self.assertEqual(sms.students[101].marks["Math"], 88)

    def test_add_marks_out_of_range(self):
        sms = StudentMarksSystem()
        sms.add_student(101, "Asha")
        with self.assertRaises(ValueError):
            sms.add_marks(101, "Math", 120)

if __name__ == "__main__":
    unittest.main()

