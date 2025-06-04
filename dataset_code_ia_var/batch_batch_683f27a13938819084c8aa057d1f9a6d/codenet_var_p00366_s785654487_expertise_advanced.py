from functools import reduce

n = int(input())
timing = [int(input()) for _ in range(n)]
max_t = max(timing)

divisors = [d for d in range(1, (max_t // 2) + 1) if max_t % d == 0] + [max_t]

def adjustment(t):
    return next((d - t for d in divisors if d >= t), 0)

print(sum(map(adjustment, timing)))