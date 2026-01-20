# Make src a package
# touch src/__init__.py

from typing import Dict

class Student:
    def __init__(self, student_id: int, name: str):
        self.student_id = student_id
        self.name = name
        self.marks: Dict[str, float] = {}

    def add_marks(self, subject: str, mark: float):
        if mark < 0 or mark > 100:
            raise ValueError("Marks must be between 0 and 100")
        self.marks[subject] = mark

    def calculate_grade(self) -> str:
        if not self.marks:
            return "N/A"
        avg = sum(self.marks.values()) / len(self.marks)
        if avg > 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        else:
            return "F"

    def generate_report(self) -> str:
        report = f"Student ID: {self.student_id}\nName: {self.name}\nMarks:\n"
        for subject, mark in self.marks.items():
            report += f"  {subject}: {mark}\n"
        report += f"Grade: {self.calculate_grade()}\n"
        return report


class StudentMarksSystem:
    def __init__(self):
        self.students: Dict[int, Student] = {}

    def add_student(self, student_id: int, name: str):
        if student_id in self.students:
            raise ValueError("Student already exists")
        self.students[student_id] = Student(student_id, name)

    def add_marks(self, student_id: int, subject: str, mark: float):
        if student_id not in self.students:
            raise ValueError("Student not found")
        self.students[student_id].add_marks(subject, mark)

    def get_report(self, student_id: int) -> str:
        if student_id not in self.students:
            raise ValueError("Student not found")
        return self.students[student_id].generate_report()

