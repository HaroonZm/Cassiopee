def solve():
    import sys
    input_stream = sys.stdin

    def compute_score(x, y):
        diff = abs(x - y)
        return diff * (diff - 30) ** 2

    while True:
        line = input_stream.readline()
        if not line:
            break
        values = list(map(int, line.strip().split()))
        if len(values) < 2:
            break
        M, W = values[0], values[1]

        if M == 0:
            break

        bm = [int(x) for x in input_stream.readline().split()]
        bw = list(map(int, input_stream.readline().split()))

        energies = []
        for m in bm:
            row = []
            for w in bw:
                row.append(compute_score(m, w))
            energies.append(row)

        dp_prev = dict()
        dp_prev[0] = 0

        for i in range(M):
            dp_curr = dict(dp_prev)
            mask_bit = 1 << W
            for mask in dp_prev:
                for j in range(W):
                    if not (mask & (1 << j)):
                        new_mask = mask | (1 << j)
                        val = dp_prev[mask] + energies[i][j]
                        if new_mask not in dp_curr or val > dp_curr[new_mask]:
                            dp_curr[new_mask] = val
            dp_prev = dp_curr

        print(max(dp_prev.values()))

solve()