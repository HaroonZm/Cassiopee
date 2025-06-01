N, M = map(int, input().split())
prices = list(map(int, input().split()))
log = []

while True:
    s, t, e = map(int, input().split())
    if s == 0 and t == 0 and e == 0:
        break
    log.append((s, t, e))

L = int(input())

for _ in range(L):
    res = []
    for i in range(1, N+1):
        salary = 0
        for (s, t, e) in log:
            if s == i:
                salary += prices[t-1] * e
        res.append(salary)
    print(*res)