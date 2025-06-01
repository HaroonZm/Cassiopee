def add_to_route(s, route):
    route.append(s)

def add_cost_to_answer(s, cost, ans):
    return ans + cost[s]

def remove_from_cost(s, cost):
    del cost[s]

def update_costs(s, cost, route, data):
    for k, c in data.items():
        if s in k:
            a, b = k
            other = b if s == a else a
            if not other in route:
                if other not in cost or c < cost[other]:
                    cost[other] = c

def get_next_s(cost):
    return sorted(cost.items(), key=lambda x: x[1])[0][0]

def recursive_f(s, cost, route, ans, data):
    add_to_route(s, route)
    ans = add_cost_to_answer(s, cost, ans)
    remove_from_cost(s, cost)
    update_costs(s, cost, route, data)
    if cost:
        s = get_next_s(cost)
        return recursive_f(s, cost, route, ans, data)
    return ans

def run():
    while True:
        n, m = map(int, raw_input().split())
        if n == m == 0:
            break
        data = {}
        for _ in range(m):
            a, b, c = map(int, raw_input().split())
            data[(a, b)] = c
        print(recursive_f(0, {0:0}, [], 0, data))