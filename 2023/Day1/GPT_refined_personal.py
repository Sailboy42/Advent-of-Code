# Read data from the file into a list
with open("Day1.txt", "r") as file:
    data_list = file.read().split("\n")

# Part 1: Calculate the sum of calibration values
new_cal = [
    int(d[0] + d[-1]) for line in data_list if (d := "".join(filter(str.isdigit, line)))
]

new_cal_total = sum(new_cal)

# Print the result
print(f"The sum of all calibration values is: {new_cal_total}")

# Part 2
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

def find_first_digit(line):
    for index, char in enumerate(line):
        if char.isdigit():
            return char, index

def find_last_digit(line):
    for index in range(len(line) - 1, -1, -1):
        if line[index].isdigit():
            return line[index], index

def find_first_char(line):
    for digit, char in digit_char.items():
        index = line.find(char)
        if index != -1:
            return str(digit), index
    return None, None

def find_last_char(line):
    last_digit_char = None
    last_index_char = -1
    for digit, char in digit_char.items():
        index = line.rfind(char)
        if index > last_index_char:
            last_index_char = index
            last_digit_char = str(digit)
    return last_digit_char, last_index_char

def extract_cal(line):
    first_digit, first_index = find_first_digit(line)
    last_digit, last_index = find_last_digit(line)
    first_char, _ = find_first_char(line)
    last_char, _ = find_last_char(line)

    first = first_digit if first_index < int(first_char) or first_char is None else first_char
    last = last_digit if last_index > int(last_char) or last_digit is None else last_char

    return int(first + last)


newer_cal = [extract_cal(line) for line in data_list]

print(newer_cal)
print(sum(newer_cal))