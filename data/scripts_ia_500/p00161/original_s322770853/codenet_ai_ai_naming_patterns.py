while True:
    number_of_entries = int(input())
    if number_of_entries == 0:
        break
    time_id_pairs = []
    for entry_index in range(number_of_entries):
        entry_values = [int(value) for value in input().split()]
        participant_id = entry_values[0]
        minutes_seconds = entry_values[1:]
        total_time_seconds = (minutes_seconds[0] + minutes_seconds[2] + minutes_seconds[4] + minutes_seconds[6]) * 60 + sum([minutes_seconds[1], minutes_seconds[3], minutes_seconds[5], minutes_seconds[7]])
        time_id_pairs.append([total_time_seconds, participant_id])
    time_id_pairs.sort()
    print(time_id_pairs[0][1])
    print(time_id_pairs[1][1])
    print(time_id_pairs[-2][1])