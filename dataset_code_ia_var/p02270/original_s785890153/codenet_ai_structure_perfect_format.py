N, K = map(int, input().split())
W = [int(input()) for _ in range(N)]
P_MIN = max(W)
P_MAX = 10 ** 9
while P_MIN < P_MAX:
    P = (P_MAX + P_MIN) // 2
    M = 0
    i = 0
    while i < N:
        mass = 0
        while i < N and mass + W[i] <= P:
            mass += W[i]
            i += 1
        M += 1
    if M > K:
        P_MIN = P + 1
    elif M <= K:
        P_MAX = P
print(P_MIN)