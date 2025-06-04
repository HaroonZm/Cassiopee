import random

num_days = int(input())
decay_rates = list(map(int, input().split()))
satisfaction_matrix = [list(map(int, input().split())) for day_idx in range(num_days)]

def calculate_total_score(selected_contests):
    total_score = 0
    last_held_day = [0] * 26
    for current_day in range(num_days):
        contest_type = selected_contests[current_day] - 1
        last_held_day[contest_type] = current_day + 1
        total_score += satisfaction_matrix[current_day][contest_type]
        for contest_idx in range(26):
            total_score -= decay_rates[contest_idx] * (current_day + 1 - last_held_day[contest_idx])
    return total_score

best_schedule = [1 + day_idx % 26 for day_idx in range(365)]
best_score = calculate_total_score(best_schedule)

for offset in range(1, 26):
    candidate_schedule = [1 + (day_idx) % 26 for day_idx in range(offset, 365 + offset)]
    candidate_score = calculate_total_score(candidate_schedule)
    if candidate_score > best_score:
        best_score = candidate_score
        best_schedule = candidate_schedule[:]

print(*best_schedule, sep="\n")