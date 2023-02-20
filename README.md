# Optionals-Elective-Managments-Objects:

Course
Student
Enrollment
Elective
Optional
Attributes and behaviors:

Course
Attributes: course_id, course_name, course_description, course_credit_hours
Behaviors: get_course_id(), get_course_name(), get_course_description(), get_course_credit_hours(), set_course_id(course_id), set_course_name(course_name), set_course_description(course_description), set_course_credit_hours(course_credit_hours)
Student
Attributes: student_id, student_name, student_email, student_major
Behaviors: get_student_id(), get_student_name(), get_student_email(), get_student_major(), set_student_id(student_id), set_student_name(student_name), set_student_email(student_email), set_student_major(student_major)
Enrollment
Attributes: course_id, student_id, grade
Behaviors: get_course_id(), get_student_id(), get_grade(), set_course_id(course_id), set_student_id(student_id), set_grade(grade)
Elective
Attributes: elective_id, elective_name, elective_description
Behaviors: get_elective_id(), get_elective_name(), get_elective_description(), set_elective_id(elective_id), set_elective_name(elective_name), set_elective_description(elective_description)
Optional
Attributes: optional_id, optional_name, optional_description
Behaviors: get_optional_id(), get_optional_name(), get_optional_description(), set_optional_id(optional_id), set_optional_name(optional_name), set_optional_description(optional_description)
Classes:

Course
Attributes: course_id, course_name, course_description, course_credit_hours
Behaviors: get_course_id(), get_course_name(), get_course_description(), get_course_credit_hours(), set_course_id(course_id), set_course_name(course_name), set_course_description(course_description), set_course_credit_hours(course_credit_hours)
Student
Attributes: student_id, student_name, student_email, student_major
Behaviors: get_student_id(), get_student_name(), get_student_email(), get_student_major(), set_student_id(student_id), set_student_name(student_name), set_student_email(student_email), set_student_major(student_major)
Enrollment
Attributes: course_id, student_id, grade
Behaviors: get_course_id(), get_student_id(), get_grade(), set_course_id(course_id), set_student_id(student_id), set_grade(grade)
Elective
Attributes: elective_id, elective_name, elective_description
Behaviors: get_elective_id(), get_elective_name(), get_elective_description(), set_elective_id(elective_id), set_elective_name(elective_name), set_elective_description(elective_description)
Optional
Attributes: optional_id, optional_name, optional_description
Behaviors: get_optional_id(), get_optional_name(), get_optional_description(), set_optional_id(optional_id), set_optional_name(optional_name), set_optional_description(optional_description)
Now, let's write the code:

python
Copy code
class Course:
    def _init_(self, course_id, course_name, course_description, course_credit_hours):
        self.course_id = course_id
        self.course_name = course_name
        self.course_description = course_description
        self.course_credit_hours = course_credit_hours
        
    def get_course_id(self):
        return self.course_id
    
    def get_course_name(self):
        return self.course_name
    
    def get_course_description(self):
        return self.course_description
    
    def get_course_credit_hours(self):
        return self.course_credit_hours
    
   




