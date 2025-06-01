from bisect import bisect_left

INFINITY = 10 ** 20

width, height = map(int, input().split())
number_of_points = int(input())

x_coordinates = []
y_coordinates = []

for _ in range(number_of_points):
    x, y = map(int, input().split())
    x_coordinates.append(x)
    y_coordinates.append(y)

sorted_x_coordinates = sorted(x_coordinates)
sorted_x_coordinates_doubled = sorted(x_coordinates * 2)
sorted_y_coordinates = sorted(y_coordinates)
sorted_y_coordinates_doubled = sorted(y_coordinates * 2)

accumulated_sum_x = 0
accumulated_sum_y = 0

cumulative_sum_x = []
cumulative_sum_y = []

for index in range(number_of_points):
    accumulated_sum_x += sorted_x_coordinates[index]
    accumulated_sum_y += sorted_y_coordinates[index]
    cumulative_sum_x.append(accumulated_sum_x)
    cumulative_sum_y.append(accumulated_sum_y)

candidate_left_x = sorted_x_coordinates_doubled[number_of_points - 1]
candidate_right_x = sorted_x_coordinates_doubled[number_of_points]
candidate_lower_y = sorted_y_coordinates_doubled[number_of_points - 1]
candidate_upper_y = sorted_y_coordinates_doubled[number_of_points]

max_index = number_of_points * 2 - 1

minimum_total_length = INFINITY
answer_x = 10 ** 10
answer_y = 10 ** 10

for index in range(number_of_points):
    current_x = x_coordinates[index]
    current_y = y_coordinates[index]

    if current_x <= candidate_left_x:
        chosen_x = candidate_right_x
    else:
        chosen_x = candidate_left_x

    if current_y <= candidate_lower_y:
        chosen_y = candidate_upper_y
    else:
        chosen_y = candidate_lower_y

    position_x = bisect_left(sorted_x_coordinates, chosen_x)
    position_y = bisect_left(sorted_y_coordinates, chosen_y)

    if position_x:
        x_length = (chosen_x * position_x - cumulative_sum_x[position_x - 1]) * 2 + (accumulated_sum_x - cumulative_sum_x[position_x - 1] - chosen_x * (number_of_points - position_x)) * 2 - abs(current_x - chosen_x)
    else:
        x_length = (accumulated_sum_x - chosen_x * number_of_points) * 2 - abs(current_x - chosen_x)

    if position_y:
        y_length = (chosen_y * position_y - cumulative_sum_y[position_y - 1]) * 2 + (accumulated_sum_y - cumulative_sum_y[position_y - 1] - chosen_y * (number_of_points - position_y)) * 2 - abs(current_y - chosen_y)
    else:
        y_length = (accumulated_sum_y - chosen_y * number_of_points) * 2 - abs(current_y - chosen_y)

    total_length = x_length + y_length

    if minimum_total_length > total_length:
        minimum_total_length = total_length
        answer_x = chosen_x
        answer_y = chosen_y
    elif minimum_total_length == total_length:
        if answer_x > chosen_x:
            answer_x = chosen_x
            answer_y = chosen_y
        elif answer_x == chosen_x:
            if answer_y > chosen_y:
                answer_y = chosen_y

print(minimum_total_length)
print(answer_x, answer_y)