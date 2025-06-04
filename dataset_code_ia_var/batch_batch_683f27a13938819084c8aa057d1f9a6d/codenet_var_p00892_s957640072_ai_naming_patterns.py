import sys
read_input_line = sys.stdin.readline

def compute_section_width(polygon_x_coords, polygon_y_coords, vertical_cut_x):
    vertex_count = len(polygon_x_coords)
    min_intersection_y = float('inf')
    max_intersection_y = -float('inf')
    for vertex_index in range(vertex_count):
        current_x = polygon_x_coords[vertex_index]
        current_y = polygon_y_coords[vertex_index]
        next_x = polygon_x_coords[(vertex_index + 1) % vertex_count]
        next_y = polygon_y_coords[(vertex_index + 1) % vertex_count]
        if (current_x - vertical_cut_x) * (next_x - vertical_cut_x) <= 0 and current_x != next_x:
            intersection_y = current_y + (next_y - current_y) * (vertical_cut_x - current_x) / (next_x - current_x)
            min_intersection_y = min(min_intersection_y, intersection_y)
            max_intersection_y = max(max_intersection_y, intersection_y)
    return max(0, max_intersection_y - min_intersection_y)

while True:
    polygon_one_vertex_count, polygon_two_vertex_count = map(int, read_input_line().split())
    if polygon_one_vertex_count == 0 and polygon_two_vertex_count == 0:
        break
    polygon_one_x_coords = [0] * polygon_one_vertex_count
    polygon_one_y_coords = [0] * polygon_one_vertex_count
    polygon_two_x_coords = [0] * polygon_two_vertex_count
    polygon_two_y_coords = [0] * polygon_two_vertex_count
    for index_one in range(polygon_one_vertex_count):
        polygon_one_x_coords[index_one], polygon_one_y_coords[index_one] = map(int, read_input_line().split())
    for index_two in range(polygon_two_vertex_count):
        polygon_two_x_coords[index_two], polygon_two_y_coords[index_two] = map(int, read_input_line().split())
    polygon_one_min_x = min(polygon_one_x_coords)
    polygon_one_max_x = max(polygon_one_x_coords)
    polygon_two_min_x = min(polygon_two_x_coords)
    polygon_two_max_x = max(polygon_two_x_coords)
    merged_x_coords = polygon_one_x_coords + polygon_two_x_coords
    merged_x_coords.sort()
    computed_area = 0
    for merged_index in range(len(merged_x_coords) - 1):
        split_x_left = merged_x_coords[merged_index]
        split_x_right = merged_x_coords[merged_index + 1]
        split_x_middle = (split_x_left + split_x_right) / 2
        if (
            polygon_one_min_x <= split_x_middle <= polygon_one_max_x and
            polygon_two_min_x <= split_x_middle <= polygon_two_max_x
        ):
            left_area_section = compute_section_width(polygon_one_x_coords, polygon_one_y_coords, split_x_left) * compute_section_width(polygon_two_x_coords, polygon_two_y_coords, split_x_left)
            right_area_section = compute_section_width(polygon_one_x_coords, polygon_one_y_coords, split_x_right) * compute_section_width(polygon_two_x_coords, polygon_two_y_coords, split_x_right)
            middle_area_section = compute_section_width(polygon_one_x_coords, polygon_one_y_coords, split_x_middle) * compute_section_width(polygon_two_x_coords, polygon_two_y_coords, split_x_middle)
            computed_area += (split_x_right - split_x_left) / 6 * (left_area_section + 4 * middle_area_section + right_area_section)
    print(computed_area)