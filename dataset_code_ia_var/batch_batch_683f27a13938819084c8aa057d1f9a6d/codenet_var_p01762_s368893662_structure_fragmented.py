def read_n():
    return int(input())

def read_c_list(n):
    c_str = input().split()
    c_values = list(map(int, c_str))
    return [0] + c_values

def init_edges(n):
    return [[] for _ in range(n)]

def read_edges(n, edges):
    for _ in range(n - 1):
        u, v, p = map(int, input().split())
        add_edge(edges, u, v, p)

def add_edge(edges, u, v, p):
    edges[u].append((v, p))
    edges[v].append((u, p))

def get_inf():
    return 10 ** 20

def init_used(n):
    return [False] * n

def set_used(used, x):
    used[x] = True

def get_pre_cost(x):
    return 0 if x != 0 else get_inf()

def loop_edges(x, edges, used, c_lst):
    ret = 0
    pre_cost = get_pre_cost(x)
    for to, p in get_edges_for_node(edges, x):
        if is_used(used, to):
            pre_cost = p
        else:
            ret += cost(to, edges, used, c_lst)
    return ret, pre_cost

def get_edges_for_node(edges, x):
    return edges[x]

def is_used(used, x):
    return used[x]

def do_return(c_lst, x, ret, pre_cost):
    if c_lst[x] == 0:
        return min(ret, pre_cost)
    else:
        return pre_cost

def cost(x, edges, used, c_lst):
    set_used(used, x)
    ret, pre_cost = loop_edges(x, edges, used, c_lst)
    return do_return(c_lst, x, ret, pre_cost)

def main():
    n = read_n()
    c_lst = read_c_list(n)
    edges = init_edges(n)
    read_edges(n, edges)
    INF = get_inf()
    used = init_used(n)
    print(cost(0, edges, used, c_lst))

main()