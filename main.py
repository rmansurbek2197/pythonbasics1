class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.courses = {}

    def add_course(self, course, grade):
        self.courses[course] = grade

    def get_courses(self):
        return self.courses


class Course:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def get_info(self):
        return f"Course: {self.name}, Code: {self.code}"


class Grade:
    def __init__(self, score):
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"
        elif self.score >= 70:
            return "C"
        elif self.score >= 60:
            return "D"
        else:
            return "F"


class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        self.students[student.id] = student

    def get_student(self, id):
        return self.students.get(id)


system = StudentManagementSystem()
math = Course("Math", "MATH101")
student1 = Student("John Doe", "S001")
student1.add_course(math.code, Grade(85))
system.add_student(student1)
print(student1.get_courses())
print(system.get_student("S001").get_courses())
math_grade = student1.get_courses().get(math.code)
print(math_grade.get_grade())