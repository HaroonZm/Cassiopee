N, t = [int(e) for e in input().split()]

ts = [[int(e) for e in input().split()] for _ in range(N)]

result = 0
for x, h in ts:
    r = h * t / x
    result = max(result, r)

print(result)