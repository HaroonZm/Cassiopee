def f(A):
    return A.count(a) > 1

R = [0, 3, 6]
N = range(9)
Z = [0] * 9

n = input()
while n:
    F = []
    for i in Z:
        F.append([" "] * 9)

    M = []
    for i in Z:
        line = raw_input().split()
        line = list(map(int, line))
        M.append(line)

    M1 = []
    for x in N:
        col = []
        for y in N:
            col.append(M[y][x])
        M1.append(col)

    M2 = []
    for y in R:
        for x in R:
            block = []
            for i in range(3):
                block += M[y + i][x:x + 3]
            M2.append(block)

    for y in N:
        A = M[y]
        p0 = (y // 3) * 3
        for x in N:
            p = p0 + (x // 3)
            a = A[x]
            if f(A) or f(M1[x]) or f(M2[p]):
                F[y][x] = "*"

    for y in N:
        line = ""
        for a, b in zip(F[y], M[y]):
            line += a + str(b)
        print(line)

    if n > 1:
        print()
    n = n - 1