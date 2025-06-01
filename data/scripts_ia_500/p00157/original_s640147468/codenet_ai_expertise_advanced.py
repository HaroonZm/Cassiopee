from sys import stdin

def read_matrix(n):
    return [tuple(map(int, stdin.readline().split())) for _ in range(n)]

while True:
    n = int(stdin.readline())
    if n == 0:
        break
    M1 = read_matrix(n)
    m = int(stdin.readline())
    M2 = read_matrix(m)

    f1 = [-1] * n
    f2 = [-1] * m

    for i, (h1, r1) in enumerate(M1):
        for j, (h2, r2) in enumerate(M2):
            if h1 < h2 and r1 < r2:
                f2[j] = i
            elif h1 > h2 and r1 > r2:
                f1[i] = j

    c1 = [-1] * (n + 1)
    c2 = [-1] * (m + 1)

    p1 = p2 = 0
    while p1 < n or p2 < m:
        if p1 < n:
            if f1[p1] < 0:
                c1[p1] = (c1[p1 - 1] if p1 else 0) + 1
                p1 += 1
            elif c2[f1[p1]] >= 0:
                c1[p1] = max(c1[p1 - 1] if p1 else 0, c2[f1[p1]]) + 1
                p1 += 1
        if p2 < m:
            if f2[p2] < 0:
                c2[p2] = (c2[p2 - 1] if p2 else 0) + 1
                p2 += 1
            elif c1[f2[p2]] >= 0:
                c2[p2] = max(c2[p2 - 1] if p2 else 0, c1[f2[p2]]) + 1
                p2 += 1

    print(max(c1 + c2))