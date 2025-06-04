import sys

def read_input():
    return sys.stdin.buffer.readline

def parse_first_line(input_func):
    N, M = map(int, input_func().split())
    return N, M

def create_adjacency_list(N):
    return [[] for _ in range(N+1)]

def add_edge(adj, a, b):
    adj[a].append(b)
    adj[b].append(a)

def fill_edges(adj, M, input_func):
    for _ in range(M):
        a, b = map(int, input_func().split())
        add_edge(adj, a, b)

def calculate_degrees(adj):
    return [len(A) for A in adj]

def collect_deg4_and_detect_odd(deg, N):
    nodes_deg4 = []
    found_odd = False
    for i in range(1, N+1):
        if deg[i] % 2 == 1:
            return 'odd', None
        elif deg[i] == 4:
            nodes_deg4.append(i)
    return 'ok', nodes_deg4

def check_deg6(deg, N):
    for i in range(1, N+1):
        if deg[i] >= 6:
            return True
    return False

def check_easy_yes(nodes_deg4):
    if len(nodes_deg4) >= 3:
        return True
    return False

def check_easy_no(nodes_deg4):
    if len(nodes_deg4) <= 1:
        return True
    return False

def setup_seen(N, t1, t2):
    seen = [0] * (N+1)
    seen[t1] = 1
    seen[t2] = 1
    return seen

def dfs_from(adj, N, t1, t2):
    seen = setup_seen(N, t1, t2)
    stack = [t1]
    while stack:
        v = stack.pop()
        for u in adj[v]:
            if seen[u] == 0:
                seen[u] = 1
                stack.append(u)
    return seen

def decide_by_seen(seen, N):
    if sum(seen) != N:
        print('Yes')
    else:
        print('No')

def early_exit(result):
    print(result)
    exit()

def main():
    input_func = read_input()
    N, M = parse_first_line(input_func)
    adj = create_adjacency_list(N)
    fill_edges(adj, M, input_func)
    deg = calculate_degrees(adj)
    status, nodes_deg4 = collect_deg4_and_detect_odd(deg, N)
    if status == 'odd':
        early_exit('No')
    if check_deg6(deg, N):
        early_exit('Yes')
    if check_easy_yes(nodes_deg4):
        early_exit('Yes')
    if check_easy_no(nodes_deg4):
        early_exit('No')
    t1, t2 = nodes_deg4[0], nodes_deg4[1]
    seen = dfs_from(adj, N, t1, t2)
    decide_by_seen(seen, N)

main()