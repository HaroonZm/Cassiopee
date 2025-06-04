n = int(input())
max_fish = -1
winner = -1
for _ in range(n):
    a, v = map(int, input().split())
    if v > max_fish:
        max_fish = v
        winner = a
    elif v == max_fish and a < winner:
        winner = a
print(winner, max_fish)