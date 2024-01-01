with open("Day1.txt", "r") as file:
    # Read the contents of the file into a variable
    floor_commands = file.read()

    # Print the names
    # print(type(floor_commands))
    # print(floor_commands)

# Part 1
count = 0

for iteration, element in enumerate(floor_commands):
    if element == "(":
        count += 1
    elif element == ")":
        count -= 1

    if count == -1:
        print(iteration + 1)
        # print(count)

    # print(iteration)
    # print(element)

print(count)
