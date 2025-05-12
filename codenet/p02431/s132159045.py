_q = int(input())
v = []
for _ in range(_q):
    *q, = map(int, input().split())

    if q[0] == 0:
        v.append(q[1])
    elif q[0] == 1:
        print(v[q[1]])
    elif q[0] == 2:
        v.pop()