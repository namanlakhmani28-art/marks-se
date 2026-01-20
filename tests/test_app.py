import unittest
from src.app import Student, StudentMarksSystem

class TestStudent(unittest.TestCase):
    def test_add_marks_and_grade(self):
        s = Student(1, "Naman")
        s.add_marks("Math", 95)
        s.add_marks("Science", 85)
        self.assertEqual(s.calculate_grade(), "A")

    def test_generate_report(self):
        s = Student(2, "Eshana")
        s.add_marks("Math", 70)
        s.add_marks("Science", 75)
        report = s.generate_report()
        self.assertIn("Grade: B", report)

class TestStudentMarksSystem(unittest.TestCase):
    def setUp(self):
        self.sms = StudentMarksSystem()
        self.sms.add_student(1, "Naman")

    def test_add_student_and_marks(self):
        self.sms.add_marks(1, "Math", 90)
        self.sms.add_marks(1, "Science", 80)
        report = self.sms.get_report(1)
        self.assertIn("Grade: A", report)

    def test_student_not_found(self):
        with self.assertRaises(ValueError):
            self.sms.add_marks(2, "Math", 90)

if __name__ == "__main__":
    unittest.main()

