# Read data from the file into a list
with open("Day2.txt", "r") as file:
    data_list = file.read().split("\n")

colors_max = {"red": 12, "green": 13, "blue": 14}

#for game in data_list:
#    print(game)
for game in range(0, len(data_list)):
    data_list[game] = data_list[game][data_list[game].index(":") + 1:]
    #print(data_list[game])
    #data_list[game] = data_list[game].replace(";", ",")
    #print(data_list[game])
    data_list[game] = data_list[game].split(";")
    for set in range(0, len(data_list[game])):
        data_list[game][set] = data_list[game][set].split(", ")

powers = []
#print(data_list)
possible_game_counter = 0
possible_index_sum = 0
for game in data_list:
    colors_count_game = {"red": 0, "green": 0, "blue": 0}
    #print(len(game))
    possible = True
    for set in game:
        color_count_set = {"red": 0, "green": 0, "blue": 0}
        #print(set)
        #possible = True
        for color in colors_max:
            for cubes in set:
                #print(cubes)
                if color in cubes:
                    # print(f"Game: {data_list.index(game) + 1}, Set Color: {cubes}")
                    cube_amount = [int(i) for i in cubes.split() if i.isdigit()]
                    #print(sum(cube_amount))
                    color_count_set[color] += sum(cube_amount)
                    if sum(cube_amount) > colors_max[color]:
                        possible = False

        for color in color_count_set:
            if colors_count_game[color] < color_count_set[color]:
                colors_count_game[color] = color_count_set[color]

    #print(colors_count_game)
    power = 1
    for color in colors_count_game:
        power = power*colors_count_game[color]
    #print(power)
    powers.append(power)
        

        #print(colors_min)
        #for color in colors_min:
         #   if colors_min[color] > colors_max[color]:
          #      possible = False
           #     break
    if possible == True:
        possible_game_counter += 1
        possible_index_sum += data_list.index(game) + 1
sum_power = sum(powers)
print(possible_index_sum)
print(possible_game_counter)
print(sum_power)
