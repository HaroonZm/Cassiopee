N = int(input())
A = sorted((list(map(int, input().split()))))

if N == 2:
    y, x = A
    print(x-y)
    print(x, y)
    exit()

XY = []

PLUS = 0
MINUS = 0
for a in A:
    if a >= 0:
        PLUS += 1
    else:
        MINUS += 1

XY = []
tmp = A[0]
if PLUS and MINUS:
    while PLUS >= 2:
        x, y = tmp, A.pop()
        XY.append((x, y))
        tmp = x-y
        PLUS -= 1
    x, y = A.pop(), tmp
    XY.append((x, y))
    tmp = x-y
    N = len(A)
    for i in range(1, N):
        a = A[i]
        x, y = tmp, a
        XY.append((x, y))
        tmp = x-y
elif PLUS:
    for i in range(N-1):
        if i < N-2:
            x, y = tmp, A.pop()
            XY.append((x, y))
            tmp = x-y
        if i == N-2:
            x, y = A.pop(), tmp
            XY.append((x, y))
            tmp = x-y
else:
    for i in range(N-1):
        if i == 0:
            x, y = A.pop(), tmp
            XY.append((x, y))
            tmp = x-y
        else:
            x, y = tmp, A.pop()
            XY.append((x, y))
            tmp = x-y       
ans = tmp
print(ans)
for x, y in XY:
    print(x, y)