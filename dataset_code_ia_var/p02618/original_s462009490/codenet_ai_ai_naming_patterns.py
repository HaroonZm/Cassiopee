num_days = int(input())
penalty_list = list(map(int, input().split()))
penalty_sum = 0
for penalty_index in range(26):
    penalty_sum += penalty_list[penalty_index]
score_grid = [ [] for _ in range(num_days)]
for day_index in range(num_days):
    score_grid[day_index] = list(map(int, input().split()))
assigned_type = [0 for _ in range(num_days)]
last_type_day = [-1 for _ in range(26)]
for current_day in range(num_days):
    best_score = -1001002003
    best_type = 0
    for type_index in range(26):
        current_score = score_grid[current_day][type_index]
        for penalty_index in range(26):
            if type_index != penalty_index:
                current_score -= penalty_list[penalty_index] * (current_day - last_type_day[penalty_index])
        if current_score > best_score:
            best_score = current_score
            best_type = type_index
            assigned_type[current_day] = type_index
    last_type_day[assigned_type[current_day]] = current_day
    print(assigned_type[current_day] + 1)