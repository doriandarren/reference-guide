network = { 
    "Alice": {
        "Bob", 
        "Charlie", 
        "Diana"
    }, 
    "Bob": {
        "Alice", 
        "Diana", 
        "Eve"
    }, 
    "Charlie": {
        "Alice", 
        "Frank", 
        "Grace"
    }, 
    "Diana": {
        "Alice", 
        "Bob", 
        "Helen"
    }, 
    "Eve": {
        "Bob", 
        "Ivan", 
        "Jack"
    }, 
    "Frank": {
        "Charlie", 
        "Grace", 
        "Helen"
    }, 
    "Grace": {
        "Charlie", 
        "Frank", 
        "Ivan"
    }, 
    "Helen": {
        "Diana", 
        "Frank", 
        "Karl"
    }, 
    "Ivan": {
        "Eve", 
        "Grace", 
        "Laura"
    }, 
    "Jack": {
        "Eve", 
        "Karl"
    }, 
    "Karl": {
        "Helen", 
        "Jack", 
        "Laura"
    }, 
    "Laura": {
        "Ivan", 
        "Karl"
    }
}


# Output should be ['Eve', 'Frank', 'Grace', 'Helen']

exclude_person = 'Alice'

exclude_st = set(network[exclude_person])
exclude_st.add(exclude_person)

##print(exclude_st)

friends_of_friends_st = set()

for person in network[exclude_person]:

    friend_st = set(network[person])

    friends_of_friends_st.update(friend_st - exclude_st)

print(sorted(friends_of_friends_st))








# network = {
#     "Alice": {"Bob", "Charlie", "Diana"},
#     "Bob": {"Alice", "Diana", "Eve"},
#     "Charlie": {"Alice", "Frank", "Grace"},
#     "Diana": {"Alice", "Bob", "Helen"},
#     "Eve": {"Bob", "Ivan", "Jack"},
#     "Frank": {"Charlie", "Grace", "Helen"},
#     "Grace": {"Charlie", "Frank", "Ivan"},
#     "Helen": {"Diana", "Frank", "Karl"},
#     "Ivan": {"Eve", "Grace", "Laura"},
#     "Jack": {"Eve", "Karl"},
#     "Karl": {"Helen", "Jack", "Laura"},
#     "Laura": {"Ivan", "Karl"},
# }

# direct = network["Alice"]

# fof = set()
# for friend in direct:
#     for f2 in network[friend]:
#         if f2 != "Alice" and f2 not in direct:
#             fof.add(f2)

# print(fof)