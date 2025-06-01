from collections import deque

def initialize_start_queue(v, indeg):
    start = deque()
    for i in range(v):
        if indeg[i] == 0:
            start.append(i)
    return start

def check_multiple_start(start):
    if len(start) > 1:
        return True
    return False

def decrement_indegree_for_node(j, indeg):
    indeg[j] -= 1
    return indeg[j]

def process_neighbors(i, g, indeg, start):
    tmp = []
    for j in g[i]:
        current_indeg = decrement_indegree_for_node(j, indeg)
        if current_indeg == 0:
            tmp.append(j)
            start.append(j)
    return tmp

def check_multiple_new_starts(tmp):
    if len(tmp) > 1:
        return True
    return False

def process_node(i, ans, g, indeg, start, flag):
    ans.append(i)
    tmp = process_neighbors(i, g, indeg, start)
    if check_multiple_new_starts(tmp):
        flag = True
    return flag

def topological_sort(v, g, indeg):
    start = initialize_start_queue(v, indeg)
    flag = check_multiple_start(start)
    ans = []
    while len(start) > 0:
        i = start.popleft()
        flag = process_node(i, ans, g, indeg, start, flag)
    return ans, flag

def read_graph_edges(m, g, indeg):
    for _ in range(m):
        wt, lt = map(int, input().split())
        wt -= 1
        lt -= 1
        g[wt].append(lt)
        indeg[lt] += 1

def solve(n, m, g, indeg):
    read_graph_edges(m, g, indeg)
    return topological_sort(n, g, indeg)

def print_result(ans, flag):
    for node in ans:
        print(node + 1)
    if flag:
        print(1)
    else:
        print(0)

def main():
    n = int(input())
    m = int(input())
    indeg = [0] * n
    g = [[] for _ in range(n)]
    ans, flag = solve(n, m, g, indeg)
    print_result(ans, flag)

main()