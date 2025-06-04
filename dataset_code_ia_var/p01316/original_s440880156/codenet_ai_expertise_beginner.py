def main():
    import sys
    input = lambda: sys.stdin.readline().rstrip()
    INF = 10**12

    # Calculer les différences au carré pour chaque (i, j)
    sq_diff = []
    for i in range(256):
        row = []
        for j in range(256):
            row.append((i-j)**2)
        sq_diff.append(row)

    while True:
        line = input()
        if not line:
            break
        N_M = line.split()
        if len(N_M) < 2:
            continue
        N = int(N_M[0])
        M = int(N_M[1])

        if N == 0 and M == 0:
            break

        C = []
        for _ in range(M):
            C.append(int(input()))
        x = []
        for _ in range(N):
            x.append(int(input()))

        # Préparer la table de normalisation
        normalize = []
        for i in range(256):
            row = []
            for c in C:
                val = i + c
                if val > 255:
                    row.append(255)
                elif val < 0:
                    row.append(0)
                else:
                    row.append(val)
            normalize.append(row)

        # Initialiser dp
        dp_cur = [INF]*256
        dp_cur[128] = 0
        dp_next = [INF]*256

        for i in x:
            for j in range(256):
                cost_cur = dp_cur[j]
                for k in range(len(C)):
                    l = normalize[j][k]
                    cost_next = cost_cur + sq_diff[i][l]
                    if cost_next < dp_next[l]:
                        dp_next[l] = cost_next
            for idx in range(256):
                dp_cur[idx] = dp_next[idx]
                dp_next[idx] = INF

        print(min(dp_cur))

if __name__ == '__main__':
    main()