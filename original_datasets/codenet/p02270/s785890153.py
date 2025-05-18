N, K = map(int, input().split())
W = [int(input()) for _ in range(N)]
P_MIN = max(W)
P_MAX = 10 ** 9
while P_MIN < P_MAX:
    P = (P_MAX + P_MIN) // 2  # トラックの最大積載量
    M = 0
    i = 0
    while i < N:  # 最大積載量Pのトラックに荷物がなくなるまで載せる
        mass = 0  # トラックは初め何も載っていない
        while i < N and mass + W[i] <= P:  # 荷物がなくなるか，トラックに積めなくなるまで荷物を載せる
            mass += W[i]
            i += 1
        M += 1  # 使用したトラックの台数が1だけ増える
    if M > K:  # 最大積載量が小さすぎて，トラックが足りない場合
        P_MIN = P + 1
    elif M <= K:  # 逆に最大積載量が大きすぎて，トラックが余る場合
        P_MAX = P
print(P_MIN)