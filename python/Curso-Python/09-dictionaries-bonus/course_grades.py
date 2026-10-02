grades = [("Math", "John", 88), ("Math", "Jane", 92), ("Biology", "John", 75)]

dic = {}


for course, student, grades in grades:

    if course not in dic.keys():
        dic_student = {}
        dic_student[student] = grades
        dic[course] = dic_student
    
    else:
        dic_student = {}
        dic_student[student] = grades
        dic[course].update(dic_student)


print(dic)





# grades = [
#     ("Calculus", "Alice", 85),
#     ("Physics", "Bob", 78),
#     ("Calculus", "Bob", 90),
#     ("Physics", "Alice", 85),
#     ("Physics", "Charlie", 92)
# ]

# course_grades = {}
# for course, student, grade in grades:
#     if course not in course_grades:
#         course_grades[course] = {}
#     course_grades[course][student] = grade

# print(course_grades)