def read_int():
    return int(input())

def read_int_list():
    return list(map(int, input().split()))

def init_adj_list(n):
    return [read_int_list() for _ in range(n)]

def init_edge_matrix(n):
    return [[0 for _ in range(n)] for _ in range(n)]

def fill_edge(adj, n, edge):
    def connect_edges(i):
        connect_neighbors(i, adj[i], edge)
    for i in range(n):
        connect_edges(i)

def connect_neighbors(i, info, edge):
    count = info[1]
    for j in range(count):
        connect_neighbor(i, info[j+2], edge)

def connect_neighbor(i, neighbor, edge):
    edge[i][neighbor-1] = 1

def init_time():
    return 1

def init_discover_final(n):
    return [0 for _ in range(n)], [0 for _ in range(n)]

def init_stack():
    return []

def set_discover(discover, idx, time):
    discover[idx] = time

def append_stack(stack, idx):
    stack.append(idx)

def dfs(n, edge, discover, final, stack, id, time):
    process_neighbors_dfs(n, edge, discover, final, stack, id, time)

def process_neighbors_dfs(n, edge, discover, final, stack, id, time):
    i = 0
    found = False
    while i < n:
        process_single_neighbor(i, id, edge, discover, final, stack, time, n, found)
        if edge[id][i] == 1 and discover[i] == 0:
            found = True
        i += 1
    if not found:
        handle_backtracking(stack, final, id, discover, n, edge, time)

def process_single_neighbor(i, id, edge, discover, final, stack, time, n, found):
    if edge[id][i] == 1 and discover[i] == 0:
        append_stack(stack, id)
        set_discover(discover, i, time)
        dfs(n, edge, discover, final, stack, i, time+1)

def handle_backtracking(stack, final, id, discover, n, edge, time):
    if len(stack) > 0:
        handle_stack_nonempty(stack, final, id, discover, n, edge, time)

def handle_stack_nonempty(stack, final, id, discover, n, edge, time):
    if final[id] == 0:
        final[id] = time
        dfs(n, edge, discover, final, stack, stack.pop(), time+1)
    else:
        dfs(n, edge, discover, final, stack, stack.pop(), time)

def handle_unvisited(n, discover, final, stack, edge):
    for i in range(n):
        if discover[i] == 0:
            discover[i] = final[0] + 1
            append_stack(stack, i)
            dfs(n, edge, discover, final, stack, i, final[0] + 2)
            break

def output_results(n, discover, final):
    for i in range(n):
        print(i+1, discover[i], final[i])

def main():
    n = read_int()
    adj = init_adj_list(n)
    edge = init_edge_matrix(n)
    fill_edge(adj, n, edge)
    time = init_time()
    discover, final = init_discover_final(n)
    stack = init_stack()
    set_discover(discover, 0, time)
    append_stack(stack, 0)
    dfs(n, edge, discover, final, stack, 0, time+1)
    handle_unvisited(n, discover, final, stack, edge)
    output_results(n, discover, final)

main()