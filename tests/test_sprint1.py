import unittest
from src.app import MarksSystem  # or StudentMarksSystem if using previous code

class TestSprint1(unittest.TestCase):

    # Add student successfully
    def test_add_student_success(self):
        ms = MarksSystem()
        ms.add_student("101", "Asha")
        self.assertIn("101", ms.students)

    # Add student duplicate
    def test_add_student_duplicate(self):
        ms = MarksSystem()
        ms.add_student("101", "Asha")
        with self.assertRaises(ValueError):
            ms.add_student("101", "Asha Again")

    # Add marks successfully
    def test_add_marks_success(self):
        ms = MarksSystem()
        ms.add_student("101", "Asha")
        ms.add_marks("101", 88)
        self.assertEqual(ms.students["101"].marks, 88)

    # Add marks out of range
    def test_add_marks_out_of_range(self):
        ms = MarksSystem()
        ms.add_student("101", "Asha")
        with self.assertRaises(ValueError):
            ms.add_marks("101", 120)

if __name__ == "__main__":
    unittest.main()

