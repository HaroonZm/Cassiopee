R = range(9)

def f1(M, F):
    for y in R:
        A = M[y]
        for x in R:
            if A.count(A[x]) >= 2:
                F[y][x] = "*"

def f2(M, F):
    for x in R:
        A = []
        for y in R:
            A.append(M[y][x])
        for y in R:
            if A.count(A[y]) >= 2:
                F[y][x] = "*"

def f3(M, F):
    for i in R:
        x = (i % 3) * 3
        y = (i // 3) * 3
        A = M[y][x:x+3] + M[y+1][x:x+3] + M[y+2][x:x+3]
        for j in R:
            if A.count(A[j]) >= 2:
                F[y + (j // 3)][x + (j % 3)] = "*"

n = int(raw_input())
while n > 0:
    M = []
    F = []
    for _ in range(9):
        F.append([" "] * 9)
    for _ in range(9):
        line = raw_input().split()
        row = []
        for num in line:
            row.append(int(num))
        M.append(row)
    f1(M, F)
    f2(M, F)
    f3(M, F)
    for i in R:
        line = ""
        for j in R:
            line += F[i][j] + str(M[i][j])
        print line
    if n > 1:
        print
    n -= 1