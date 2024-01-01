# Read data from the file into a list
with open("Day3Example.txt", "r") as file:
    data_list = file.read().split("\n")

for i in data_list:
    part_numbers = i.split(".")
    print(part_numbers)
part_numbers = {}
