import sys

n, q = map(int, input().split())
P = [i for i in range(n)]
for line in sys.stdin:
    order = line.strip("\n").split()
    x, y = map(int, order[1:])
    if x > y:
        x, y = y, x
    while True:
        if x == P[x]:
            break
        x = P[x]
    while True:
        if y == P[y]:
            break
        y = P[y]
    if order[0] == "0":
        P[x] = P[y]
    elif order[0] == "1":
        if y == x:
            print(1)
        else:
            print(0)