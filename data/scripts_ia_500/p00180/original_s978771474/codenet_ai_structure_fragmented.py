def update_cost_from_node(n, dic, cost):
    for k, c in dic.items():
        a, b = k
        if a == n:
            update_cost_dict(cost, b, c)
        elif b == n:
            update_cost_dict(cost, a, c)

def update_cost_dict(cost, node, c):
    if node not in cost or c < cost[node]:
        cost[node] = c

def get_next_node(cost, res):
    sorted_cost = sorted(cost.items(), key=lambda x: x[1])
    for k, c in sorted_cost:
        if k not in res:
            return k, c
    return None, None

def process_node(n, ans, dic, cost, res):
    update_cost_from_node(n, dic, cost)
    next_node, cost_value = get_next_node(cost, res)
    if next_node is not None:
        res.append(next_node)
        ans += cost_value
        del cost[next_node]
        return process_node(next_node, ans, dic, cost, res)
    return ans

def parse_edge():
    a, b, c = map(int, raw_input().split())
    return a, b, c

while True:
    n, m = map(int, raw_input().split())
    if n == 0 and m == 0:
        break
    dic = {}
    s, b, c = parse_edge()
    dic[(s, b)] = c
    for i in range(m - 1):
        a, b, c = parse_edge()
        dic[(a, b)] = c
    cost = {}
    res = [s]
    print(process_node(s, 0, dic, cost, res))