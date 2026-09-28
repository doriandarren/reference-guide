grades = [('Bob', 8.0), ('Alice', 7.5), ('Bob', 9.0), ('Charlie', 5.5)]

student_dic = {}

for name, grade in grades:

    if name not in student_dic:
        student_dic[name] = [grade]
    else:
        student_dic[name].append(grade)

print(student_dic)





# grades = [("Alice", 8.5), ("Bob", 7.8), ("Alice", 9.0),
#           ("Bob", 8.5), ("Charlie", 9.2), ("Alice", 9.5)]

# grade_book = {}
# for name, grade in grades:
#     grade_book[name] = grade_book.get(name, []) + [grade]

# print(grade_book)