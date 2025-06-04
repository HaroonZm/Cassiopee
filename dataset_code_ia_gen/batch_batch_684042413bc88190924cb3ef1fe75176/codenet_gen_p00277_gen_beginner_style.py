N, R, L = map(int, input().split())
events = []
for _ in range(R):
    d, t, x = map(int, input().split())
    events.append((t, d, x))

scores = [0] * (N + 1)
time_shown = [0] * (N + 1)

current_time = 0
current_winner = 1
# Initially, all scores are 0, so team 1 is winning by smallest ID

for event in events:
    t, d, x = event
    # Add time from current_time to t to current_winner's shown time
    time_shown[current_winner] += t - current_time
    current_time = t

    # Update score
    scores[d] = x

    # Find leader
    max_score = max(scores[1:])
    candidates = [i for i, score in enumerate(scores[1:], start=1) if score == max_score]
    current_winner = min(candidates)

# Add remaining time after last event
time_shown[current_winner] += L - current_time

max_time = max(time_shown[1:])
candidates = [i for i, t in enumerate(time_shown[1:], start=1) if t == max_time]
print(min(candidates))