def shredder():
    import sys
    sys.setrecursionlimit(10**7)
    for line in sys.stdin:
        t, num = line.strip().split()
        if t == '0' and num == '0':
            break
        t = int(t)
        n = len(num)
        if t == int(num):
            print(num)
            continue

        dp = [{} for _ in range(n+1)]
        dp[0][0] = [()]

        for i in range(1, n+1):
            for j in range(max(0, t+1)):
                if dp[i-1].get(j) is None:
                    continue
                for k in range(i, n+1):
                    part = int(num[i-1:k])
                    s = j + part
                    if s <= t:
                        if s not in dp[k]:
                            dp[k][s] = []
                        dp[k][s].extend([way + (part,) for way in dp[i-1][j]])

        if not dp[n]:
            print("error")
            continue

        max_sum = max(dp[n].keys())
        ways = dp[n][max_sum]

        if len(ways) > 1:
            uniq = set(ways)
            if len(uniq) > 1:
                print("rejected")
                continue

        print(max_sum, *ways[0])

shredder()