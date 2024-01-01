# Read data from the file into a list
with open("Day3.txt", "r") as file:
    route = file.read()

route_example = "^>v<"

houses = {(0, 0): 1}
cords = [0, 0]
moves = {"^": [1, 0], "v": [-1, 0], ">": [0, 1], "<": [0, -1]}
for direction in route:
    cords = [sum(i) for i in zip(cords, moves[direction])]
    houses[tuple(cords)] = houses.get(tuple(cords), 0) + 1

print(len(houses))


# Part 2
houses_2 = {(0, 0): 1}
cords_santa = [0, 0]
moves = {"^": [1, 0], "v": [-1, 0], ">": [0, 1], "<": [0, -1]}
for direction in route[::2]:
    #print(direction)
    cords_santa = [sum(i) for i in zip(cords_santa, moves[direction])]
    houses_2[tuple(cords_santa)] = houses_2.get(tuple(cords_santa), 0) + 1
#print(houses_2)
#print(len(houses_2))

cords_robot = [0, 0]
moves = {"^": [1, 0], "v": [-1, 0], ">": [0, 1], "<": [0, -1]}
for direction in route[1::2]:
    #print(direction)
    cords_robot = [sum(i) for i in zip(cords_robot, moves[direction])]
    houses_2[tuple(cords_robot)] = houses_2.get(tuple(cords_robot), 0) + 1
#print(houses_2)
print(len(houses_2))
