import sys
input = sys.stdin.readline

N, R, L = map(int, input().split())
logs = [tuple(map(int, input().split())) for _ in range(R)]

scores = [0] * (N + 1)
times = [0] * (N + 1)

current_best_score = 0
current_best_team = 1
visible_start = 0

# Accumulated visible time for each team
visible_time = [0] * (N + 1)

def update_best():
    max_score = max(scores[1:])
    candidates = [i for i, s in enumerate(scores[1:], 1) if s == max_score]
    return max_score, min(candidates)

for i in range(R):
    d, t, x = logs[i]
    scores[d] += x
    last_best_score, last_best_team = current_best_score, current_best_team
    current_best_score, current_best_team = update_best()
    if current_best_team != last_best_team:
        visible_time[last_best_team] += t - visible_start
        visible_start = t

if visible_start < L:
    visible_time[current_best_team] += L - visible_start

max_visible = max(visible_time[1:])
ans = min(i for i, v in enumerate(visible_time[1:], 1) if v == max_visible)
print(ans)