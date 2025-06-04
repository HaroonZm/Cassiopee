import bisect

M = []
D = []
N = []
count = 0

q = int(input())
for _ in range(q):
    query = list(map(str, input().split()))
    typ = int(query[0])
    if typ == 0:
        key = query[1]
        x = int(query[2])
        y = bisect.bisect_left(D, key)
        if y < count and D[y] == key:
            M[y][1] = x
            N[y] = x
        else:
            M.insert(y, [key, x])
            D.insert(y, key)
            N.insert(y, x)
            count += 1
    elif typ == 1:
        key = query[1]
        y = bisect.bisect_left(D, key)
        if y < count and D[y] == key:
            print(N[y])
        else:
            print(0)
    elif typ == 2:
        key = query[1]
        y = bisect.bisect_left(D, key)
        if y < count and D[y] == key:
            M.pop(y)
            D.pop(y)
            N.pop(y)
            count -= 1
    else:
        L = query[1]
        R = query[2]
        s = bisect.bisect_left(D, L)
        e = bisect.bisect_right(D, R)
        if e - s > 0:
            for i in range(s, e):
                print(M[i][0] + " " + str(M[i][1]))