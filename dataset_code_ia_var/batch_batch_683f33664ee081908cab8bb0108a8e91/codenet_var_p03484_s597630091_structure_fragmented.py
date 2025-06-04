import sys
from bisect import bisect_right

def get_read_functions():
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    return read, readline, readlines

def input_N(readline):
    return int(readline())

def input_m(read):
    return map(int, read().split())

def input_AB(m):
    return zip(m, m)

def init_graph(N):
    return [[] for _ in range(N + 1)]

def add_edge_to_graph(graph, a, b):
    graph[a].append(b)
    graph[b].append(a)

def build_graph(N, AB):
    graph = init_graph(N)
    for a, b in AB:
        add_edge_to_graph(graph, a, b)
    return graph

def get_root():
    return 1

def init_parent(N):
    return [0] * (N + 1)

def init_order():
    return []

def init_stack(root):
    return [root]

def process_children(graph, parent, x, stack):
    for y in graph[x]:
        if y == parent[x]:
            continue
        parent[y] = x
        stack.append(y)

def make_order_and_parent(graph, root, parent):
    order = init_order()
    stack = init_stack(root)
    while stack:
        x = stack.pop()
        order.append(x)
        process_children(graph, parent, x, stack)
    return order, parent

def pop_x_elements(S, x):
    seg = 0
    while S and S[-1] == x:
        S.pop()
        seg += 1
    return seg

def get_lower_upper(S, x):
    i = bisect_right(S, x // 2)
    lower = S[:i][::-1]
    upper = S[i:]
    return lower, upper

def make_pairs_inner(upper, lower, x, cand, rest):
    seg = 0
    for b in upper[::-1]:
        while lower and lower[-1] + b <= x:
            cand.append(lower.pop())
        if cand:
            cand.pop()
            seg += 1
        else:
            rest.append(b)
    return seg

def post_process_cand_rest(cand, rest, seg):
    L = len(cand)
    q, r = divmod(L, 2)
    if r:
        return seg + len(rest) + q, cand[0]
    else:
        seg += q
        if rest:
            return seg + len(rest) - 1, rest[-1]
        else:
            return seg, 0

def make_pairs(S, x):
    seg = pop_x_elements(S, x)
    lower, upper = get_lower_upper(S, x)
    cand = []
    rest = []
    seg += make_pairs_inner(upper, lower, x, cand, rest)
    return post_process_cand_rest(cand, rest, seg)

def init_dp(N):
    return [0] * (N + 1)

def init_temp(N):
    return [[] for _ in range(N + 1)]

def update_temp(temp, p, l):
    temp[p].append(l + 1)

def update_dp(dp, v, s):
    dp[v] += s

def update_dp_parent(dp, p, v):
    dp[p] += dp[v]

def solve_inner(order, parent, temp, dp, x):
    for v in order[::-1]:
        p = parent[v]
        S = temp[v]
        S.sort()
        s, l = make_pairs(S, x)
        update_dp(dp, v, s)
        update_dp_parent(dp, p, v)
        update_temp(temp, p, l)
        if v == 1:
            if not l:
                return dp[1]
            else:
                return dp[1] + 1

def solve(N, order, parent, x):
    dp = init_dp(N)
    temp = init_temp(N)
    return solve_inner(order, parent, temp, dp, x)

def find_seg(N, order, parent):
    extra = 10
    return solve(N, order, parent, N + extra)

def binary_search(N, order, parent, seg):
    left = 0
    right = N
    while left + 1 < right:
        x = (left + right) // 2
        if solve(N, order, parent, x) == seg:
            right = x
        else:
            left = x
    return right

def print_result(seg, right):
    print(seg, right)

def main():
    read, readline, readlines = get_read_functions()
    N = input_N(readline)
    m = input_m(read)
    AB = input_AB(m)
    graph = build_graph(N, AB)
    root = get_root()
    parent = init_parent(N)
    order, parent = make_order_and_parent(graph, root, parent)
    seg = find_seg(N, order, parent)
    right = binary_search(N, order, parent, seg)
    print_result(seg, right)

if __name__ == "__main__":
    main()