# CODE FESTIVAL 2016 Final
# B - Exactly N points

if __name__ == "__main__":

    total_required_points = int(input())

    list_of_selected_points = []

    remaining_points_needed = total_required_points

    current_point_to_add = 1

    while True:
        if remaining_points_needed <= 0:
            if remaining_points_needed == 0:
                break
            else:
                # If we've gone over, remove the point that is the excess
                excess_point = abs(remaining_points_needed)
                list_of_selected_points.remove(excess_point)
                break

        list_of_selected_points.append(current_point_to_add)
        remaining_points_needed -= current_point_to_add
        current_point_to_add += 1

    for selected_point in list_of_selected_points:
        print(selected_point)