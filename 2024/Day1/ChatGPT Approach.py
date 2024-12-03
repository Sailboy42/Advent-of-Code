from collections import Counter

def calculate_total_distance(left_list, right_list):
    # Sort both lists
    sorted_left = sorted(left_list)
    sorted_right = sorted(right_list)
    # Pair and calculate distance
    return sum(abs(l - r) for l, r in zip(sorted_left, sorted_right))

def calculate_similarity_score(left_list, right_list):
    # Count occurrences in the right list
    right_counter = Counter(right_list)
    # Compute weighted sum
    return sum(num * right_counter[num] for num in left_list)

# Main script
with open('Day1.txt', 'r') as file:
    left_list = []
    right_list = []
    for line in file:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

# Calculate Part One and Part Two
total_distance = calculate_total_distance(left_list, right_list)
similarity_score = calculate_similarity_score(left_list, right_list)

print("Total Distance (Part One):", total_distance)
print("Similarity Score (Part Two):", similarity_score)
