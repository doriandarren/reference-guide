form = "Mg2ON12"

d = {}
elem = ""
num = ""

for c in form:
    if c.isupper():
        if elem != "":
            d[elem] = int(num) if num else 1
        elem = c
        num = ""

    elif c.islower():
        elem += c

    elif c.isdigit():
        num += c


d[elem] = int(num) if num else 1


print(d)