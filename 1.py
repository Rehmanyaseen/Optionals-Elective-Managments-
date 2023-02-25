class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.courses = []
        self.electives = []

    def enroll_in_course(self, course_id):
        self.courses.append(course_id)

    def unenroll_from_course(self, course_id):
        self.courses.remove(course_id)

    def enroll_in_elective(self, elective_id):
        self.electives.append(elective_id)

    def unenroll_from_elective(self, elective_id):
        self.electives.remove(elective_id)

    def get_courses(self):
        return self.courses

    def get_electives(self):
        return self.electives


class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name
        self.students = []

    def add_student(self, student_id):
        self.students
