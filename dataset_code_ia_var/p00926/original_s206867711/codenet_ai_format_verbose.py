number_of_positions, number_of_events = map(int, input().split())

position_counters = [0] * number_of_positions

for event_index in range(number_of_events):
    
    start_position, end_position = map(int, input().split())
    
    position_counters[start_position - 1] += 1
    position_counters[end_position - 1] -= 1

current_sum = 0
first_active_position = 0
final_answer = number_of_positions + 1

for position_index in range(number_of_positions):
    
    if current_sum == 0 and position_counters[position_index] > 0:
        first_active_position = position_index
    
    current_sum += position_counters[position_index]
    
    if current_sum == 0 and position_counters[position_index] < 0:
        final_answer += (position_index - first_active_position) * 2

print(final_answer)