from collections import deque

def initialize_start_queue(n, indeg):
    start = deque()
    for i in xrange(n):
        if indeg[i] == 0:
            start.append(i)
    return start

def update_start_queue_for_node(j, indeg, start):
    indeg[j] -= 1
    if indeg[j] == 0:
        start.append(j)
        return 1
    return 0

def process_neighbors(i, g, indeg, start):
    tmp = 0
    for j in g[i]:
        tmp += update_start_queue_for_node(j, indeg, start)
    return tmp

def append_to_answer(i, ans):
    ans.append(i)

def update_count(cnt, tmp):
    return max(cnt, cnt*tmp)

def perform_topo_sort_iteration(start, g, indeg, ans, cnt):
    i = start.popleft()
    append_to_answer(i, ans)
    tmp = process_neighbors(i, g, indeg, start)
    cnt = update_count(cnt, tmp)
    return cnt

def TopoSort_cnt(n, cnt, g, indeg, ans):
    start = initialize_start_queue(n, indeg)
    cnt += len(start)
    while len(start) > 0:
        cnt = perform_topo_sort_iteration(start, g, indeg, ans, cnt)
    return ans, cnt

def read_edge():
    wt, lt = map(int, raw_input().split())
    wt -= 1
    lt -= 1
    return wt, lt

def add_edge(wt, lt, g, indeg):
    g[wt].append(lt)
    indeg[lt] += 1

def read_and_build_graph(m, g, indeg):
    for _ in xrange(m):
        wt, lt = read_edge()
        add_edge(wt, lt, g, indeg)

def print_result(ans, n, flag):
    for i in xrange(n):
        print(ans[i] + 1)
    print(flag)

def solve(n, m, g, indeg, ans):
    read_and_build_graph(m, g, indeg)
    ans, cnt = TopoSort_cnt(n, 0, g, indeg, ans)
    if cnt > 1:
        print_result(ans, n, 1)
    else:
        print_result(ans, n, 0)

n = int(raw_input())
m = int(raw_input())
indeg = [0] * n
g = [[] for _ in xrange(n)]
ans = []

solve(n, m, g, indeg, ans)