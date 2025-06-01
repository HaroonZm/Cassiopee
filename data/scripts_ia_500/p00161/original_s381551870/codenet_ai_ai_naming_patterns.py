while True:
    total_participants = int(input())
    if total_participants == 0:
        break

    participant_times = []
    for _ in range(total_participants):
        participant_data = list(map(int, input().split()))
        participant_id = participant_data.pop(0)

        total_time_seconds = 0
        for _ in range(4):
            minutes = participant_data.pop(0)
            seconds = participant_data.pop(0)
            total_time_seconds += minutes * 60 + seconds

        participant_times.append([participant_id, total_time_seconds])

    participant_times_sorted = sorted(participant_times, key=lambda entry: entry[1])
    print(participant_times_sorted[0][0])
    print(participant_times_sorted[1][0])
    print(participant_times_sorted[-2][0])