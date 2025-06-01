import sys

def calculate_convex_hull(points_list, turn_direction):
    initial_max_cosine = {"right": -1.0, "left": 1.0}
    convex_hull = [points_list[0]]
    current_point = points_list[0]
    while True:
        max_cosine = initial_max_cosine[turn_direction]
        for index in range(1, len(points_list)):
            candidate_point = points_list[index]
            if candidate_point[1] < current_point[1] or candidate_point == current_point:
                continue
            vector_x = candidate_point[0] - current_point[0]
            vector_y = candidate_point[1] - current_point[1]
            vector_length = (vector_x ** 2 + vector_y ** 2) ** 0.5
            cosine_value = vector_x / vector_length
            if turn_direction == "right" and cosine_value >= max_cosine:
                max_cosine = cosine_value
                next_point = candidate_point
            if turn_direction == "left" and cosine_value <= max_cosine:
                max_cosine = cosine_value
                next_point = candidate_point
        current_point = next_point
        convex_hull.append(next_point)
        if next_point == points_list[-1]:
            break
    return convex_hull

while True:
    number_of_points = int(raw_input())
    if number_of_points == 0:
        break
    points_collection = []
    for _ in range(number_of_points):
        input_line = raw_input()
        point_coordinates = map(float, input_line.split(","))
        points_collection.append(point_coordinates)
    points_collection.sort(key=lambda point: point[1])
    right_hull = calculate_convex_hull(points_collection, "right")
    left_hull = calculate_convex_hull(points_collection, "left")
    total_points = len(points_collection)
    hull_points = len(right_hull) + len(left_hull) - 2
    print total_points - hull_points