from bisect import bisect_left

INFINITY = 10 ** 20

def main():
    
    width, height = map(int, input().split())
    number_of_points = int(input())
    
    x_coordinates = []
    y_coordinates = []
    
    for _ in range(number_of_points):
        x_point, y_point = map(int, input().split())
        x_coordinates.append(x_point)
        y_coordinates.append(y_point)
    
    sorted_x_coordinates = sorted(x_coordinates)
    sorted_y_coordinates = sorted(y_coordinates)
    
    cumulative_sum_x = []
    cumulative_sum_y = []
    
    accumulated_x = 0
    accumulated_y = 0
    
    for index in range(number_of_points):
        accumulated_x += sorted_x_coordinates[index]
        accumulated_y += sorted_y_coordinates[index]
        cumulative_sum_x.append(accumulated_x)
        cumulative_sum_y.append(accumulated_y)
    
    if number_of_points % 2 == 1:
        candidate_left_x = candidate_right_x = sorted_x_coordinates[number_of_points // 2]
        candidate_left_y = candidate_right_y = sorted_y_coordinates[number_of_points // 2]
    else:
        candidate_left_x = sorted_x_coordinates[number_of_points // 2 - 1]
        candidate_right_x = sorted_x_coordinates[number_of_points // 2]
        candidate_left_y = sorted_y_coordinates[number_of_points // 2 - 1]
        candidate_right_y = sorted_y_coordinates[number_of_points // 2]
    
    minimum_total_distance = INFINITY
    best_x = None
    best_y = None
    
    for index in range(number_of_points):
        
        current_x = x_coordinates[index]
        current_y = y_coordinates[index]
        
        if current_x <= candidate_left_x:
            chosen_x = candidate_right_x
        else:
            chosen_x = candidate_left_x
        
        if current_y <= candidate_left_y:
            chosen_y = candidate_right_y
        else:
            chosen_y = candidate_left_y
        
        position_x = bisect_left(sorted_x_coordinates, chosen_x)
        position_y = bisect_left(sorted_y_coordinates, chosen_y)
        
        if position_x > 0:
            sum_x_below = cumulative_sum_x[position_x - 1]
            distance_x = ((chosen_x * position_x - sum_x_below) * 2) + ((accumulated_x - sum_x_below - chosen_x * (number_of_points - position_x)) * 2) - abs(current_x - chosen_x)
        else:
            distance_x = (accumulated_x - chosen_x * number_of_points) * 2 - abs(current_x - chosen_x)
        
        if position_y > 0:
            sum_y_below = cumulative_sum_y[position_y - 1]
            distance_y = ((chosen_y * position_y - sum_y_below) * 2) + ((accumulated_y - sum_y_below - chosen_y * (number_of_points - position_y)) * 2) - abs(current_y - chosen_y)
        else:
            distance_y = (accumulated_y - chosen_y * number_of_points) * 2 - abs(current_y - chosen_y)
        
        total_distance = distance_x + distance_y
        
        if total_distance < minimum_total_distance:
            minimum_total_distance = total_distance
            best_x = chosen_x
            best_y = chosen_y
        elif total_distance == minimum_total_distance:
            if best_x > chosen_x:
                best_x = chosen_x
                best_y = chosen_y
            elif best_x == chosen_x:
                if best_y > chosen_y:
                    best_y = chosen_y
    
    print(minimum_total_distance)
    print(best_x, best_y)

main()