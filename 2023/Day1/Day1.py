"""
Take a txt file of lines of data and concatanate the first and last appearing
digit whether that be in integer or char form
"""

# Import
day_1 = open("Day1.txt", "r")
data = day_1.read()
data_list = data.split("\n")
# print(data_list)
day_1.close()


# Part 1
new_cal = []


def concat(a, b):
    """
    Bring two digits together to form a 2 digit number
    """
    # Convert both the integers to string
    s1 = str(a)
    s2 = str(b)

    # Concatenate both strings
    s = s1 + s2

    # Convert the concatenated string
    # to integer
    c = int(s)

    # return the formed integer
    return c


for i in data_list:
    for d in i:
        if d.isdigit():
            first_digit = d
            break
    for d in reversed(i):
        if d.isdigit():
            last_digit = d
            break
    cal = concat(first_digit, last_digit)
    new_cal.append(cal)

# print(new_cal)
new_cal_total = sum(new_cal)
# print(new_cal_total)


# Part 2
newer_cal = []

digit_char = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

for i in data_list:
    # Find first digit and index
    for d in range(0, len(i)):
        if i[d].isdigit():
            # print(d)
            first_digit_digit = i[d]
            first_index_digit = d
            break

    # Find last digit and index
    for d in range(len(i) - 1, -1, -1):
        if i[d].isdigit():
            # print(d)
            last_digit_digit = i[d]
            last_index_digit = d
            break
    # Find first digit char and index
    first_index_char = -1
    for digit in digit_char.values():
        index = i.find(digit)
        if index != -1:
            # print(index)
            if index < first_index_char or first_index_char == -1:
                first_index_char = index
                first_digit_char = list(digit_char.keys())[
                    list(digit_char.values()).index(digit)
                ]

    # Find last digit char and index
    last_index_char = -1
    for digit in digit_char.values():
        index = i.rfind(digit)
        if index != -1:
            # print(index)
            if index > last_index_char:
                last_index_char = index
                last_digit_char = list(digit_char.keys())[
                    list(digit_char.values()).index(digit)
                ]

    # Determine whether digit or char index is less, thus first
    if first_index_digit < first_index_char or first_index_char == -1:
        first_digit = first_digit_digit
    else:
        first_digit = first_digit_char

    # Determine whether digit or char index is more, thus last
    if last_index_digit > last_index_char:
        last_digit = last_digit_digit
    else:
        last_digit = last_digit_char

    cal = concat(first_digit, last_digit)
    print(cal)
    newer_cal.append(cal)
# print(newer_cal)

print(sum(newer_cal))
