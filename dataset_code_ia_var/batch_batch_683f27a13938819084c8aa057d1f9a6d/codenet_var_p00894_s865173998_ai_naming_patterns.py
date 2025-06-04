while True:
    event_count = input()
    if event_count == 0:
        break
    entry_time_map = {}
    admin_entry_time = -1
    time_accum_map = {}
    for event_index in xrange(event_count):
        event_parts = raw_input().split()
        hour, minute = map(int, event_parts[1].split(":"))
        absolute_minute = 60 * hour + minute
        is_entry = event_parts[2] == 'I'
        user_id = event_parts[3]

        if user_id == '000':
            if is_entry:
                admin_entry_time = absolute_minute
            else:
                for participant_id in entry_time_map:
                    if participant_id != user_id and entry_time_map[participant_id] != -1:
                        previous = time_accum_map.get(participant_id, 0)
                        time_delta = absolute_minute - max(admin_entry_time, entry_time_map[participant_id])
                        time_accum_map[participant_id] = previous + time_delta
                admin_entry_time = -1
        else:
            if is_entry:
                entry_time_map[user_id] = absolute_minute
            else:
                if admin_entry_time != -1:
                    previous = time_accum_map.get(user_id, 0)
                    time_delta = absolute_minute - max(admin_entry_time, entry_time_map[user_id])
                    time_accum_map[user_id] = previous + time_delta
                entry_time_map[user_id] = -1
    print max(time_accum_map.values()) if time_accum_map else 0