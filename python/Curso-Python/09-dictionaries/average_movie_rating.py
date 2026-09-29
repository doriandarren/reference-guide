ratings = [
    ("The Godfather", 9.2),
    ("Pulp Fiction", 8.9),
    ("The Lord of the Rings: The Return of the King", 8.8),
    ("The Godfather", 9.5),
    ("Pulp Fiction", 8.5),
    ("The Godfather", 9.1),
    ("The Lord of the Rings: The Return of the King", 9.3),
    ("Pulp Fiction", 9.7),
    ("The Lord of the Rings: The Return of the King", 9.99999999)
]


dic = {}
ordered = {}


# for name, value in ratings:
#     if name not in dic:
#         dic[name] = []
#     dic[name].append(value)


for name, value in ratings:
    dic[name] = dic.get(name, []) + [value]



for movie in dic:
    average = round(sum(dic[movie]) / len(dic[movie]), 2)
    #print(average)
    dic[movie] = average


while dic:
    movie = max(dic, key=dic.get)
    ordered[movie] = dic.pop(movie)

print(ordered)



# {'The Lord of the Rings: The Return of the King': 9.37, 'The Godfather': 9.27, 'Pulp Fiction': 9.03}
