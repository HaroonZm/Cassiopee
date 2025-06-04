if __name__ == '__main__':
    while True:
        M, N = list(map(int, input().split()))
        if M == 0 and N == 0:
            break

        X1 = []
        Y1 = []
        X2 = []
        Z2 = []
        for i in range(M):
            tmp = input().split()
            X1.append(int(tmp[0]))
            Y1.append(int(tmp[1]))
        for i in range(N):
            tmp = input().split()
            X2.append(int(tmp[0]))
            Z2.append(int(tmp[1]))

        min1 = min(X1)
        max1 = max(X1)
        min2 = min(X2)
        max2 = max(X2)

        xs = sorted(X1 + X2)
        res = 0

        for i in range(len(xs) - 1):
            a = xs[i]
            b = xs[i + 1]
            c = (a + b) / 2

            if min1 <= c <= max1 and min2 <= c <= max2:
                # width on X1/Y1 at a
                lb = float("inf")
                ub = -float("inf")
                for j in range(M):
                    x1 = X1[j]
                    y1 = Y1[j]
                    x2 = X1[(j + 1) % M]
                    y2 = Y1[(j + 1) % M]
                    if (x1 - a) * (x2 - a) <= 0 and x1 != x2:
                        y = y1 + (y2 - y1) * (a - x1) / (x2 - x1)
                        lb = min(lb, y)
                        ub = max(ub, y)
                wa = max(0, ub - lb)

                lb = float("inf")
                ub = -float("inf")
                for j in range(N):
                    x1 = X2[j]
                    y1 = Z2[j]
                    x2 = X2[(j + 1) % N]
                    y2 = Z2[(j + 1) % N]
                    if (x1 - a) * (x2 - a) <= 0 and x1 != x2:
                        y = y1 + (y2 - y1) * (a - x1) / (x2 - x1)
                        lb = min(lb, y)
                        ub = max(ub, y)
                wa2 = max(0, ub - lb)

                lb = float("inf")
                ub = -float("inf")
                for j in range(M):
                    x1 = X1[j]
                    y1 = Y1[j]
                    x2 = X1[(j + 1) % M]
                    y2 = Y1[(j + 1) % M]
                    if (x1 - b) * (x2 - b) <= 0 and x1 != x2:
                        y = y1 + (y2 - y1) * (b - x1) / (x2 - x1)
                        lb = min(lb, y)
                        ub = max(ub, y)
                wb = max(0, ub - lb)

                lb = float("inf")
                ub = -float("inf")
                for j in range(N):
                    x1 = X2[j]
                    y1 = Z2[j]
                    x2 = X2[(j + 1) % N]
                    y2 = Z2[(j + 1) % N]
                    if (x1 - b) * (x2 - b) <= 0 and x1 != x2:
                        y = y1 + (y2 - y1) * (b - x1) / (x2 - x1)
                        lb = min(lb, y)
                        ub = max(ub, y)
                wb2 = max(0, ub - lb)

                lb = float("inf")
                ub = -float("inf")
                for j in range(M):
                    x1 = X1[j]
                    y1 = Y1[j]
                    x2 = X1[(j + 1) % M]
                    y2 = Y1[(j + 1) % M]
                    if (x1 - c) * (x2 - c) <= 0 and x1 != x2:
                        y = y1 + (y2 - y1) * (c - x1) / (x2 - x1)
                        lb = min(lb, y)
                        ub = max(ub, y)
                wc = max(0, ub - lb)

                lb = float("inf")
                ub = -float("inf")
                for j in range(N):
                    x1 = X2[j]
                    y1 = Z2[j]
                    x2 = X2[(j + 1) % N]
                    y2 = Z2[(j + 1) % N]
                    if (x1 - c) * (x2 - c) <= 0 and x1 != x2:
                        y = y1 + (y2 - y1) * (c - x1) / (x2 - x1)
                        lb = min(lb, y)
                        ub = max(ub, y)
                wc2 = max(0, ub - lb)

                fa = wa * wa2
                fb = wb * wb2
                fc = wc * wc2
                res += ((b - a) / 6) * (fa + 4 * fc + fb)
        print(res)