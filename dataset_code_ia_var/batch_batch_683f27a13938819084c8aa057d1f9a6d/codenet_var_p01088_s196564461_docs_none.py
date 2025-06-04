while 1:
    n = input()
    if n == 0:
        break
    L = 500 * n
    dp = [None] * (L + 1)
    dp[0] = (0, 0)
    for i in xrange(n):
        dp2 = dp[:]
        cost = int(raw_input())
        d3 = cost % 1000
        for j in xrange(L + 1):
            if dp[j] is None:
                continue
            num, su = dp[j]
            if d3 == 0:
                if 500 <= j:
                    if dp2[j - 500] is None or (num + 1, su - cost) > dp2[j - 500]:
                        dp2[j - 500] = (num + 1, su - cost)
            elif 1 <= d3 <= 500 + j:
                if dp2[j + (500 - d3)] is None or (num + 1, su - cost) > dp2[j + (500 - d3)]:
                    dp2[j + (500 - d3)] = (num + 1, su - cost)
            else:
                if dp2[j + (1000 - d3)] is None or (num, su - cost) > dp2[j + (1000 - d3)]:
                    dp2[j + (1000 - d3)] = (num, su - cost)
        dp, dp2 = dp2, dp
    num, su = max(x for x in dp if x is not None)
    print num, -su