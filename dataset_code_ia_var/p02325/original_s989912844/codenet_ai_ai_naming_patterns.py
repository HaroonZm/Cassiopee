import math

point_list = []
input_line = input()
point_count = int(input_line)
for point_index in range(point_count):
    input_line = input()
    x_coord, y_coord = map(int, input_line.split())
    point_list.append([x_coord, y_coord])

def compute_distance(index_a, index_b):
    x_a, y_a = point_list[index_a]
    x_b, y_b = point_list[index_b]
    return math.sqrt((x_a - x_b) ** 2 + (y_a - y_b) ** 2)

def solve_bitonic_tsp():
    distance_table = [[0 for _ in range(point_count)] for _ in range(point_count)]
    for end_index in range(1, point_count):
        distance_table[0][end_index] = distance_table[0][end_index - 1] + compute_distance(end_index - 1, end_index)
    for left_index in range(1, point_count):
        for right_index in range(left_index, point_count):
            if left_index == right_index - 1 or left_index == right_index:
                min_value = float('inf')
                for split_index in range(left_index):
                    min_value = min(min_value, distance_table[split_index][left_index] + compute_distance(right_index, split_index))
                distance_table[left_index][right_index] = min_value
            else:
                distance_table[left_index][right_index] = distance_table[left_index][right_index - 1] + compute_distance(right_index - 1, right_index)
    return distance_table[point_count - 1][point_count - 1]

print(solve_bitonic_tsp())