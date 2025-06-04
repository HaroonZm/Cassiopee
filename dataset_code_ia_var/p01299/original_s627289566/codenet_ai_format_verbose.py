from collections import deque
import sys

input_stream_readline = sys.stdin.readline
output_stream_write = sys.stdout.write

def process_test_case():
    number_of_circles = int(input_stream_readline())
    if number_of_circles == 0:
        return False

    start_point_x, start_point_y, target_point_x, target_point_y = map(int, input_stream_readline().split())
    circle_parameters_list = []
    directed_graph = [[] for _ in range(number_of_circles + 2)]
    number_of_valid_circles = 0

    for current_circle_index in range(number_of_circles):
        circle_center_x, circle_center_y, circle_radius = map(int, input_stream_readline().split())

        start_inside_current_circle = ((start_point_x - circle_center_x) ** 2 + (start_point_y - circle_center_y) ** 2 <= circle_radius ** 2)
        target_inside_current_circle = ((target_point_x - circle_center_x) ** 2 + (target_point_y - circle_center_y) ** 2 <= circle_radius ** 2)

        if (start_inside_current_circle and target_inside_current_circle) or (not start_inside_current_circle and not target_inside_current_circle):
            continue

        for existing_circle_index in range(number_of_valid_circles):
            existing_circle_x, existing_circle_y, existing_circle_radius = circle_parameters_list[existing_circle_index]
            centers_distance_squared = (circle_center_x - existing_circle_x) ** 2 + (circle_center_y - existing_circle_y) ** 2
            radii_difference_squared = (circle_radius - existing_circle_radius) ** 2

            if centers_distance_squared < radii_difference_squared:
                if circle_radius < existing_circle_radius:
                    directed_graph[number_of_valid_circles].append(existing_circle_index)
                elif circle_radius > existing_circle_radius:
                    directed_graph[existing_circle_index].append(number_of_valid_circles)

        if target_inside_current_circle:
            directed_graph[number_of_circles].append(number_of_valid_circles)
        if start_inside_current_circle:
            directed_graph[number_of_circles + 1].append(number_of_valid_circles)

        circle_parameters_list.append((circle_center_x, circle_center_y, circle_radius))
        number_of_valid_circles += 1

    def compute_longest_path_from_source(source_node_index):
        processing_queue = deque([source_node_index])
        node_visited_flag = [0] * (number_of_circles + 2)
        node_incoming_degree = [0] * (number_of_circles + 2)
        node_visited_flag[source_node_index] = 1

        while processing_queue:
            current_node_index = processing_queue.popleft()
            for adjacent_node_index in directed_graph[current_node_index]:
                node_incoming_degree[adjacent_node_index] += 1
                if node_visited_flag[adjacent_node_index]:
                    continue
                node_visited_flag[adjacent_node_index] = 1
                processing_queue.append(adjacent_node_index)

        processing_queue = deque([source_node_index])
        node_longest_distance = [0] * (number_of_circles + 2)

        while processing_queue:
            current_node_index = processing_queue.popleft()
            updated_distance = node_longest_distance[current_node_index] + 1
            for adjacent_node_index in directed_graph[current_node_index]:
                node_incoming_degree[adjacent_node_index] -= 1
                node_longest_distance[adjacent_node_index] = max(node_longest_distance[adjacent_node_index], updated_distance)
                if node_incoming_degree[adjacent_node_index] == 0:
                    processing_queue.append(adjacent_node_index)

        return node_longest_distance

    longest_distances_from_target = compute_longest_path_from_source(number_of_circles)
    longest_distances_from_start = compute_longest_path_from_source(number_of_circles + 1)
    max_result_path_length = max(max(longest_distances_from_target), max(longest_distances_from_start))

    for source_circle_index in range(number_of_valid_circles):
        if longest_distances_from_target[source_circle_index] == 0:
            continue
        source_circle_x, source_circle_y, source_circle_radius = circle_parameters_list[source_circle_index]
        for target_circle_index in range(number_of_valid_circles):
            if longest_distances_from_start[target_circle_index] == 0:
                continue
            target_circle_x, target_circle_y, target_circle_radius = circle_parameters_list[target_circle_index]
            center_to_center_squared_distance = (source_circle_x - target_circle_x) ** 2 + (source_circle_y - target_circle_y) ** 2
            sum_of_radii_squared = (source_circle_radius + target_circle_radius) ** 2
            if center_to_center_squared_distance > sum_of_radii_squared:
                candidate_path_length = longest_distances_from_target[source_circle_index] + longest_distances_from_start[target_circle_index]
                max_result_path_length = max(max_result_path_length, candidate_path_length)

    output_stream_write("%d\n" % max_result_path_length)
    return True

while process_test_case():
    pass