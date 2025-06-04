import sys
input = sys.stdin.readline

N, Q, S, T = map(int, input().split())
A = [int(input()) for _ in range(N + 1)]

# Compute initial differences D[i] = A[i] - A[i-1] for i in [1..N]
D = [A[i] - A[i - 1] for i in range(1, N + 1)]

# Compute initial temperature using differences
# temp = sum_over_i ( if D[i]>0: -S*D[i] else T*(-D[i]) )
temp = 0
for d in D:
    if d > 0:
        temp -= S * d
    else:
        temp += T * (-d)

for _ in range(Q):
    L, R, X = map(int, input().split())

    # Update edges that can be affected by the altitude change in [L, R]
    # Only differences at L and R+1 may change:
    # For difference at L: D[L] = A[L] - A[L-1], only if L >= 1
    # For difference at R+1: D[R+1] = A[R+1] - A[R], only if R + 1 <= N

    # Update at L (if L > 1)
    if L > 1:
        i = L - 1  # zero-based index on D
        old = D[i]
        # A[L] changes by X, A[L-1] unchanged -> D[i] += X
        D[i] += X
        new = D[i]
        # update temp
        if old > 0:
            temp += S * old
        else:
            temp -= T * (-old)

        if new > 0:
            temp -= S * new
        else:
            temp += T * (-new)

    # Update at R+1 (if R < N)
    if R < N:
        i = R  # zero-based index on D
        old = D[i]
        # A[R+1] unchanged, A[R] changes by X -> D[i] = A[R+1] - (A[R] + X) = old - X
        D[i] -= X
        new = D[i]

        if old > 0:
            temp += S * old
        else:
            temp -= T * (-old)

        if new > 0:
            temp -= S * new
        else:
            temp += T * (-new)

    # Apply addition of X to A[k] for k in [L,R], but we don't update A fully, we only update differences accordingly on edges L and R+1.

    print(temp)