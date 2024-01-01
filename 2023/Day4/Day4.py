# Read data from the file into a list
with open("Day4.txt", "r") as file:
    data_list = file.read().split("\n")

game_points = 0
for game, nums in enumerate(data_list):
    winning_num_counter = 0
    points = 0
    data_list[game] = data_list[game][data_list[game].index(":") + 2:]
    data_list[game] = data_list[game].split(" | ")
    #print(data_list[game])
    for pair, nums in enumerate(data_list[game]):
    #    print(type(set))
        data_list[game][pair] = data_list[game][pair].split(" ")
        #print(data_list[game])
        data_list[game][pair] = list(filter(None, data_list[game][pair]))
    #print(data_list[game])

    winning_nums = data_list[game][0]
    #print(winning_nums)
    my_nums = data_list[game][1]
    for num in my_nums:
        if num in winning_nums and points != 0:
            winning_num_counter +=1
            points = 2*points
        elif num in winning_nums:
            points = 1
            winning_num_counter +=1
        #print(winning_nums_counter)

    game_points += points
    #print(winning_nums_counter)
print(game_points)
