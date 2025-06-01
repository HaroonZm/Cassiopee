import sys
sys.setrecursionlimit(100000)
N = []
K = []
C = []
while True:
    line = input().split()
    n, k = int(line[0]), int(line[1])
    if n == 0 and k == 0:
        break
    N.append(n)
    K.append(k)
    c = []
    for _ in range(k):
        c.append(int(input()))
    C.append(c)
for idx in range(len(N)):
    c = C[idx]
    n = N[idx]
    k = K[idx]
    c.sort()
    ans = 0
    if c[0] == 0:
        tmp = 1
        for i in range(len(c)-2):
            v1 = c[i+1]
            v2 = c[i+2]
            diff = v2 - v1
            if diff == 1:
                if tmp == 0:
                    s = 0
                elif tmp > 0:
                    s = 1
                else:
                    s = -1
                tmp += 1 * s
                if abs(tmp) > abs(ans):
                    ans = tmp
            elif diff == 2:
                if tmp > 0:
                    tmp = -tmp - 2
                else:
                    tmp = -3
            else:
                tmp = 1
        if ans > 0:
            ans += 1
        ans = abs(ans)
    else:
        tmp = 1
        for i in range(len(c)-1):
            v1 = c[i]
            v2 = c[i+1]
            if v2 - v1 == 1:
                tmp += 1
                if tmp > ans:
                    ans = tmp
            else:
                tmp = 1
    print(ans)