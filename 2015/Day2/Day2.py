# Read data from the file into a list
with open("Day2.txt", "r") as file:
    data_list = file.read().split("\n")

total_footage = 0
total_ribbon = 0

for i in data_list:
    dimensions = i.split('x')
    dimensions = list(map(int, dimensions))
    l = dimensions[0]
    w = dimensions[1]
    h = dimensions[2]
    sides = [l*w, w*h, h*l]
    dimensions.sort()
    total_footage += min(sides) + sum([area * 2 for area in sides])

    perimeter_min = (2 * dimensions[0]) + (2 * dimensions[1])
    volume = 1
    for x in dimensions:
        volume *= x

    total_ribbon += (perimeter_min + volume)


print(total_footage)
print(total_ribbon)
