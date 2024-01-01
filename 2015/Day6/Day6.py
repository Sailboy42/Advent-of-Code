import re
import numpy as np

# Read data from the file into a list
with open("Day6.txt", "r") as file:
    data_list = file.read().split("\n")

#Part 1
grid = np.full((1000, 1000), False, dtype=bool)

for direction in data_list:
    cords = [int(coord) for coord in re.findall(r'\d+', direction)]
    
    if "turn on" in direction:
        grid[cords[0]:cords[2]+1, cords[1]:cords[3]+1] = True
    elif "turn off" in direction:
        grid[cords[0]:cords[2]+1, cords[1]:cords[3]+1] = False
    elif "toggle" in direction:
        grid[cords[0]:cords[2]+1, cords[1]:cords[3]+1] = np.logical_not(grid[cords[0]:cords[2]+1, cords[1]:cords[3]+1])

on_count = np.count_nonzero(grid)

print(on_count)

#Part 2
grid = np.full((1000, 1000), 0, dtype=int)

for direction in data_list:
    cords = [int(coord) for coord in re.findall(r'\d+', direction)]
    
    if "turn on" in direction:
        grid[cords[0]:cords[2]+1, cords[1]:cords[3]+1] += 1
    elif "turn off" in direction:
        grid[cords[0]:cords[2]+1, cords[1]:cords[3]+1] = np.maximum(0, grid[cords[0]:cords[2]+1, cords[1]:cords[3]+1] - 1)
    elif "toggle" in direction:
        grid[cords[0]:cords[2]+1, cords[1]:cords[3]+1] += 2

brightness = np.sum(grid)

print(brightness)
