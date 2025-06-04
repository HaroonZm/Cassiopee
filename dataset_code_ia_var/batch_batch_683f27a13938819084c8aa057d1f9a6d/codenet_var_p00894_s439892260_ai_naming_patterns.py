while True:
    event_count = int(raw_input())
    if event_count == 0:
        break
    active_participants = set()
    participant_last_time = [0] * 1000
    participant_bless_total = [0] * 1000
    for event_index in xrange(event_count):
        event_month, event_hm, event_type, participant_id = raw_input().split()
        event_hour, event_minute = map(int, event_hm.split(":"))
        event_abs_minute = 60 * event_hour + event_minute
        participant_id = int(participant_id)
        if event_type == "I":
            participant_last_time[participant_id] = event_abs_minute
            active_participants.add(participant_id)
        else:
            active_participants.remove(participant_id)
            if participant_id == 0:
                for current_id in active_participants:
                    participant_bless_total[current_id] += event_abs_minute - max(participant_last_time[participant_id], participant_last_time[current_id])
            elif 0 in active_participants:
                participant_bless_total[participant_id] += event_abs_minute - max(participant_last_time[0], participant_last_time[participant_id])
    print max(participant_bless_total)