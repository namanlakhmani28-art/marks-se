class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.marks = {}

    def add_marks(self, subject, mark):
        """Add marks for a subject"""
        self.marks[subject] = mark

    def calculate_grade(self):
        """Calculate grade based on average marks"""
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

    def generate_report(self):
        """Return a formatted report for the student"""
        report = f"Student ID: {self.student_id}\n"
        report += f"Name: {self.name}\n"
        report += "Marks:\n"
        for subject, mark in self.marks.items():
            report += f"  {subject}: {mark}\n"
        report += f"Grade: {self.calculate_grade()}\n"
        return report


class StudentMarksSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name):
        if student_id in self.students:
            raise ValueError("Student ID already exists")
        self.students[student_id] = Student(student_id, name)

    def add_marks(self, student_id, subject, mark):
        if student_id not in self.students:
            raise ValueError("Student not found")
        self.students[student_id].add_marks(subject, mark)

    def get_report(self, student_id):
        if student_id not in self.students:
            raise ValueError("Student not found")
        return self.students[student_id].generate_report()


# Optional: run a quick demo
if __name__ == "__main__":
    sms = StudentMarksSystem()
    sms.add_student(1, "Naman")
    sms.add_marks(1, "Math", 90)
    sms.add_marks(1, "Science", 85)
    print(sms.get_report(1))

