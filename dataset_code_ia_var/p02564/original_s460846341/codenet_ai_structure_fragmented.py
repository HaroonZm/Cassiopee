def init_start(n, edges):
    start = [0] * (n + 1)
    for e in edges:
        increment_start_entry(start, e)
    return start

def increment_start_entry(start, e):
    start[e[0] + 1] += 1

def accumulate_start(start, n):
    for i in range(1, n + 1):
        start[i] += start[i - 1]
    return start

def init_elist(edges):
    return [0] * len(edges)

def copy_list(lst):
    return lst[:]

def fill_elist_and_counter(edges, start):
    elist = init_elist(edges)
    counter = copy_list(start)
    for e in edges:
        elist[counter[e[0]]] = e[1]
        counter[e[0]] += 1
    return elist

class CSR:
    def __init__(self, n: int, edges: list):
        self.start = build_start(n, edges)
        self.elist = fill_elist_and_counter(edges, self.start)

def build_start(n, edges):
    start = init_start(n, edges)
    start = accumulate_start(start, n)
    return start

def create_empty_list(size, value):
    return [value] * size

def is_node_unvisited(order, node):
    return order[node] == -1

def all_nodes(n):
    return range(n)

def create_stack(root):
    return [root, root]

def visit_node(visited, low, order, now_ord, v):
    visited.append(v)
    low[v] = order[v] = now_ord
    now_ord += 1
    return now_ord

def process_child_node(stack, parent, t, v):
    stack += [t, t]
    parent[t] = v

def update_low_edges(low, v, order, t):
    low[v] = min(low[v], order[t])

def update_low_parent(low, parent, v):
    low[parent[v]] = min(low[parent[v]], low[v])

def handle_scc_group(visited, order, ids, group_num, n, v):
    while True:
        u = visited.pop()
        order[u] = n
        ids[u] = group_num
        if u == v:
            break
    return group_num + 1

def finalize_ids(ids, group_num):
    for i, x in enumerate(ids):
        ids[i] = group_num - 1 - x
    return ids

def count_groups(group_num, ids):
    counts = [0] * group_num
    for x in ids:
        counts[x] += 1
    return counts

def build_groups(group_num, ids):
    groups = [[] for _ in range(group_num)]
    for i, x in enumerate(ids):
        groups[x].append(i)
    return groups

class SccGraph:
    def __init__(self, n: int = 0):
        self.__n = n
        self.__edges = []
    
    def __len__(self):
        return self.__n
    
    def add_edge(self, s: int, t: int):
        assert_edge_in_bounds(self.__n, s, t)
        self.__edges.append([s, t])
    
    def __scc_ids(self):
        g = CSR(self.__n, self.__edges)
        now_ord, group_num = 0, 0
        visited = []
        low = create_empty_list(self.__n, 0)
        order = create_empty_list(self.__n, -1)
        ids = create_empty_list(self.__n, 0)
        parent = create_empty_list(self.__n, -1)
        for root in all_nodes(self.__n):
            if is_node_unvisited(order, root):
                stack = create_stack(root)
                while stack:
                    v = stack.pop()
                    if is_node_unvisited(order, v):
                        now_ord = visit_node(visited, low, order, now_ord, v)
                        for i in range(g.start[v], g.start[v+1]):
                            t = g.elist[i]
                            if is_node_unvisited(order, t):
                                process_child_node(stack, parent, t, v)
                            else:
                                update_low_edges(low, v, order, t)
                    else:
                        if low[v] == order[v]:
                            group_num = handle_scc_group(visited, order, ids, group_num, self.__n, v)
                        if parent[v] != -1:
                            update_low_parent(low, parent, v)
        ids = finalize_ids(ids, group_num)
        return group_num, ids
    
    def scc(self):
        group_num, ids = self.__scc_ids()
        count_groups(group_num, ids) # not used further
        groups = build_groups(group_num, ids)
        return groups

def assert_edge_in_bounds(n, s, t):
    assert 0 <= s < n and 0 <= t < n

def parse_input():
    return map(int, input().split())

def read_edges(M):
    edges = []
    for _ in range(M):
        a, b = parse_input()
        edges.append((a, b))
    return edges

def add_edges_to_sccgraph(sg, M):
    for _ in range(M):
        a, b = parse_input()
        sg.add_edge(a, b)

def print_scc_groups(scc):
    print(len(scc))
    for group in scc:
        print(*([len(group)] + group))

def main():
    N, M = parse_input()
    sg = SccGraph(N)
    add_edges_to_sccgraph(sg, M)
    scc = sg.scc()
    print_scc_groups(scc)

main()