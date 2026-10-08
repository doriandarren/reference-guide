"""
We want to implement a simple system to manage a school, keeping track of students and the courses they are enrolled in.

Class Course: should represent a subject (e.g., Mathematics, Science) and include attributes such as
course_name and course_code.
Class Student: should include attributes like
student_id, name, and
enrolled_courses (a list of Course objects).
External function is_enrolled(student, course_code): this function
must not be part of any class. It should receive a Student object and a
course_code, and return True if the student is enrolled in that course,
or False otherwise.
Check the example code to see how to implement your classes and the external function correctly.

"""



# Your code goes here

#---------------------------
# Course
#---------------------------
class Course:

    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code

    def __repr__(self):
        return f"{self.course_name} {self.course_code}"


#---------------------------
# Student
#---------------------------
class Student:

    def __init__(self, student_id, name, enrolled_courses = []):
        self.student_id = student_id
        self.name = name
        self.enrolled_courses = enrolled_courses


    def __repr__(self):
        return f"{self.student_id} {self.name} {self.enrolled_courses}"



def is_enrolled(student, course_code):


    flag = False

    for ele in student.enrolled_courses:
        if ele.course_code == course_code:
            flag = True


    print(student)


    return flag
        

# Example usage

# Enroll students to courses
math = Course("Mathematics", "MATH_1")
english = Course("English", "ENG_1")
alice = Student(1, "Alice")
bob = Student(2, "Bob")

alice.enrolled_courses.append(math)
bob.enrolled_courses.extend([math, english])

# Check enrollment
print(f"Is Alice enrolled in MATH_1? {'Yes' if is_enrolled(alice, 'MATH_1') else 'No'}")
print(f"Is Bob enrolled in ENG_1? {'Yes' if is_enrolled(bob, 'ENG_1') else 'No'}")
print(f"Is Bob enrolled in ENG_1? {'Yes' if is_enrolled(alice, 'ENG_1') else 'No'}")