n = int(input())
for _ in range(n):
    k, p = map(int, input().split())
    winner = k % p
    if winner == 0:
        winner = p
    print(winner)