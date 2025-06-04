N, Q, S, T = map(int, input().split())
A = [int(input()) for _ in range(N+1)]
B = []
for i in range(N):
    B.append(A[i+1] - A[i])
C = 0
for i in range(N):
    if A[i] < A[i+1]:
        C += S * (A[i] - A[i+1])
    else:
        C += T * (A[i] - A[i+1])
ans = []
for _ in range(Q):
    l, r, x = map(int, input().split())
    # process B[l-1]
    if x >= 0:
        if B[l-1] <= 0:
            if B[l-1] + x <= 0:
                C += - T * x
            else:
                C += T * B[l-1] - S * (B[l-1] + x)
        else:
            C += - S * x
    else:
        if B[l-1] >= 0:
            if B[l-1] + x >= 0:
                C += - S * x
            else:
                C += S * B[l-1] - T * (B[l-1] + x)
        else:
            C += - T * x
    B[l-1] += x
    if r < N:
        # process B[r] with -x
        y = -x
        if y >= 0:
            if B[r] <= 0:
                if B[r] + y <= 0:
                    C += - T * y
                else:
                    C += T * B[r] - S * (B[r] + y)
            else:
                C += - S * y
        else:
            if B[r] >= 0:
                if B[r] + y >= 0:
                    C += - S * y
                else:
                    C += S * B[r] - T * (B[r] + y)
            else:
                C += - T * y
        B[r] += y
    ans.append(C)
for v in ans:
    print(v)