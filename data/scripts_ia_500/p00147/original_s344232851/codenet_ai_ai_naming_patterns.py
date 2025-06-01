from heapq import heappop, heappush

STATE_OUT = 0
STATE_IN = 1

def pattern_p(index):
    return 31 if index % 5 == 1 else 3

def pattern_m(index):
    return 17 * (index % 2) + 3 * (index % 3) + 19

def find_available_position(bitmask, pattern):
    for position in range(16):
        if ((bitmask >> position) & pattern) == 0:
            return position
    return None

answer_list = [-1] * 100 + [0]

event_queue = list(
    (index * 5, index, STATE_IN, None, pattern_p(index))
    for index in range(100)
)

bitmask_state = 1 << 17

while event_queue:
    current_time, item_index, event_type, shift_index, pattern = heappop(event_queue)
    if event_type == STATE_IN:
        shift_index = find_available_position(bitmask_state, pattern)
        if answer_list[item_index - 1] != -1 and shift_index is not None:
            bitmask_state |= pattern << shift_index
            answer_list[item_index] = current_time - item_index * 5
            heappush(event_queue, (current_time + pattern_m(item_index), item_index, STATE_OUT, shift_index, pattern))
        else:
            heappush(event_queue, (current_time + 1, item_index, STATE_IN, None, pattern))
    else:
        bitmask_state ^= pattern << shift_index

while True:
    try:
        query_index = int(input())
        print(answer_list[query_index])
    except:
        break