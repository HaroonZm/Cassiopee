from collections import Counter

number_of_elements, _ = map(int, raw_input().split())

input_sequence = map(int, raw_input().split())

max_values_to_right = [None for index in range(number_of_elements)]

current_maximum = 0

for index in range(number_of_elements - 1, -1, -1):
    current_maximum = max(input_sequence[index], current_maximum)
    max_values_to_right[index] = current_maximum

differences_to_next_max = []

for index in range(number_of_elements - 1):
    difference = max_values_to_right[index + 1] - input_sequence[index]
    differences_to_next_max.append(difference)

difference_counter = Counter(differences_to_next_max)

most_frequent_difference = max(differences_to_next_max)

print difference_counter[most_frequent_difference]