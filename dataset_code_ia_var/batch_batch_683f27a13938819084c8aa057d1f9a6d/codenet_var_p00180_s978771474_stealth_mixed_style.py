def func(node, total):
    stack = list(dic.keys())
    while stack:
        key = stack.pop()
        a, b = key
        val = dic[key]
        if a == node:
            if cost.get(b, float('inf')) > val:
                cost[b] = val
        if b == node:
            if cost.get(a, float('inf')) > val:
                cost[a] = val

    keys = list(cost.keys())
    pairs = sorted([(k, cost[k]) for k in keys], key=lambda z: z[1])

    from operator import itemgetter
    for item in pairs:
        to = itemgetter(0)(item)
        if to not in result:
            result.append(to)
            total += itemgetter(1)(item)
            del cost[to]
            return func(to, total)
    else:
        return total

while 1:
    n, m = map(int, raw_input().split())
    if not (n or m): break
    dic = dict()
    line = raw_input().split()
    s, b, c = int(line[0]), int(line[1]), int(line[2])
    dic[(s, b)] = c
    for __ in range(m-1):
        a, b, c = (int(x) for x in raw_input().split())
        dic[(a, b)] = c
    cost = {}
    result = [s]
    print(func(s, 0))