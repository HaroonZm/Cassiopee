num_events, interval_gap, total_duration = map(int, input().split())
event_times = list(map(int, input().split()))

gap_durations = [event_times[0]]
for idx in range(1, num_events):
    gap_durations.append(event_times[idx] - event_times[idx - 1])
gap_durations.append(total_duration - event_times[num_events - 1])

unused_time = 0
unused_time += gap_durations[0] - interval_gap
for gap_idx in range(1, num_events):
    unused_time += max(0, gap_durations[gap_idx] - 2 * interval_gap)
unused_time += max(0, gap_durations[num_events] - interval_gap)

print(unused_time)