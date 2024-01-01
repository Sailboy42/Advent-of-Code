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
