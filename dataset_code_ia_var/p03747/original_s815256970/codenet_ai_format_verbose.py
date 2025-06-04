import bisect

number_of_balls, belt_length, time_duration = map(int, input().split())

initial_positions_and_directions = [
    list(map(int, input().split())) for _ in range(number_of_balls)
]

positions_clockwise = []
positions_anticlockwise = []
final_positions_by_index = [None] * number_of_balls

for index, (initial_position, direction) in enumerate(initial_positions_and_directions):

    if direction == 1:
        positions_clockwise.append((initial_position, index))
    else:
        positions_anticlockwise.append((initial_position, index))

count_clockwise = len(positions_clockwise)
count_anticlockwise = len(positions_anticlockwise)

positions_clockwise.sort()
positions_anticlockwise.sort()

for original_index, (initial_position, direction) in enumerate(initial_positions_and_directions):

    if direction == 1:

        shifted_right = (2 * time_duration + initial_position) % belt_length
        right_bisect_index = bisect.bisect_right(
            positions_anticlockwise, (shifted_right, float('inf'))
        )
        left_bisect_index = bisect.bisect_right(
            positions_anticlockwise, (initial_position, -float('inf'))
        )
        crossing_count = right_bisect_index - left_bisect_index

        completed_loops = (initial_position + 2 * time_duration) // belt_length

        final_index = (
            original_index + crossing_count + completed_loops * count_anticlockwise
        ) % number_of_balls

        final_position = (initial_position + time_duration) % belt_length
        final_positions_by_index[final_index] = final_position

    else:

        shifted_left = (initial_position - 2 * time_duration) % belt_length
        left_bisect_index = bisect.bisect_left(
            positions_clockwise, (initial_position, -float('inf'))
        )
        right_bisect_index = bisect.bisect_left(
            positions_clockwise, (shifted_left, -float('inf'))
        )
        crossing_count = left_bisect_index - right_bisect_index

        completed_loops = (initial_position - 2 * time_duration) // belt_length

        final_index = (
            original_index - crossing_count + completed_loops * count_clockwise
        ) % number_of_balls

        final_position = (initial_position - time_duration) % belt_length
        final_positions_by_index[final_index] = final_position

for computed_position in final_positions_by_index:
    print(computed_position)