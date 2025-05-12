n, p = map(int, input().split())

e = [tuple(map(int, input().split())) for _ in range(n)]
# e = [(w,b), ...]

e2 = sorted(((100 - p) * w + p * b for w, b in e), reverse=True)

rest = p * sum(b for _, b in e)

cur = 0
while rest > 0 and cur < n:
    rest -= e2[cur]
    cur += 1
print(cur)