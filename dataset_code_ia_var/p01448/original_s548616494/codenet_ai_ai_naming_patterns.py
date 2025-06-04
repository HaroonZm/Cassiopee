input_n = int(input())
interval_list = []
max_right = 0
for interval_index in range(input_n):
    interval_points = [int(value) for value in input().split()]
    interval_end = interval_points[1] + 1
    if interval_end > max_right:
        max_right = interval_end
    interval_list.append([interval_points[0], interval_end])

events_table = [0] * (max_right + 1)
for interval_index in range(input_n):
    start_point = interval_list[interval_index][0]
    end_point = interval_list[interval_index][1]
    events_table[start_point] += 1
    events_table[end_point] -= 1

for position in range(1, max_right + 1):
    events_table[position] += events_table[position - 1]

maximum_answer = 0
total_positions = len(events_table)
for position in range(total_positions):
    if position <= events_table[position] + 1 and position <= input_n + 1:
        if position > maximum_answer:
            maximum_answer = position

print(maximum_answer - 1)