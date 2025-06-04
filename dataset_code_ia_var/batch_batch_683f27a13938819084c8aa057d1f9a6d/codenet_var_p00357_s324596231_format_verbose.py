number_of_positions = 0

bounce_distances_from_each_position = []

def is_goal_reachable_from_start() :

    furthest_reached_distance = 0

    for position_index in range(number_of_positions) :

        position_distance = 10 * position_index

        if furthest_reached_distance < position_distance :
            return False

        maximum_reachable_distance = position_distance + bounce_distances_from_each_position[position_index]

        furthest_reached_distance = max(furthest_reached_distance, maximum_reachable_distance)

        if furthest_reached_distance >= 10 * number_of_positions :
            return True

    return False

number_of_positions = int(input())

for _ in range(number_of_positions) :
    bounce_distance = int(input())
    bounce_distances_from_each_position.append(bounce_distance)

if not is_goal_reachable_from_start() :
    print("no")
else :
    bounce_distances_from_each_position.reverse()
    if is_goal_reachable_from_start() :
        print("yes")
    else :
        print("no")