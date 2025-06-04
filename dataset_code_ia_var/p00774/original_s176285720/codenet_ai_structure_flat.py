l = 0
while l == 0:
    H = int(input())
    if H == 0:
        quit()
    else:
        A = []
        for _ in range(H):
            A.append(list(map(int, input().split())))
        p = 0
        ans = 0
        while p == 0:
            this = 0
            i = 0
            while i < len(A):
                now = 1
                j = 1
                while j < 5:
                    if A[i][j] == A[i][j-1] and A[i][j] != 0:
                        now += 1
                    else:
                        if now >= 3:
                            this = 1
                            ans += A[i][j-1] * now
                            k = j - now
                            while k < j:
                                A[i][k] = 0
                                k += 1
                        now = 1
                    j += 1
                if now >= 3:
                    this = 1
                    ans += A[i][j-1] * now
                    k = j - now
                    while k < j:
                        A[i][k] = 0
                        k += 1
                i += 1
            if this == 0:
                p = 1
            N = len(A)
            i = 1
            while i <= N:
                j = 0
                while j < 5:
                    if A[N-i][j] == 0 and i != N:
                        k = 1
                        while (N-i-k >= 0) and A[N-i-k][j] == 0 and (k + i < N):
                            k += 1
                        if N-i-k >= 0:
                            A[N-i][j] = A[N-i-k][j]
                            A[N-i-k][j] = 0
                    j += 1
                i += 1
            q = 0
            while q == 0:
                idx = -1
                i = 0
                while i < len(A):
                    if A[i] == [0,0,0,0,0]:
                        idx = i
                        break
                    i += 1
                if idx != -1:
                    A.pop(idx)
                else:
                    q = 1
        print(ans)