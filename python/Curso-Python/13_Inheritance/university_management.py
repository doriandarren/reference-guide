"""
Implement a university management system that manages students, courses, and instructors. The system consists of several classes:

A Person class with attributes: name, age, and ID.
A Student class that inherits from Person, with an additional attribute: enrolled_courses (a list of course IDs the student is enrolled in) and a method list_courses() that returns the IDs of the courses the student is enrolled in.
An Instructor class that inherits from Person, with an additional attribute: courses_taught (a list of course IDs the instructor teaches) and a method list_courses() that returns the IDs of the courses the instructor is assigned to.
A Course class with attributes: course_name, course_ID, instructor (an Instructor object), and students (a list of Student objects). This class includes methods: enroll(student) to enroll a student in a course, assign_instructor(instructor) to assign an instructor to the course, and list_students() to return a list of student names enrolled in the course.
The system should also handle edge cases not explicitly listed. For example, a student attempting to enroll in the same course multiple times, which is not allowed.



----------


Implementar un sistema de gestión universitaria que administre estudiantes, cursos e instructores. El sistema consta de varias clases:

Una Personclase con atributos: name, age, y ID.
Una Studentclase que hereda de Person, con un atributo adicional: enrolled_courses(una lista de ID de cursos en los que el estudiante está inscrito) y un método list_courses()que devuelve los ID de los cursos en los que el estudiante está inscrito.
Una Instructorclase que hereda de Person, con un atributo adicional: courses_taught(una lista de ID de cursos que el instructor imparte) y un método list_courses()que devuelve los ID de los cursos a los que está asignado el instructor.
Una Courseclase con atributos: course_name, course_ID, instructor(un Instructor objeto ) y students(una lista de Student objetos ). Esta clase incluye métodos: enroll(student)para inscribir a un estudiante en un curso, assign_instructor(instructor)para asignar un instructor al curso y list_students()para devolver una lista de nombres de estudiantes inscritos en el curso.
El sistema también debe contemplar casos excepcionales no especificados explícitamente. Por ejemplo, un estudiante que intenta inscribirse en el mismo curso varias veces, lo cual no está permitido.


"""






# Your code goes here

#---------------------
# Person
#---------------------
class Person:

    def __init__(self, name, age, identifier):
        self.name = name
        self.age = age
        self.identifier = identifier



#---------------------
# Student
#---------------------
class Student(Person):

    def __init__(self, name, age, identifier):
        super().__init__(name, age, identifier)
        self.enrolled_courses = []


    def list_courses(self):
        return self.enrolled_courses


    def __repr__(self):
        return f"{self.name}"
    




#---------------------
# Instructor
#---------------------
class Instructor(Person):

    def __init__(self, name, age, identifier):
        super().__init__(name, age, identifier)
        self.courses_taught = []


    def list_courses(self):
        return self.courses_taught


    def __repr__(self):
        return f"{self.name} {self.age} {self.identifier} | {self.courses_taught}"



#---------------------
# Course
#---------------------
class Course:

    def __init__(self, course_name, course_ID):

        self.course_name = course_name
        self.course_ID = course_ID
        
        self.instructor = None
        self.students = []


    def enroll(self, student):
        """ inscribir un estudiante en un curso """

        duplicated = any(
            x.identifier == student.identifier
            for x in self.students
        )

        if not duplicated:
            self.students.append(student)
            student.enrolled_courses.append(self.course_ID)
        else:
            print(f"The student {student.name} is already enroll in this course.")


    def assign_instructor(self, instructor):
        """asignar un instructor al curso"""

        # Se busca antes si tiene el curso asignado y se borra
        if self.instructor is not None:
            previus_instructor = self.instructor

            if self.course_ID in previus_instructor.courses_taught:
                previus_instructor.courses_taught.remove(self.course_ID)


        self.instructor = instructor

        if self.course_ID not in instructor.courses_taught:
            instructor.courses_taught.append(self.course_ID)



    def list_students(self):
        """ retornar una lista de nombres de estudiantes inscritos en el curso """
        return list(
            map(
                lambda x: x.name,
                self.students
            )
        )


    def __repr__(self):
        return f"Instructor: {self.instructor} | Students: {self.students}"




# Example usage

# Create students
student1 = Student("Alice", 20, "S001")
student2 = Student("Bob", 21, "S002")
student3 = Student("Charlie", 22, "S003")

# Create instructors
instructor1 = Instructor("Dr. Smith", 40, "T001")
instructor2 = Instructor("Prof. Johnson", 45, "T002")

# Create courses
course1 = Course("Math 101", "M101")
course2 = Course("Physics 101", "P101")
course3 = Course("Literature 101", "L101")




# Enroll students in courses
course1.enroll(student1)  # Alice enrolls in Math 101
course1.enroll(student2)  # Bob enrolls in Math 101
course1.enroll(student3)  # Charlie enrolls in Math 101

course2.enroll(student1)  # Alice also enrolls in Physics 101
course2.enroll(student2)  # Bob also enrolls in Physics 101
course3.enroll(student3)  # Charlie enrolls in Literature 101



# Assign instructors to courses
course1.assign_instructor(instructor1)  # Dr. Smith teaches Math 101
course2.assign_instructor(instructor1)  # Dr. Smith also teaches Physics 101
course3.assign_instructor(instructor2)  # Prof. Johnson teaches Literature 101





# Attempt to enroll a student twice in the same course
course1.enroll(student1)  # Student is already enrolled, do not enroll again



# List all students of each course

print(course1.list_students())  # ['Alice', 'Bob', 'Charlie']
print(course2.list_students())  # ['Alice', 'Bob']
print(course3.list_students())  # ['Charlie']

# List all courses taught by instructors
print(instructor1.list_courses())  # ['M101', 'P101']
print(instructor2.list_courses())  # ['Literature 101']

# List all courses a student is enrolled in
print(student1.list_courses())  # ['M101', 'P101']
print(student2.list_courses())  # ['M101', 'P101']
print(student3.list_courses())  # ['M101', 'L101']