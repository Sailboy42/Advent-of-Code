# Read data from the file into a list
with open("Day2.txt", "r") as file:
    data_list = file.read().split("\n")

def str_to_int(list):
    new_list = []
    for i in range(len(list)):
    #    #print(data_list[i][b])
        new_list.append(int(list[i]))
    return new_list

def is_safe(sequence):
    '''
    '''
    visited_values = []
    order = None
    for i in range(len(sequence)):
        #Convert to integers
        #data_list[i][j] = int(data_list[i][j])

        #Check for duplicates
        if sequence[i] in visited_values:           
            return False
        #First value
        if visited_values == []:
            #print(j)
            visited_values.append(sequence[i])
            continue
        #Ascending order
        if sequence[i] > visited_values[-1]:
            if order == None:
                order = 'asc'
            if order == 'desc':               
                return False
            #Within 3
            if sequence[i] - 3 > visited_values[-1]:                
                return False

        #Descending order
        if sequence[i] < visited_values[-1]:
            if order == None:
                order = 'desc'
            if order == 'asc':
                return False
            #Within 3
            if visited_values[-1] > sequence[i] + 3:
                return False

        #Add to visited values
        visited_values.append(sequence[i])
    return True

def safe_excepetion(sequence):
    '''
    '''
    #print(sequence)
    for k in range(len(sequence)):
        temp = sequence[:]
        #print(f"Index k: {k}, Temp before pop: {temp}")
        # Remove value
        val = temp.pop(k)
        #print(f"Value removed: {val}, Temp after pop: {temp}")
        # Check if the list is safe
        if is_safe(temp):
            #print('hello')
            return True
    return False

safe_counter_p1 = 0
safe_counter_p2 = 0
for i in range(len(data_list)):
    data_list[i] = data_list[i].split()
    data_list[i] = str_to_int(data_list[i])
    if is_safe(data_list[i]):
        safe_counter_p1 += 1
    elif safe_excepetion(data_list[i]):
        safe_counter_p2 += 1

print(safe_counter_p1)
print(safe_counter_p2) 
print(safe_counter_p1 + safe_counter_p2)