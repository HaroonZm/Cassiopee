def f(s, cost, route, ans):
    route += [s]
    ans = ans + cost.pop(s)
    for edge in data:
        if s in edge:
            nodes = list(edge)
            other = nodes[1] if nodes[0] == s else nodes[0]
            if not other in route:
                current = cost.get(other, None)
                if current is None or data[edge] < current:
                    cost[other] = data[edge]
    if len(cost):
        nxt = min(cost, key=lambda x: cost[x])
        return f(nxt, cost, route, ans)
    return ans

while True:
    n, m = [int(x) for x in raw_input().split()]
    if n == 0 and m == 0:
        break
    data = dict()
    i = 0
    while i < m:
        tpl = raw_input().split()
        if len(tpl) != 3:
            continue
        a, b, c = [int(v) for v in tpl]
        data[(a, b)] = c
        i += 1
    print(f(0, {0: 0}, [], 0))