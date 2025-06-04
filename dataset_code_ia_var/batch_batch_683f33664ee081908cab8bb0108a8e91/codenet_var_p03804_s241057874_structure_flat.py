N, M = map(int, input().split())
A = []
i = 0
while i < N:
    A.append(input())
    i += 1
B = []
i = 0
while i < M:
    B.append(input())
    i += 1
l = 0
L = len(A[0])
L2 = len(B[0])
found = False
while l <= L - L2:
    i = 0
    while i <= N - M:
        s = A[i][l:]
        if B[0] in s:
            if s.find(B[0]) == 0:
                m = 1
                ok = True
                while m < M:
                    t = A[i + m][l:]
                    if B[m] not in t:
                        ok = False
                        break
                    if t.find(B[m]) != 0:
                        ok = False
                        break
                    m += 1
                if ok:
                    print("Yes")
                    exit()
        i += 1
    l += 1
print("No")