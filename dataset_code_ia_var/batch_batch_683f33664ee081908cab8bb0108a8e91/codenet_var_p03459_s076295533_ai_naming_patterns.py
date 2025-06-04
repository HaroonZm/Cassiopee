num_events = int(input())
event_times = [0]
event_positions = [(0, 0)]
for event_index in range(num_events):
    time_value, x_coord, y_coord = map(int, input().split())
    event_times.append(time_value)
    event_positions.append((x_coord, y_coord))

def can_reach_position(start_pos, end_pos, time_delta):
    distance = abs(start_pos[0] - end_pos[0]) + abs(start_pos[1] - end_pos[1])
    if distance > time_delta:
        return False
    if distance % 2 != time_delta % 2:
        return False
    return True

all_reachable = True
for check_index in range(1, num_events + 1):
    previous_position = event_positions[check_index - 1]
    current_position = event_positions[check_index]
    time_difference = event_times[check_index] - event_times[check_index - 1]
    if not can_reach_position(previous_position, current_position, time_difference):
        all_reachable = False
        break

if all_reachable:
    print('Yes')
else:
    print('No')