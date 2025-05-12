n = int(input())
queries = [list(map(int, input().split())) for i in range(n)]

s, t = 1, 0
for q in queries:
    if q[0] == 1:
        s *= q[1]
        t *= q[1]
    elif q[0] == 2:
        t += q[1]
    else:
        t -= q[1]
print(-t, s)