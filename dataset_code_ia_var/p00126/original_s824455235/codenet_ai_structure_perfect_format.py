def f(A):
    return A.count(a) > 1

R = [0, 3, 6]
N = range(9)
Z = [0] * 9

n = input()
while n:
    F = [[" " for _ in Z] for _ in Z]
    M = [map(int, raw_input().split()) for _ in Z]
    M1 = [[M[y][x] for y in N] for x in N]
    M2 = [M[y][x:x+3] + M[y+1][x:x+3] + M[y+2][x:x+3] for y in R for x in R]
    for y in N:
        A = M[y]
        p0 = y // 3 * 3
        for x in N:
            p = p0 + x // 3
            a = A[x]
            if any(map(f, [A, M1[x], M2[p]])):
                F[y][x] = "*"
        print "".join([a + b for a, b in zip(F[y], map(str, A))])
    if n > 1:
        print
    n -= 1