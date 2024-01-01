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
