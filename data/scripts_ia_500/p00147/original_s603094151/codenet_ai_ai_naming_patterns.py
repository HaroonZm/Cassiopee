from heapq import heappop, heappush

STATUS_OUT, STATUS_IN = 0, 1

def pattern_p(index):
    return 31 if index % 5 == 1 else 3

def increment_m(index):
    return 17 * (index % 2) + 3 * (index % 3) + 19

def find_first_available_slot(bitmask, pattern):
    for position in range(16):
        if ((bitmask >> position) & pattern) == 0:
            return position
    return None

answer_list = [-1] * 100 + [0]
priority_queue = list(map(lambda idx: (idx * 5, idx, STATUS_IN, None), range(100)))
occupied_bitmask = 1 << 17

while len(priority_queue) != 0:
    current_time, current_index, event_type, slot_index = heappop(priority_queue)
    if event_type == STATUS_IN:
        current_pattern = pattern_p(current_index)
        free_slot = find_first_available_slot(occupied_bitmask, current_pattern)
        if answer_list[current_index - 1] != -1 and free_slot is not None:
            occupied_bitmask = occupied_bitmask | (current_pattern << free_slot)
            answer_list[current_index] = current_time - current_index * 5
            heappush(priority_queue, (current_time + increment_m(current_index), current_index, STATUS_OUT, free_slot))
        else:
            heappush(priority_queue, (current_time + 1, current_index, STATUS_IN, None))
    else:
        current_pattern = pattern_p(current_index)
        occupied_bitmask = occupied_bitmask ^ (current_pattern << slot_index)

while True:
    try:
        input_index = input()
        print(answer_list[input_index])
    except:
        break