import bisect

A, B, Q = map(int, input().split())

large_number = 10 ** 11

S = [-large_number]
for i in range(A):
    S.append(int(input()))
S.append(large_number)

T = [-large_number]
for i in range(B):
    T.append(int(input()))
T.append(large_number)

X = []
for i in range(Q):
    X.append(int(input()))

for i in range(Q):
    x = X[i]
    pos_s = bisect.bisect_right(S, x)
    pos_t = bisect.bisect_right(T, x)
    candidates = []
    # Checking all combinations of neighbors
    for s in [S[pos_s], S[pos_s - 1]]:
        for t in [T[pos_t], T[pos_t - 1]]:
            d1 = abs(x - s) + abs(s - t)
            d2 = abs(x - t) + abs(t - s)
            candidates.append(d1)
            candidates.append(d2)
    print(min(candidates))