number_of_trampolines = int(input())

jump_distances = [int(input()) for index in range(number_of_trampolines)]

can_reach_end_forward = True
maximum_reachable_index_forward = 0

for current_index in range(number_of_trampolines - 1):

    if current_index > maximum_reachable_index_forward:
        can_reach_end_forward = False
        break

    reachable_index = current_index + jump_distances[current_index] // 10

    if reachable_index >= maximum_reachable_index_forward:
        maximum_reachable_index_forward = reachable_index

if maximum_reachable_index_forward < number_of_trampolines - 1:
    can_reach_end_forward = False

reversed_jump_distances = jump_distances[::-1]

can_reach_end_backward = True
maximum_reachable_index_backward = 0

for current_index in range(number_of_trampolines - 1):

    if current_index > maximum_reachable_index_backward:
        can_reach_end_backward = False
        break

    reachable_index = current_index + reversed_jump_distances[current_index] // 10

    if reachable_index >= maximum_reachable_index_backward:
        maximum_reachable_index_backward = reachable_index

if maximum_reachable_index_backward < number_of_trampolines - 1:
    can_reach_end_backward = False

if can_reach_end_forward and can_reach_end_backward:
    print('yes')
else:
    print('no')