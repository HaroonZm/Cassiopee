from collections import deque

while True:
    number_of_segments, number_of_destinations = map(int, input().split())

    if number_of_segments == 0 and number_of_destinations == 0:
        break

    segment_lengths = list(map(int, input().split()))
    destination_points = sorted(map(int, input().split()))

    total_segment_length = sum(segment_lengths)

    remaining_cost = sum(
        destination_point - total_segment_length
        for destination_point in destination_points
        if total_segment_length <= destination_point
    )

    memoization_cache = { (1 << number_of_segments) - 1: remaining_cost }

    def minimum_total_cost(bitmask_state, current_position, destination_index):
        if bitmask_state in memoization_cache:
            return memoization_cache[bitmask_state]

        minimal_cost = float('inf')

        for segment_index in range(number_of_segments):
            if (bitmask_state >> segment_index) & 1 == 0:
                move_cost = 0
                temp_destination_index = destination_index
                new_position = current_position + segment_lengths[segment_index]
                while (temp_destination_index < number_of_destinations and 
                       destination_points[temp_destination_index] <= new_position):
                    distance_cost = min(
                        new_position - destination_points[temp_destination_index],
                        destination_points[temp_destination_index] - current_position
                    )
                    move_cost += distance_cost
                    temp_destination_index += 1

                total_cost = move_cost + minimum_total_cost(
                    bitmask_state | (1 << segment_index),
                    current_position + segment_lengths[segment_index],
                    temp_destination_index
                )

                minimal_cost = min(minimal_cost, total_cost)

        memoization_cache[bitmask_state] = minimal_cost
        return minimal_cost

    print(minimum_total_cost(0, 0, 0))