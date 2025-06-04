while True:
    num_rooms, num_meetings = map(int, raw_input().split())
    if num_rooms == 0:
        break
    meeting_schedule = [[0] * 1261 for _ in range(num_meetings)]
    num_events = input()
    event_list = [map(int, raw_input().split()) for _ in range(num_events)]
    sorted_events = sorted(event_list, key=lambda event: event[1])
    for event_idx in range(0, num_events, 2):
        start_time1, unused_n1, room_id1, unused_s1 = sorted_events[event_idx]
        start_time2, unused_n2, room_id2, unused_s2 = sorted_events[event_idx + 1]
        meeting_schedule[room_id1 - 1][start_time1:start_time2] = [1] * (start_time2 - start_time1)
    num_requests = input()
    for request_idx in range(num_requests):
        time_start, time_end, req_room_id = map(int, raw_input().split())
        print sum(meeting_schedule[req_room_id - 1][time_start:time_end])