def extract_calibration_value(line):
    digits = ""
    for char in line:
        if char.isdigit():
            digits += char

    try:
        # Extract the first and last appearing digits
        return int(digits[0] + digits[-1])
    except IndexError:
        # Handle the case where the line doesn't contain valid digits
        print(f"Warning: Skipping line '{line.strip()}' due to invalid format")
        return 0  # Return 0 for lines with errors


def calculate_sum_of_calibration_values(file_path):
    total_sum = 0

    # Open the calibration document file
    with open(file_path, "r") as file:
        # Read each line from the file
        for line in file:
            # Remove newline character and extract the calibration value
            calibration_value = extract_calibration_value(line.strip())

            # Add the calibration value to the total sum
            total_sum += calibration_value

    return total_sum


# Replace 'your_calibration_document.txt' with the actual file path
file_path = "Day1.txt"

# Calculate the sum of all calibration values
result = calculate_sum_of_calibration_values(file_path)

# Print the result
print(f"The sum of all calibration values is: {result}")

##Part two

import re

# Define a dictionary to map spelled-out digits to numerical values
digit_mapping = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
                 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0'}

# Function to convert digits and spelled-out numbers
def convert_to_numeric(value):
    # Convert digits and spelled-out numbers to a unified format
    return ''.join(digit_mapping.get(word, word) for word in re.findall(r'\b(?:\w+)\b', value.lower()))


# Read data from the file into a list
with open("Day1.txt", "r") as file:
    data_list = file.read().split("\n")

# Part 2: Calculate the sum of calibration values with spelled-out digits
new_cal = []
for line in data_list:
    # Use the conversion function to handle both digits and spelled-out digits
    mapped_digits = convert_to_numeric(line)

    # Extract all valid numerical sequences (digits and spelled-out numbers)
    numerical_sequences = re.findall(r'\b(?:\d+|\w+)\b', mapped_digits)

    # Convert each sequence to its corresponding integer and sum them up
    sequence_sum = sum(int(sequence) for sequence in numerical_sequences if sequence.isdigit())

    # Append the sum to the list
    new_cal.append(sequence_sum)

# Print the result
print("Actual sums  :", new_cal)