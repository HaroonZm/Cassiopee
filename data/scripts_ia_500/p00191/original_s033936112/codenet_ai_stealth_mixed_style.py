def process():
    import sys
    try:
        while True:
            line = sys.stdin.readline()
            if not line:
                break
            parts = line.strip().split()
            if not parts:
                continue
            n, m = int(parts[0]), int(parts[1])
            if n == 0:
                break
            gs = []
            for _ in range(n):
                row = list(map(float, sys.stdin.readline().strip().split()))
                gs.append(row)
            dp = []
            dp.append([0]*n)
            dp.append([1.0]*n)
            i = 2
            while i <= m:
                temp = []
                for j in range(n):
                    candidates = []
                    for k in range(n):
                        candidates.append(dp[i-1][k]*gs[k][j])
                    temp.append(max(candidates))
                dp.append(temp)
                i += 1
            print("%.2f" % max(dp[m]))
    except EOFError:
        pass

if __name__ == "__main__":
    process()