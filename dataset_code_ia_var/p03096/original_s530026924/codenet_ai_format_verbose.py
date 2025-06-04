number_of_elements = int(input())

input_sequence = [int(input()) for element_index in range(number_of_elements)]

previous_occurrence_indices = [-1] * number_of_elements

last_seen_index_for_value = dict()

for current_index, current_value in enumerate(input_sequence):
    if current_value in last_seen_index_for_value:
        previous_occurrence_indices[current_index] = last_seen_index_for_value[current_value]
        last_seen_index_for_value[current_value] = current_index
    else:
        last_seen_index_for_value[current_value] = current_index

number_of_ways_to_reach = [1] * number_of_elements

number_of_ways_to_reach[0] = 1

modulo_value = 10 ** 9 + 7

for index in range(1, number_of_elements):
    if previous_occurrence_indices[index] == -1:
        number_of_ways_to_reach[index] = number_of_ways_to_reach[index - 1]
    elif previous_occurrence_indices[index] == index - 1:
        number_of_ways_to_reach[index] = number_of_ways_to_reach[index - 1]
    else:
        number_of_ways_to_reach[index] = (number_of_ways_to_reach[index - 1] + number_of_ways_to_reach[previous_occurrence_indices[index]]) % modulo_value

print(number_of_ways_to_reach[number_of_elements - 1])