def f(s, cost, route, ans):
    route.append(s)
    ans += cost[s]
    del cost[s]
    for k, c in data.items():
        if s in k:
            a, b = k
            if s == a:
                if not b in route:
                    if not b in cost or c < cost[b]:
                        cost[b] = c
                        del data[(a, b)]
            elif s == b:
                if not a in route:
                    if not a in cost or c < cost[a]:
                        cost[a] = c
                        del data[(a, b)]
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