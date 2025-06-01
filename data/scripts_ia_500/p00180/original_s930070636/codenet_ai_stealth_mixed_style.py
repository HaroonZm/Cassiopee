def f(s, cost, route, ans):
    route.append(s)
    ans += cost[s]
    cost.pop(s)
    for k in data.keys():
        if s in k:
            a, b = k
            other = b if s == a else a
            if other not in route:
                if other not in cost or data[k] < cost[other]:
                    cost[other] = data[k]
    if cost:
        s = min(cost.items(), key=lambda x: x[1])[0]
        return f(s, cost, route, ans)
    return ans

while True:
    n, m = tuple(map(int, input().split()))
    if n == 0 and m == 0:
        break
    data = {}
    for _ in range(m):
        a, b, c = map(int, input().split())
        data[(a,b)] = c
    result = f(0, {0: 0}, [], 0)
    print(result)