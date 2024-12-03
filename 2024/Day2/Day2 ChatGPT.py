def is_safe(sequence):
    """
    Check if a sequence satisfies the safety rules: 
    either strictly increasing or decreasing with differences between 1 and 3.
    """
    increasing = all(1 <= sequence[i + 1] - sequence[i] <= 3 for i in range(len(sequence) - 1))
    decreasing = all(1 <= sequence[i] - sequence[i + 1] <= 3 for i in range(len(sequence) - 1))
    return increasing or decreasing

def can_be_safe_with_dampener(sequence):
    """
    Check if removing one element makes the sequence safe.
    """
    for i in range(len(sequence)):
        temp_sequence = sequence[:]
        temp_sequence.pop(i)
        if is_safe(temp_sequence):
            return True
    return False

# Read data from the file
with open("Day2.txt", "r") as file:
    data_list = [list(map(int, line.split())) for line in file.read().splitlines()]

safe_counter = 0

# Analyze each report
for report in data_list:
    if is_safe(report) or can_be_safe_with_dampener(report):
        print(report)
        safe_counter += 1

print(safe_counter)
