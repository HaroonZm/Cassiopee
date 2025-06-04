input_count, time_limit = map(int, input().split())
candidates = []
for _ in range(input_count):
    cost, time = map(int, input().split())
    if time <= time_limit:
        candidates.append(cost)
if len(candidates) == 0:
    print("TLE")
else:
    print(min(candidates))