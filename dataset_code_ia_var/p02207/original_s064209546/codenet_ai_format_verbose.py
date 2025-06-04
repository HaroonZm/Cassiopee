import sys

input_stream = sys.stdin.readline

number_of_events = int(input_stream())

event_list = [list(map(int, input_stream().split())) for _ in range(number_of_events)]

number_of_queries = int(input_stream())

query_intervals = [list(map(int, input_stream().split())) for _ in range(number_of_queries)]

all_time_points = []

for event_time, event_value in event_list:
    all_time_points.append(event_time)

for query_left, query_right in query_intervals:
    all_time_points.append(query_left)
    all_time_points.append(query_right)

coordinate_compression_mapping = {time_point: index for index, time_point in enumerate(sorted(set(all_time_points)))}

for event_index in range(number_of_events):
    event_list[event_index][0] = coordinate_compression_mapping[event_list[event_index][0]]

for query_index in range(number_of_queries):
    query_intervals[query_index] = [
        coordinate_compression_mapping[query_intervals[query_index][0]],
        coordinate_compression_mapping[query_intervals[query_index][1]]
    ]


def segment_tree_operation(x, y):
    return x * y

segment_tree_element_count = 1 << (len(coordinate_compression_mapping).bit_length())

segment_tree_array = [1] * (2 * segment_tree_element_count)

for event_time_compressed, event_value in event_list:
    segment_tree_array[event_time_compressed + segment_tree_element_count] = 1 - 0.1 * event_value

for parent_index in range(segment_tree_element_count - 1, 0, -1):
    segment_tree_array[parent_index] = segment_tree_operation(
        segment_tree_array[parent_index * 2],
        segment_tree_array[parent_index * 2 + 1]
    )

def update_segment_tree_value(update_index, new_value, segment_tree_base_index):
    node_index = update_index + segment_tree_base_index
    segment_tree_array[node_index] = new_value
    node_index >>= 1

    while node_index != 0:
        segment_tree_array[node_index] = segment_tree_operation(
            segment_tree_array[node_index * 2],
            segment_tree_array[node_index * 2 + 1]
        )
        node_index >>= 1

def compute_segment_tree_range_product(left_index, right_index):
    left = left_index + segment_tree_element_count
    right = right_index + segment_tree_element_count
    product_result = 1

    while left < right:
        if left & 1:
            product_result *= segment_tree_array[left]
            left += 1

        if right & 1:
            right -= 1
            product_result *= segment_tree_array[right]
        left >>= 1
        right >>= 1

    return product_result

for query_left_compressed, query_right_compressed in query_intervals:
    print(10 ** 9 * compute_segment_tree_range_product(query_left_compressed, query_right_compressed))