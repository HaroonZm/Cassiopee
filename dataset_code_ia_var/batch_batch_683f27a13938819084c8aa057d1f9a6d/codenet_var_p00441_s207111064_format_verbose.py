def main():

    while True:
        number_of_points = int(input())

        if number_of_points == 0:
            break

        list_of_points = []
        point_exists_map = {}

        for _ in range(number_of_points):
            point_x, point_y = map(int, input().split())
            point_exists_map[(point_x, point_y)] = True
            list_of_points.append((point_x, point_y))

        maximum_distance_squared = 0

        for first_point_index in range(number_of_points):
            for second_point_index in range(number_of_points):
                first_point = list_of_points[first_point_index]
                second_point = list_of_points[second_point_index]

                vector_x = second_point[0] - first_point[0]
                vector_y = second_point[1] - first_point[1]

                rotated_first_point = (first_point[0] + vector_y, first_point[1] - vector_x)
                rotated_second_point = (second_point[0] + vector_y, second_point[1] - vector_x)

                if rotated_first_point in point_exists_map and rotated_second_point in point_exists_map:
                    squared_distance = vector_x ** 2 + vector_y ** 2
                    if squared_distance > maximum_distance_squared:
                        maximum_distance_squared = squared_distance

        print(maximum_distance_squared)

main()