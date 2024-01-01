import numpy as np

# Read data from the file into a list
with open("Day3Example.txt", "r") as file:
    data_list = file.read().split("\n")



#print(*data_list,sep='\n')
special_char = []
for line in data_list:
    special_data = line.replace(".", "")
    special_data = ''.join([i for i in special_data if not i.isdigit()])
    #print(special_char)
    special_char.append(special_data)
special_char = [value for value in special_char if value != ""]
#print(special_char)
special_char = list(set(special_char))
special_char = "".join(special_char)
p = ""
for char in special_char:
    if char not in p:
        p = p+char
special_char = p
#print(special_char)

data_array = np.asarray(data_list)
#print(data_array)



def isValidPos(i, j, n, m):
 
    if (i < 0 or j < 0 or i > n - 1 or j > m - 1):
        return 0
    return 1
 
 
# Function that returns all adjacent elements
def getAdjacent(arr, i, j):
 
    # Size of given 2d array
    n = len(arr)
    m = len(arr[0])
 
    # Initialising a vector array
    # where adjacent element will be stored
    v = []
 
    # Checking for all the possible adjacent positions
    if (isValidPos(i - 1, j - 1, n, m)) and arr[i - 1][j - 1] != ".":
        v.append(arr[i - 1][j - 1])
    if (isValidPos(i - 1, j, n, m)) and arr[i - 1][j] != ".":
        v.append(arr[i - 1][j])
    if (isValidPos(i - 1, j + 1, n, m)) and arr[i - 1][j + 1] != ".":
        v.append(arr[i - 1][j + 1])
    if (isValidPos(i, j - 1, n, m)) and arr[i][j - 1] != ".":
        v.append(arr[i][j - 1])
    if (isValidPos(i, j + 1, n, m)) and arr[i][j + 1] != ".":
        v.append(arr[i][j + 1])
    if (isValidPos(i + 1, j - 1, n, m)) and arr[i + 1][j - 1] != ".":
        v.append(arr[i + 1][j - 1])
    if (isValidPos(i + 1, j, n, m)) and arr[i + 1][j] != ".":
        v.append(arr[i + 1][j])
    if (isValidPos(i + 1, j + 1, n, m)) and arr[i + 1][j + 1] != ".":
        v.append(arr[i + 1][j + 1])
 
    # Returning the vector
    return v
 
 
# Driver Code
if __name__ == "__main__":
    
    adjacent_nums = []
    cords = []
    for row in range(0, len(data_array)):
        #print(type)
        for column in range(0, len(data_array[row])):
            if data_array[row][column] in special_char:
                cords.append((row,column))
    #print(cords)

    # Function call
    for xy in cords:
        x, y = xy
        ans = (getAdjacent(data_array, x, y))
        adjacent_nums.append(ans)
        #print(type(ans))
    #print(adjacent_nums)
    for row in data_list:
        searching = True
        while searching == True:
            
        
