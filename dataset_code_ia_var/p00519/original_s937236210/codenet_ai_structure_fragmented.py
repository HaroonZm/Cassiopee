from heapq import heappop as pop
from heapq import heappush as push
INF = 10 ** 20

def read_input():
    n, k = parse_n_and_k()
    clst, rlst = read_clst_rlst(n)
    edges = build_edges(n, k)
    return n, k, clst, rlst, edges

def parse_n_and_k():
    n, k = map(int, input().split())
    return n, k

def read_clst_rlst(n):
    clst = []
    rlst = []
    for _ in range(n):
        c, r = read_c_r()
        clst.append(c)
        rlst.append(r)
    return clst, rlst

def read_c_r():
    return map(int, input().split())

def build_edges(n, k):
    edges = [[] for _ in range(n)]
    for _ in range(k):
        a, b = read_pair()
        add_edge(edges, a, b)
    return edges

def read_pair():
    a, b = map(int, input().split())
    return a-1, b-1

def add_edge(edges, a, b):
    edges[a].append(b)
    edges[b].append(a)

def initial_costs(n):
    return [0 if i == 0 else INF for i in range(n)]

def initial_used(n):
    return [True if i==0 else False for i in range(n)]

def make_to_lst(s_num, edges, rlst):
    loop = rlst[s_num]
    temp = set(edges[s_num])
    ret = set()
    while keep_loop(loop, temp):
        new = gather_next(temp, edges)
        ret = ret | temp
        temp = compute_temp(new, ret)
        loop -= 1
    return ret

def keep_loop(loop, temp):
    return loop and temp

def gather_next(temp, edges):
    new = set()
    for p in temp:
        pto = set(edges[p])
        new |= pto
    return new

def compute_temp(new, ret):
    return new - ret

def initialize_queue(clst):
    return [(clst[0], 0)]

def search(n, clst, rlst, edges):
    costs = initial_costs(n)
    used = initial_used(n)
    que = initialize_queue(clst)
    break_flag = [False]
    while que and not break_flag[0]:
        process_queue(que, costs, used, clst, rlst, edges, n, break_flag)
    return costs

def process_queue(que, costs, used, clst, rlst, edges, n, break_flag):
    next_cost, s_num = pop(que)
    to_lst = make_to_lst(s_num, edges, rlst)
    for num in to_lst:
        update_costs(costs, num, next_cost)
        if is_goal(num, n):
            set_break_flag(break_flag)
            break
        if not used[num]:
            schedule(que, costs, clst, num)
            mark_used(used, num)

def update_costs(costs, num, next_cost):
    costs[num] = next_cost

def is_goal(num, n):
    return num == n - 1

def set_break_flag(break_flag):
    break_flag[0] = True

def schedule(que, costs, clst, num):
    push(que, (costs[num] + clst[num], num))

def mark_used(used, num):
    used[num] = True

def print_result(costs, n):
    print(costs[n - 1])

def main():
    n, k, clst, rlst, edges = read_input()
    costs = search(n, clst, rlst, edges)
    print_result(costs, n)

main()