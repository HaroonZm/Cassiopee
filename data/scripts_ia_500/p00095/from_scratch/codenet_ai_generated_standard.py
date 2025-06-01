n=int(input())
winner, max_fish = 0, -1
for _ in range(n):
    a,v=map(int,input().split())
    if v>max_fish or (v==max_fish and a<winner):
        winner, max_fish = a, v
print(winner, max_fish)