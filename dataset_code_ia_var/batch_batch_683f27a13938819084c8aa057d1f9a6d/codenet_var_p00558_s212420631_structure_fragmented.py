from heapq import heappush, heappop

INF = 10 ** 20

def read_initial_values():
    n, m, x = map(int, input().split())
    return n, m, x

def read_temperature_list(n):
    return [int(input()) for _ in range(n)]

def init_edges(n):
    return [[] for _ in range(n)]

def read_edges(m, edges):
    for _ in range(m):
        a, b, d = map(int, input().split())
        a -= 1
        b -= 1
        add_edge(edges, a, b, d)

def add_edge(edges, a, b, d):
    edges[a].append((b, d))
    edges[b].append((a, d))

def init_queue(x):
    return [(0, x, 0, 0)]

def push_to_queue(que, item):
    heappush(que, item)

def pop_from_queue(que):
    return heappop(que)

def init_dic(x):
    return {(x, 0, 0): 0}

def update_dic(dic, new_ct, new_ht, to, new_total):
    dic[(new_ct, new_ht, to)] = new_total

def in_dic(dic, new_ct, new_ht, to):
    return (new_ct, new_ht, to) in dic

def get_dic_value(dic, new_ct, new_ht, to):
    return dic[(new_ct, new_ht, to)]

def valid_next(t, new_ct, new_ht):
    return t == 1 or (t == 0 and new_ht == 0) or (t == 2 and new_ct == 0)

def update_temperatures(t, x, new_ct, new_ht):
    if t == 0:
        new_ct = x
    if t == 2:
        new_ht = x
    return new_ct, new_ht

def expand_node(edges, tlst, x, que, dic):
    while que:
        total, ct, ht, node = pop_from_queue(que)
        for to, dist in edges[node]:
            new_ct = max(0, ct - dist)
            new_ht = max(0, ht - dist)
            t = tlst[to]
            if valid_next(t, new_ct, new_ht):
                new_total = total + dist
                updated_ct, updated_ht = update_temperatures(t, x, new_ct, new_ht)
                if (not in_dic(dic, updated_ct, updated_ht, to)) or (get_dic_value(dic, updated_ct, updated_ht, to) > new_total):
                    update_dic(dic, updated_ct, updated_ht, to, new_total)
                    push_to_queue(que, (new_total, updated_ct, updated_ht, to))

def find_minimum(dic, n, x):
    candidates = []
    for ct in range(x + 1):
        for ht in range(x + 1):
            if (ct, ht, n - 1) in dic:
                candidates.append(dic[(ct, ht, n - 1)])
            else:
                candidates.append(INF)
    return min(candidates)

def main():
    n, m, x = read_initial_values()
    tlst = read_temperature_list(n)
    edges = init_edges(n)
    read_edges(m, edges)
    que = []
    push_to_queue(que, (0, x, 0, 0))
    dic = init_dic(x)
    expand_node(edges, tlst, x, que, dic)
    answer = find_minimum(dic, n, x)
    print(answer)

main()