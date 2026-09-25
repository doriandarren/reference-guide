date_list = ['2024-02-29']

for d in date_list:

    is_valid = True

    year, month, day = d.split("-")

    year = int(year)
    month = int(month)
    day = int(day)

    if year < 1900 or year > 2100:
        is_valid = False

    if month < 1 or month > 12:
        is_valid = False

    
    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_days = 31

    elif month in [4, 6, 9, 11]:
        max_days = 30

    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            max_days = 29
        else:
            max_days = 28

    else:
        max_days = 0

    if day < 1 or day > max_days:
        is_valid = False

    if is_valid:
        print(f"{d}: Valid")
    else:
        print(f"{d}: Invalid")
