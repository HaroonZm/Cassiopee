number_of_elements = int(input())

jump_distances_per_position = []

for current_index in range(number_of_elements):
    jump_distance = int(input()) // 10
    jump_distances_per_position.append(jump_distance)

maximum_reachable_index_forward = 0

for current_index in range(number_of_elements):
    if maximum_reachable_index_forward >= current_index:
        maximum_reachable_index_forward = max(
            maximum_reachable_index_forward,
            current_index + jump_distances_per_position[current_index]
        )

if maximum_reachable_index_forward >= number_of_elements - 1:
    maximum_reachable_index_backward = 0

    for offset in range(number_of_elements):
        current_index = number_of_elements - 1 - offset

        if maximum_reachable_index_backward >= offset:
            maximum_reachable_index_backward = max(
                maximum_reachable_index_backward,
                offset + jump_distances_per_position[current_index]
            )

    if maximum_reachable_index_backward >= number_of_elements - 1:
        print("yes")
    else:
        print("no")

else:
    print("no")