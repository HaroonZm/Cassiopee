def all_used_for_current(used, cur):
    return all(used[cur])

def unused_nodes(ns, used, cur):
    return [d for d, s in zip(range(ns+1), used[cur]) if not s]

def mark_used(used, i, cur):
    used[cur][i] = True
    used[i][cur] = True

def unmark_used(used, i, cur):
    used[cur][i] = False
    used[i][cur] = False

def extend_route(route, cur, i, ret):
    return [[cur, i]] + ret

def make_routes(ns, used, cur):
    if all_used_for_current(used, cur):
        yield []
    else:
        for i in unused_nodes(ns, used, cur):
            mark_used(used, i, cur)
            for ret in make_routes(ns, used, i):
                yield extend_route([], cur, i, ret)
            unmark_used(used, i, cur)

def get_input_line():
    return raw_input().split()

def parse_ns_nl():
    parts = get_input_line()
    return map(int, parts)

def create_costs(ns):
    return [[0]*(ns+1) for _ in xrange(ns+1)]

def create_used(ns):
    return [[True]*(ns+1) for _ in xrange(ns+1)]

def update_costs_and_used(costs, used, a, b, c):
    costs[a][b] = c
    costs[b][a] = c
    used[a][b] = False
    used[b][a] = False

def process_nl_lines(nl, costs, used):
    for _ in xrange(nl):
        a, b, c = map(int, get_input_line())
        update_costs_and_used(costs, used, a, b, c)

def route_cost(costs, route):
    return sum(costs[a][b] for a, b in route)

def process_routes_for_i(ns, used, costs, ans, i):
    for route in make_routes(ns, used, i):
        cost = route_cost(costs, route)
        if ans[0] < cost:
            ans[0] = cost
            ans[1] = route

def process_routes(ns, used, costs):
    ans = [0, []]
    for i in xrange(1, ns):
        process_routes_for_i(ns, used, costs, ans, i)
    return ans

def format_route_output(route):
    if not route:
        return ''
    head = str(route[0][0])
    rest = " ".join(str(a[1]) for a in route)
    return "{} {}".format(head, rest)

def process_case(ns, nl):
    costs = create_costs(ns)
    used = create_used(ns)
    process_nl_lines(nl, costs, used)
    ans = process_routes(ns, used, costs)
    print ans[0]
    print format_route_output(ans[1])

def main():
    while True:
        ns, nl = parse_ns_nl()
        if ns == 0 and nl == 0:
            break
        process_case(ns, nl)

main()