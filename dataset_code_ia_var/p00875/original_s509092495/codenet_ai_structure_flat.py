INF = 10**9

while 1:
    n = input()
    if n == 0:
        break
    P = [raw_input().split() for i in xrange(n)]
    g = raw_input()
    d = raw_input()
    memo = {}

    stack = [(g, 0)]
    ans = INF

    while stack:
        s, steps = stack.pop()
        if len(s) > len(d):
            continue
        if s == d:
            ans = min(ans, steps)
            continue
        if s in memo and memo[s] <= steps:
            continue
        memo[s] = steps
        for a, b in P:
            r = s.replace(a, b)
            if r != s:
                stack.append((r, steps + 1))
    print ans if ans < INF else -1