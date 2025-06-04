import sys
A, B = map(int, sys.stdin.readline().split())

def greedy_count(x):
    coins = 0
    for coin in [B, A, 1]:
        coins += x // coin
        x %= coin
    return coins

def optimal_count(x):
    min_coins = float('inf')
    max_b = x // B
    for b in range(max_b + 1):
        rem = x - b * B
        a = rem // A
        c = rem % A
        count = b + a + c
        if count < min_coins:
            min_coins = count
    return min_coins

limit = A * B  # Checking up to A*B covers all modular classes for coin usage
ans = -1
for x in range(1, limit):
    if greedy_count(x) > optimal_count(x):
        ans = x
        break

print(ans)