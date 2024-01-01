import time

start = time.time()
# Read data from the file into a list
with open("Day5.txt", "r") as file:
    data_list = file.read().split("\n")


# Part 1
def silly_naughty_nice_checker(data):
    nice_string_counter = 0
    for string in data:
        vowels = ["a", "e", "i", "o", "u"]
        vowel_counter = 0
        naughty_sub_strings = ["ab", "cd", "pq", "xy"]
        naughty_checker = False
        pos_double = ["0", "1"]
        double_check = False
        string_list = list(string)
        for i in string_list:
            pos_double[0] = pos_double[1]
            pos_double[1] = i
            if "".join(pos_double) in naughty_sub_strings:
                # print(pos_double)
                naughty_checker = True
                break
            if i in vowels:
                vowel_counter += 1
            if pos_double[0] == pos_double[1]:
                double_check = True
            # print(pos_double)
        if vowel_counter >= 3 and double_check and not naughty_checker:
            nice_string_counter += 1
            # print(string)

    return nice_string_counter


# Part 2
def improved_naughty_nice_checker(data):
    nice_string_counter = 0
    for string in data:
        pairs = {}
        current_triple = ["0", "1", "2"]
        triple_check = False
        for i in string:
            current_triple[0] = current_triple[1]
            current_triple[1] = current_triple[2]
            current_triple[2] = i
            pair = "".join(current_triple[1:])
            pairs[pair] = pairs.get(pair, 0) + 1
            if current_triple[0] == current_triple[2]:
                triple_check = True
                # print(current_triple)
            if (
                current_triple[0] == current_triple[1]
                and current_triple[1] == current_triple[2]
            ):
                pair = "".join(current_triple[:2])
                pairs[pair] = -1
        # print(pairs)

        if triple_check and any(value >= 2 for value in pairs.values()):
            nice_string_counter += 1
        # print(string)

    return nice_string_counter


def silly_naughty_nice_checker_ChatGPT(data):
    nice_string_counter = 0

    for string in data:
        vowels = {"a", "e", "i", "o", "u"}
        naughty_sub_strings = {"ab", "cd", "pq", "xy"}

        vowel_counter = sum(1 for char in string if char in vowels)

        double_check = any(string[i] == string[i + 1] for i in range(len(string) - 1))

        naughty_checker = any(substring in string for substring in naughty_sub_strings)

        if vowel_counter >= 3 and double_check and not naughty_checker:
            nice_string_counter += 1
            # print(string)

    return nice_string_counter


def improved_naughty_nice_checker_ChatGPT(data):
    nice_string_counter = 0

    for string in data:
        pairs = {}
        triple_check = False

        for i in range(len(string) - 1):
            pair = string[i : i + 2]
            triple_check = triple_check or (
                i < len(string) - 2 and string[i] == string[i + 2]
            )

            pairs[pair] = pairs.get(pair, 0) + 1

            if i < len(string) - 2 and string[i] == string[i + 1] == string[i + 2]:
                pairs[pair] -= 1

        if triple_check and any(value >= 2 for value in pairs.values()):
            nice_string_counter += 1

    return nice_string_counter


print(silly_naughty_nice_checker(data_list))
print(improved_naughty_nice_checker(data_list))
end = time.time()
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")
