from collections import deque

number_of_elements, number_of_ranges = map(int, input().split())
values = list(map(int, input().split()))

ranges_for_position = [[] for _ in range(number_of_elements)]

for _ in range(number_of_ranges):
    left_index, right_index = map(int, input().split())
    ranges_for_position[left_index - 1].append(right_index)

segment_tree_size = 2 ** (number_of_elements).bit_length()
infinity = 2 ** 31 - 1
segment_tree_data = [infinity] * (2 * segment_tree_size)

def update_segment_tree(position, value):
    position += segment_tree_size - 1
    segment_tree_data[position] = value
    while position > 0:
        position = (position - 1) // 2
        segment_tree_data[position] = max(segment_tree_data[2 * position + 1], segment_tree_data[2 * position + 2])

def query_segment_tree(left_bound, right_bound):
    left = left_bound + segment_tree_size
    right = right_bound + segment_tree_size
    maximum_value = -infinity
    while left < right:
        if right & 1:
            right -= 1
            maximum_value = max(maximum_value, segment_tree_data[right - 1])
        if left & 1:
            maximum_value = max(maximum_value, segment_tree_data[left - 1])
            left += 1
        left >>= 1
        right >>= 1
    return maximum_value

update_segment_tree(0, 0)

active_ranges = deque()

for current_index in range(number_of_elements):
    while active_ranges and active_ranges[0][1] <= current_index:
        active_ranges.popleft()

    next_range_end = (active_ranges[0][0] if active_ranges else current_index) + 1
    max_value_up_to_next = query_segment_tree(0, next_range_end) + values[current_index]
    update_segment_tree(current_index + 1, max_value_up_to_next)

    for range_end in ranges_for_position[current_index]:
        active_ranges.append((current_index, range_end))

final_result = query_segment_tree(0, number_of_elements + 1)
print(final_result)