def f(s, cost, route, ans):
    route.append(s)
    ans += cost[s]
    del cost[s]
    for k, c in data.items():
        if s in k:
            a, b = k
            b = b if s == a else a
            if not b in route:
                if not b in cost or c < cost[b]:
                    cost[b] = c
    if cost:
        s = sorted(cost.items(), key=lambda x: x[1])[0][0]
        return f(s, cost, route, ans)
    return ans

while 1:
    n, m = map(int, raw_input().split())
    if n == m == 0: break
    data = {}
    for i in range(m):
        a, b, c = map(int, raw_input().split())
        data[(a, b)] = c
    print f(0, {0:0}, [], 0)