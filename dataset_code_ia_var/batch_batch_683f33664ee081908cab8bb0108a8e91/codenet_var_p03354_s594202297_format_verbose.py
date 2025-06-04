import sys

read_input_line = sys.stdin.readline

number_of_elements, number_of_connections = map(int, read_input_line().split())

target_positions = list(map(int, read_input_line().split()))

def find_root(element_index):
    if element_index != disjoint_set_parent[element_index]:
        disjoint_set_parent[element_index] = find_root(disjoint_set_parent[element_index])
    return disjoint_set_parent[element_index]

def check_same_set(first_index, second_index):
    return find_root(first_index) == find_root(second_index)

def union_sets(first_index, second_index):
    root_first = find_root(first_index)
    root_second = find_root(second_index)

    if disjoint_set_rank[root_first] < disjoint_set_rank[root_second]:
        disjoint_set_parent[root_first] = root_second
    else:
        disjoint_set_parent[root_second] = root_first
        if disjoint_set_rank[root_first] == disjoint_set_rank[root_second]:
            disjoint_set_rank[root_first] += 1

disjoint_set_parent = list(range(number_of_elements))
disjoint_set_rank = [0] * number_of_elements

for connection_index in range(number_of_connections):
    first_element, second_element = map(int, read_input_line().split())
    union_sets(first_element - 1, second_element - 1)

elements_in_correct_position = 0

for current_index in range(number_of_elements):
    if check_same_set(target_positions[current_index] - 1, current_index):
        elements_in_correct_position += 1

print(elements_in_correct_position)