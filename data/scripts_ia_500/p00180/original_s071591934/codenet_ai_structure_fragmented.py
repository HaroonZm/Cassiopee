def append_to_route(s, route):
    route.append(s)

def add_cost_to_ans(s, cost, ans):
    ans += cost[s]
    return ans

def remove_cost_entry(s, cost):
    del cost[s]

def is_edge_connected_to_s(k, s):
    return s in k

def get_edge_nodes(k):
    return k

def is_s_equal_to_a(s, a):
    return s == a

def is_node_not_in_route(node, route):
    return node not in route

def is_node_not_in_cost(node, cost):
    return node not in cost

def is_c_less_than_cost(c, cost_node):
    return c < cost_node

def update_cost_and_remove_data(a, b, c, cost, route):
    if is_node_not_in_route(b, route):
        if is_node_not_in_cost(b, cost) or is_c_less_than_cost(c, cost[b]):
            cost[b] = c
            del data[(a, b)]

def update_cost_and_remove_data_reverse(a, b, c, cost, route):
    if is_node_not_in_route(a, route):
        if is_node_not_in_cost(a, cost) or is_c_less_than_cost(c, cost[a]):
            cost[a] = c
            del data[(a, b)]

def process_edge(s, k, c, cost, route):
    a, b = get_edge_nodes(k)
    if is_s_equal_to_a(s, a):
        update_cost_and_remove_data(a, b, c, cost, route)
    elif s == b:
        update_cost_and_remove_data_reverse(a, b, c, cost, route)

def process_edges(s, cost, route):
    for k, c in data.items():
        if is_edge_connected_to_s(k, s):
            process_edge(s, k, c, cost, route)

def choose_next_s(cost):
    sorted_cost_items = sorted(cost.items(), key=lambda x: x[1])
    next_s = sorted_cost_items[0][0]
    return next_s

def f(s, cost, route, ans):
    append_to_route(s, route)
    ans = add_cost_to_ans(s, cost, ans)
    remove_cost_entry(s, cost)
    process_edges(s, cost, route)
    if cost:
        s = choose_next_s(cost)
        return f(s, cost, route, ans)
    return ans

def read_input():
    return map(int, raw_input().split())

def create_data(m):
    data = {}
    for i in range(m):
        a, b, c = map(int, raw_input().split())
        data[(a, b)] = c
    return data

while True:
    n, m = read_input()
    if n == m == 0:
        break
    data = create_data(m)
    print f(0, {0:0}, [], 0)