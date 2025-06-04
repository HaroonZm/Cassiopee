def get_single_integer_input():
    return int(input())

def get_multiple_integer_input():
    return list(map(int, input().split()))

while True:
    rectangle_width, rectangle_height, number_of_lines = get_multiple_integer_input()
    
    if rectangle_width == 0 and rectangle_height == 0 and number_of_lines == 0:
        break
    
    segment_endpoints = [get_multiple_integer_input() for _ in range(2 * number_of_lines)]
    
    intersection_y_coordinates = [0, rectangle_height]
    
    for segment_index, (segment_x, segment_y) in enumerate(segment_endpoints):
        if segment_x < rectangle_width:
            intersection_with_right = segment_y * rectangle_width / (rectangle_width - segment_x)
            if 0 <= intersection_with_right <= rectangle_height:
                intersection_y_coordinates.append(intersection_with_right)
            intersection_with_left = rectangle_height - (rectangle_height - segment_y) * rectangle_width / (rectangle_width - segment_x)
            if 0 <= intersection_with_left <= rectangle_height:
                intersection_y_coordinates.append(intersection_with_left)
        
        for previous_x, previous_y in segment_endpoints[:segment_index]:
            if segment_x != previous_x:
                intersection_with_previous = previous_y - (previous_y - segment_y) / (previous_x - segment_x) * previous_x
                if 0 <= intersection_with_previous <= rectangle_height:
                    intersection_y_coordinates.append(intersection_with_previous)
    
    intersection_y_coordinates.sort()
    total_area = 0
    INF = 1e16
    EPSILON = 1e-11

    for y_start, y_end in zip(intersection_y_coordinates, intersection_y_coordinates[1:]):
        if abs(y_end - y_start) < EPSILON:
            continue
        y_middle = (y_start + y_end) / 2

        boundary_values = []
        for segment_x, segment_y in segment_endpoints:
            if segment_x != 0:
                boundary_value = y_middle + (segment_y - y_middle) / (segment_x + EPSILON) * rectangle_width
            else:
                boundary_value = 0 if segment_y <= y_middle else rectangle_height
            boundary_value = max(0, min(rectangle_height, boundary_value))
            boundary_values.append(boundary_value)

        sorted_boundary_values = sorted(boundary_values)
        lower_boundary = sorted_boundary_values[number_of_lines - 1]
        upper_boundary = sorted_boundary_values[number_of_lines]

        area_contribution = (y_end - y_start) * (upper_boundary - lower_boundary)
        total_area += area_contribution

    print("{:0.11f}".format(total_area / rectangle_height / rectangle_height))