from collections import defaultdict
num_days = int(input())
contest_decay_rates = list(map(int, input().split()))
daily_scores = []
for day_index in range(num_days):
    daily_scores.append(list(map(int, input().split())))
last_held_day = defaultdict(int)
for day_number in range(1, num_days + 1):
    best_score = float('-inf')
    best_contest = None
    for contest_index in range(26):
        current_score = daily_scores[day_number - 1][contest_index]
        current_score += contest_decay_rates[contest_index] * (day_number - last_held_day[contest_index])
        if current_score > best_score:
            best_score = current_score
            best_contest = contest_index
    print(best_contest + 1)
    last_held_day[best_contest] = day_number