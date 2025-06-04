def run_main():
    output_list = []

    while True:
        segment_results = process_input()
        if segment_results == -1:
            break
        output_list += segment_results

    for output_value in output_list:
        print(output_value)

def process_input():
    result_list = []
    num_rooms, num_tracks = map(int, input().split())
    if (num_rooms, num_tracks) == (0, 0):
        return -1
    slot_matrix = [[0] * (1260 - 540 + 1) for _ in range(num_tracks)]
    num_events = int(input())
    for _ in range(num_events):
        event_time, room_id, track_id, status_flag = map(int, input().split())
        slot_index = event_time - 540
        adjusted_track = track_id - 1
        if status_flag == 1:
            slot_matrix[adjusted_track][slot_index] += 1
        elif status_flag == 0:
            slot_matrix[adjusted_track][slot_index] -= 1
    for track_idx, track_slots in enumerate(slot_matrix):
        active_count = 0
        for slot_idx, slot_value in enumerate(track_slots):
            active_count += slot_value
            if active_count >= 1:
                slot_matrix[track_idx][slot_idx] = 1
            else:
                slot_matrix[track_idx][slot_idx] = 0
    num_queries = int(input())
    for _ in range(num_queries):
        query_start, query_end, query_track = map(int, input().split())
        sliced_start = query_start - 540
        sliced_end = query_end - 540
        query_track_idx = query_track - 1
        busy_sum = sum(slot_matrix[query_track_idx][sliced_start:sliced_end])
        result_list.append(busy_sum)
    return result_list

run_main()