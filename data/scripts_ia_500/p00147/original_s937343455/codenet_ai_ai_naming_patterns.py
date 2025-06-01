def decrement_eat_timers():
    to_delete = []
    for entity_id in eat_timers:
        eat_timers[entity_id] -= 1
        if eat_timers[entity_id] == 0:
            clear_counter_marks(entity_id)
            to_delete.append(entity_id)
    for entity_id in to_delete:
        del eat_timers[entity_id]

def clear_counter_marks(entity_id):
    for idx, value in enumerate(counter_slots):
        if value == entity_id:
            counter_slots[idx] = '_'

def increment_wait_timers():
    for entity_id in wait_timers:
        wait_timers[entity_id] += 1

def check_and_assign_slot(entity_id, wait_time):
    segment_length = 5 if entity_id % 5 == 1 else 2
    for start_idx, slot_value in enumerate(counter_slots):
        if slot_value == '_':
            if counter_slots[start_idx:start_idx + segment_length] == ['_'] * segment_length:
                for idx in range(start_idx, start_idx + segment_length):
                    counter_slots[idx] = entity_id
                else:
                    results[entity_id] = wait_time
                    return True
    return False

results = {}
process_queue = []
wait_timers = {}
eat_timers = {}
counter_slots = ['_' for _ in range(17)]
time_step = 0

while True:
    decrement_eat_timers()
    increment_wait_timers()
    if process_queue:
        for entity_id in process_queue[:]:
            if check_and_assign_slot(entity_id, wait_timers[entity_id]):
                del wait_timers[entity_id]
                del process_queue[0]
                eat_timers[entity_id] = 17*(entity_id % 2) + 3*(entity_id % 3) + 19
            else:
                break
    if len(results) == 100:
        break
    if time_step <= 495:
        if time_step % 5 == 0:
            entity_id = time_step // 5
            if not process_queue and check_and_assign_slot(entity_id, 0):
                eat_timers[entity_id] = 17*(entity_id % 2) + 3*(entity_id % 3) + 19
            else:
                process_queue.append(entity_id)
                wait_timers[entity_id] = 0
    time_step += 1

while True:
    try:
        print(results[int(input())])
    except EOFError:
        break