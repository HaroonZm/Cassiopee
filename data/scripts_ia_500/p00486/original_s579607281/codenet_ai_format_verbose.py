from bisect import bisect_left
MAX_INF = 10 ** 20

def main():
    
    width, height = map(int, input().split())
    number_of_points = int(input())
    
    x_coordinates = []
    y_coordinates = []
    
    append_x = x_coordinates.append
    append_y = y_coordinates.append
    
    for _ in range(number_of_points):
        x_pos, y_pos = map(int, input().split())
        append_x(x_pos)
        append_y(y_pos)
    
    sorted_x_coordinates = sorted(x_coordinates)
    sorted_y_coordinates = sorted(y_coordinates)
    
    cumulative_sum_x = []
    cumulative_sum_y = []
    
    append_cum_x = cumulative_sum_x.append
    append_cum_y = cumulative_sum_y.append
    
    accumulated_x = 0
    accumulated_y = 0
    
    for index in range(number_of_points):
        accumulated_x += sorted_x_coordinates[index]
        accumulated_y += sorted_y_coordinates[index]
        append_cum_x(accumulated_x)
        append_cum_y(accumulated_y)
    
    if number_of_points % 2 == 1:
        center_left_x = center_right_x = sorted_x_coordinates[number_of_points // 2]
        center_left_y = center_right_y = sorted_y_coordinates[number_of_points // 2]
    else:
        center_left_x = sorted_x_coordinates[number_of_points // 2 - 1]
        center_right_x = sorted_x_coordinates[number_of_points // 2]
        center_left_y = sorted_y_coordinates[number_of_points // 2 - 1]
        center_right_y = sorted_y_coordinates[number_of_points // 2]
    
    position_left_x = bisect_left(sorted_x_coordinates, center_left_x)
    position_right_x = bisect_left(sorted_x_coordinates, center_right_x)
    position_left_y = bisect_left(sorted_y_coordinates, center_left_y)
    position_right_y = bisect_left(sorted_y_coordinates, center_right_y)
    
    if position_left_x != 0:
        x_length_left = (accumulated_x - cumulative_sum_x[position_left_x - 1] * 2 - center_left_x * (number_of_points - position_left_x * 2)) * 2
    else:
        x_length_left = (accumulated_x - center_left_x * number_of_points) * 2
    
    if position_right_x != 0:
        x_length_right = (accumulated_x - cumulative_sum_x[position_right_x - 1] * 2 - center_right_x * (number_of_points - position_right_x * 2)) * 2
    else:
        x_length_right = (accumulated_x - center_right_x * number_of_points) * 2
    
    if position_left_y != 0:
        y_length_left = (accumulated_y - cumulative_sum_y[position_left_y - 1] * 2 - center_left_y * (number_of_points - position_left_y * 2)) * 2
    else:
        y_length_left = (accumulated_y - center_left_y * number_of_points) * 2
    
    if position_right_y != 0:
        y_length_right = (accumulated_y - cumulative_sum_y[position_right_y - 1] * 2 - center_right_y * (number_of_points - position_right_y * 2)) * 2
    else:
        y_length_right = (accumulated_y - center_right_y * number_of_points) * 2
    
    minimum_total_length = MAX_INF
    answer_x = MAX_INF
    answer_y = MAX_INF
    maximum_distance_sum = 0
    
    for index in range(number_of_points):
        
        current_x = x_coordinates[index]
        current_y = y_coordinates[index]
        
        if current_x <= center_left_x:
            chosen_center_x = center_right_x
            current_x_length = x_length_right
        else:
            chosen_center_x = center_left_x
            current_x_length = x_length_left
        
        if current_y <= center_left_y:
            chosen_center_y = center_right_y
            current_y_length = y_length_right
        else:
            chosen_center_y = center_left_y
            current_y_length = y_length_left
        
        delta_x = abs(current_x - chosen_center_x)
        delta_y = abs(current_y - chosen_center_y)
        
        if maximum_distance_sum > delta_x + delta_y:
            continue
        
        maximum_distance_sum = delta_x + delta_y
        
        total_length = current_x_length + current_y_length - maximum_distance_sum
        
        if minimum_total_length > total_length:
            minimum_total_length = total_length
            answer_x = chosen_center_x
            answer_y = chosen_center_y
        elif minimum_total_length == total_length:
            if answer_x > chosen_center_x or (answer_x == chosen_center_x and answer_y > chosen_center_y):
                answer_x = chosen_center_x
                answer_y = chosen_center_y
    
    print(minimum_total_length)
    print(answer_x, answer_y)

main()