from collections import deque
import sys

def init_start_list(N):
    return [0] * (N + 1)

def init_elist(edges):
    return [0] * len(edges)

def count_edge_starts(edges, start):
    for e in edges:
        start[e[0] + 1] += 1

def accumulate_starts(N, start):
    for i in range(1, N + 1):
        start[i] += start[i - 1]

def make_counter(start):
    return start[:]

def fill_elist(edges, elist, counter):
    for e in edges:
        elist[counter[e[0]]] = e[1]
        counter[e[0]] += 1

class csr:
    def __init__(self, N, edges):
        self.start = init_start_list(N)
        self.elist = init_elist(edges)
        count_edge_starts(edges, self.start)
        accumulate_starts(N, self.start)
        counter = make_counter(self.start)
        fill_elist(edges, self.elist, counter)

def make_edges():
    return []

def add_to_edges(edges, v, w):
    edges.append((v, w))

def make_array(size, value=0):
    return [value] * size

def make_order_array(size):
    return [-1] * size

def make_parent_array(size):
    return [-1] * size

def dfs_stack_start(i):
    stack = deque()
    stack.append(i)
    stack.append(i)
    return stack

def stack_not_empty(stack):
    return bool(stack)

def pop_stack(stack):
    return stack.pop()

def update_low_order(v, now_ord, low, order):
    low[v] = order[v] = now_ord

def append_visited(visited, v):
    visited.append(v)

def edges_in_range(startv, endv):
    return range(startv, endv)

def get_next_to(g, v, i):
    return g.elist[i]

def stack_push_to(stack, to):
    stack.append(to)
    stack.append(to)

def set_parent(parent, to, v):
    parent[to] = v

def update_low_from_order(low, v, order, to):
    low[v] = min(low[v], order[to])

def low_eq_order(low, v, order):
    return low[v] == order[v]

def scc_pop_visited(visited):
    return visited.pop()

def mark_as_visited(order, u, N):
    order[u] = N

def assign_group(ids, u, group_num):
    ids[u] = group_num

def found_main_node(u, v):
    return u == v

def incr_group_num(group_num):
    return group_num + 1

def update_parent_low(parent, v, low):
    if parent[v] != -1:
        low[parent[v]] = min(low[parent[v]], low[v])

def finalize_ids(ids, group_num):
    for i, x in enumerate(ids):
        ids[i] = group_num - 1 - x

def make_groups(group_num):
    return [[] for _ in range(group_num)]

def fill_groups(groups, ids):
    for i, x in enumerate(ids):
        groups[x].append(i)

class scc_graph:
    def __init__(self, N):
        self.N = N
        self.edges = make_edges()

    def add_edge(self, v, w):
        add_to_edges(self.edges, v, w)

    def scc_ids(self):
        g = csr(self.N, self.edges)
        now_ord, group_num = 0, 0
        visited = deque()
        low = make_array(self.N)
        order = make_order_array(self.N)
        ids = make_array(self.N)
        parent = make_parent_array(self.N)
        for i in range(self.N):
            if order[i] == -1:
                stack = dfs_stack_start(i)
                while stack_not_empty(stack):
                    v = pop_stack(stack)
                    if order[v] == -1:
                        update_low_order(v, now_ord, low, order)
                        now_ord += 1
                        append_visited(visited, v)
                        for idx in edges_in_range(g.start[v], g.start[v + 1]):
                            to = get_next_to(g, v, idx)
                            if order[to] == -1:
                                stack_push_to(stack, to)
                                set_parent(parent, to, v)
                            else:
                                update_low_from_order(low, v, order, to)
                    else:
                        if low_eq_order(low, v, order):
                            while True:
                                u = scc_pop_visited(visited)
                                mark_as_visited(order, u, self.N)
                                assign_group(ids, u, group_num)
                                if found_main_node(u, v):
                                    break
                            group_num = incr_group_num(group_num)
                        update_parent_low(parent, v, low)
        finalize_ids(ids, group_num)
        return group_num, ids

    def scc(self):
        group_num, ids = self.scc_ids()
        groups = make_groups(group_num)
        fill_groups(groups, ids)
        return groups

def read_stdin_ints():
    return list(map(int, sys.stdin.buffer.read().split()))

def read_stdin_split():
    return sys.stdin.buffer.readline().split()

def range_input_edges(ab):
    it = iter(ab)
    return zip(it, it)

def print_group(group):
    print(*([len(group)] + group))

def main():
    readline = sys.stdin.buffer.readline
    N, M = map(int, readline().split())
    ab = read_stdin_ints()
    sg = scc_graph(N)
    for a, b in range_input_edges(ab):
        sg.add_edge(a, b)
    scc = sg.scc()
    print(len(scc))
    for group in scc:
        print_group(group)

if __name__ == "__main__":
    main()