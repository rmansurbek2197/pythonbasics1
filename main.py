class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        self.courses.remove(course)

class Course:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.students = []
        self.grade = None

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def set_grade(self, grade):
        self.grade = grade

class Grade:
    def __init__(self, score, letter):
        self.score = score
        self.letter = letter

class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.grades = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        self.courses.remove(course)

    def add_grade(self, grade):
        self.grades.append(grade)

    def print_students(self):
        for student in self.students:
            print(f"Name: {student.name}, ID: {student.id}")

    def print_courses(self):
        for course in self.courses:
            print(f"Name: {course.name}, ID: {course.id}, Grade: {course.grade.score} ({course.grade.letter})")

    def print_grades(self):
        for grade in self.grades:
            print(f"Score: {grade.score}, Letter: {grade.letter}")

system = StudentManagementSystem()

student1 = Student("John Doe", 1)
student2 = Student("Jane Doe", 2)

course1 = Course("Math", 1)
course2 = Course("Science", 2)

grade1 = Grade(90, "A")
grade2 = Grade(80, "B")

system.add_student(student1)
system.add_student(student2)
system.add_course(course1)
system.add_course(course2)
system.add_grade(grade1)
system.add_grade(grade2)

course1.add_student(student1)
course1.add_student(student2)
course1.set_grade(grade1)

course2.add_student(student1)
course2.set_grade(grade2)

system.print_students()
system.print_courses()
system.print_grades()