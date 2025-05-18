if __name__ == "__main__":
    num_nodes = int(input())
    P = list(map(lambda x: float(x), input().split()))
    Q = list(map(lambda x: float(x), input().split()))

    Depth = [[0] * (num_nodes + 1) for i in range(num_nodes + 1)]
    Exp = [[0.0] * (num_nodes + 1) for i in range(num_nodes + 1)]
    Cum_prob = [0.0] * (2 * num_nodes + 2)

    for i in range(2 * num_nodes + 1):
        Cum_prob[i + 1] = Cum_prob[i] + (P[i // 2] if i % 2 else Q[i // 2])

    for i in range(num_nodes + 1):
        Exp[i][i] = Q[i]
        Depth[i][i] = i

    for l in range(1, num_nodes + 1):
        for i in range(num_nodes + 1 - l):
            j = i + l
            d0 = Depth[i][j - 1]
            d1 = Depth[i + 1][j]
            d2 = -1
            cost = 1e30
            for k in range(d0, min(d1 + 1, j)):
                v = Exp[i][k] + Exp[k + 1][j]
                if v < cost:
                    d2 = k
                    cost = v
            Depth[i][j] = d2
            Exp[i][j] = cost + Cum_prob[2 * j + 1] - Cum_prob[2 * i]

    print(f"{Exp[0][num_nodes]:.5f}")