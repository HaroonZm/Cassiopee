number_of_runners, track_length, total_rounds = map(int, input().split())
runner_speeds = [int(input()) for _ in range(number_of_runners)]
current_positions = [0] * number_of_runners
bottle_counts = [0] * track_length

for runner_index in range(number_of_runners):
    current_positions[runner_index] = (current_positions[runner_index] + runner_speeds[runner_index]) % track_length
    bottle_counts[current_positions[runner_index]] += 1

for _ in range(total_rounds - 1):
    new_bottle_counts = [0] * track_length
    for runner_index in range(number_of_runners):
        bottle_counts[current_positions[runner_index]] -= 1
        current_positions[runner_index] = (current_positions[runner_index] + runner_speeds[runner_index]) % track_length
        new_bottle_counts[current_positions[runner_index]] += 1
    for position_index in range(track_length):
        if bottle_counts[position_index] < new_bottle_counts[position_index]:
            bottle_counts[position_index] = new_bottle_counts[position_index]
        bottle_counts[position_index] += new_bottle_counts[position_index]

print(sum(bottle_counts))