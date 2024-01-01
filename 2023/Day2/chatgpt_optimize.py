def read_data(file_path):
    with open(file_path, "r") as file:
        data_list = [line.strip() for line in file]

    return [game.split(": ")[1].split("; ") for game in data_list]


def main():
    data_list = read_data("Day2.txt")

    colors_max = {"red": 12, "green": 13, "blue": 14}

    powers = []
    possible_game_counter = 0
    possible_index_sum = 0

    for game_index, game in enumerate(data_list, start=1):
        colors_count_game = {"red": 0, "green": 0, "blue": 0}
        possible = True

        for set in game:
            color_count_set = {"red": 0, "green": 0, "blue": 0}

            for color in colors_max:
                for cubes in set.split(", "):
                    if color in cubes:
                        cube_amount = [int(i) for i in cubes.split() if i.isdigit()]
                        color_count_set[color] += sum(cube_amount)
                        if sum(cube_amount) > colors_max[color]:
                            possible = False

            for color in color_count_set:
                if colors_count_game[color] < color_count_set[color]:
                    colors_count_game[color] = color_count_set[color]

        power = 1
        for color in colors_count_game:
            power *= colors_count_game[color]

        powers.append(power)

        if possible:
            possible_game_counter += 1
            possible_index_sum += game_index

    sum_power = sum(powers)
    print(f"Possible Index Sum: {possible_index_sum}")
    print(f"Possible Game Counter: {possible_game_counter}")
    print(f"Sum Power: {sum_power}")


if __name__ == "__main__":
    main()
