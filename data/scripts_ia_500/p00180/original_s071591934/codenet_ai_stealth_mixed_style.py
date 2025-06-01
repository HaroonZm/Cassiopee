def f(s, cost, route, ans):
    route.append(s)
    ans += cost[s]
    cost.pop(s)
    for edge, cst in list(data.items()):
        a, b = edge
        if s == a and b not in route:
            if b not in cost or cst < cost[b]:
                cost[b] = cst
                del data[edge]
        elif s == b and a not in route:
            if a not in cost or cst < cost[a]:
                cost[a] = cst
                del data[edge]
    if cost:
        s = min(cost, key=cost.get)
        return f(s, cost, route, ans)
    else:
        return ans

while True:
    line = input()
    if line == '0 0':
        break
    n, m = map(int, line.split())
    data = dict()
    for _ in range(m):
        a, b, c = map(int, input().split())
        data[(a, b)] = c
    result = f(0, {0: 0}, list(), 0)
    print(result)