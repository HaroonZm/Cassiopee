input_count, result_value = int(input()), 1
event_list = []
for event_index in range(input_count):
    event_list.append((int(input()), 1))
for event_index in range(input_count):
    event_list.append((int(input()), -1))
event_list.sort()
current_total = 0
for event_tuple in event_list:
    event_delta = event_tuple[1]
    if abs(event_delta + current_total) != abs(event_delta) + abs(current_total):
        result_value = (result_value * abs(current_total)) % 1000000007
    current_total += event_delta
print(result_value)