def read_input_as_int_list():
    return list(map(int, input().split()))

number_of_elements, _ = read_input_as_int_list()
initial_sequence = read_input_as_int_list()

if number_of_elements == 1:
    print(*initial_sequence)
    exit()

left_neighbor = [0] * (number_of_elements + 1)
right_neighbor = [0] * (number_of_elements + 1)

for index in range(number_of_elements - 1):
    current_element = initial_sequence[index]
    next_element = initial_sequence[index + 1]
    right_neighbor[current_element] = next_element
    left_neighbor[next_element] = current_element

current_leftmost = initial_sequence[0]
current_rightmost = initial_sequence[-1]

for query_element in read_input_as_int_list():
    if query_element == current_rightmost:
        left_of_query = left_neighbor[query_element]

        right_neighbor[left_of_query] = 0
        left_neighbor[query_element] = 0
        right_neighbor[query_element] = current_leftmost
        left_neighbor[current_leftmost] = query_element

        current_leftmost = query_element
        current_rightmost = left_of_query

    elif query_element == current_leftmost:
        right_of_query = right_neighbor[query_element]

        left_neighbor[right_of_query] = 0
        right_neighbor[query_element] = 0
        left_neighbor[query_element] = current_rightmost
        right_neighbor[current_rightmost] = query_element

        current_leftmost = right_of_query
        current_rightmost = query_element

    else:
        left_of_query = left_neighbor[query_element]
        right_of_query = right_neighbor[query_element]

        left_neighbor[query_element] = current_rightmost
        right_neighbor[query_element] = current_leftmost

        right_neighbor[left_of_query] = 0
        left_neighbor[right_of_query] = 0

        left_neighbor[current_leftmost] = query_element
        right_neighbor[current_rightmost] = query_element

        current_rightmost = left_of_query
        current_leftmost = right_of_query

final_sequence = []
current_element = current_leftmost
while current_element != 0:
    final_sequence.append(current_element)
    current_element = right_neighbor[current_element]

print(*final_sequence)