n = int(input())
max_fish = -1
winner = -1

for _ in range(n):
    a, v = map(int, input().split())
    if v > max_fish or (v == max_fish and a < winner):
        max_fish = v
        winner = a

print(winner, max_fish)