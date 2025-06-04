from heapq import heappush, heappop

number_of_inputs = input()

smallest_negatives_heap = [-10000] * 4

for input_index in range(number_of_inputs):

    current_number = input()

    heappush(smallest_negatives_heap, -current_number)

    heappop(smallest_negatives_heap)

stringified_positive_numbers = [str(-number) for number in smallest_negatives_heap]

concatenated_number_combinations = []

for first_index in range(3):

    for second_index in range(first_index + 1, 4):

        concatenated_number_combinations.append(int(stringified_positive_numbers[first_index] + stringified_positive_numbers[second_index]))

        concatenated_number_combinations.append(int(stringified_positive_numbers[second_index] + stringified_positive_numbers[first_index]))

concatenated_number_combinations.sort()

print concatenated_number_combinations[2]