def f(n, ans):
    for key, val in dic.items():
        a, b = key
        if a == n:
            if b not in cost or val < cost[b]:
                cost[b] = val
        elif b == n:
            if a not in cost or val < cost[a]:
                cost[a] = val
    items = sorted(cost.items(), key=lambda pair: pair[1])
    for k, c in items:
        if k not in res:
            res.append(k)
            ans = ans + c
            del cost[k]
            return f(k, ans)
    return ans

while True:
    line = raw_input()
    if line == "0 0":
        break
    n, m = [int(x) for x in line.split()]
    dic = dict()
    s, b, c = map(int, raw_input().split())
    dic[(s, b)] = c
    for i in xrange(m-1):
        a, b, c = map(int, raw_input().split())
        dic[(a, b)] = c
    cost = {}
    res = list()
    res += [s]
    print f(s, 0)