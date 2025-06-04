from heapq import heappop as pop
from heapq import heappush as push

def read_initial_inputs():
    n, k = map(int, input().split())
    return n, k

def read_cost_and_range(n):
    clst = []
    rlst = []
    for _ in range(n):
        c, r = map(int, input().split())
        clst.append(c)
        rlst.append(r)
    return clst, rlst

def init_edges(n):
    return [[] for _ in range(n)]

def read_edges(k, edges):
    for _ in range(k):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        add_edge(edges, a, b)

def add_edge(edges, a, b):
    edges[a].append(b)
    edges[b].append(a)

def init_costs_and_used(n):
    return [None] * n, [False] * n

def make_to_lst(s_num, edges, rlst):
    loop = rlst[s_num]
    temp = set(edges[s_num])
    ret = set()
    while loop and temp:
        temp, ret = make_to_lst_inner(temp, ret, edges)
        loop -= 1
    return ret

def make_to_lst_inner(temp, ret, edges):
    new = set()
    for p in temp:
        pto = set(edges[p])
        new = new | pto
    ret = ret | temp
    return new - ret, ret

def init_start(used, costs, clst):
    used[0] = True
    costs[0] = 0
    return [(clst[0], 0)]

def check_goal_and_update(num, n, next_cost):
    if num == n - 1:
        print(next_cost)
        return True
    return False

def update_cost(costs, num, next_cost):
    costs[num] = next_cost

def add_to_queue(que, next_cost, clst, num):
    push(que, (next_cost + clst[num], num))

def mark_used(used, num):
    used[num] = True

def process_to_lst(to_lst, costs, used, que, clst, n, next_cost):
    for num in to_lst:
        if check_goal_and_update(num, n, next_cost):
            return True
        update_cost(costs, num, next_cost)
        if not used[num]:
            add_to_queue(que, next_cost, clst, num)
            mark_used(used, num)
    return False

def dijkstra(n, clst, rlst, edges):
    costs, used = init_costs_and_used(n)
    que = init_start(used, costs, clst)
    while que:
        next_cost, s_num = pop(que)
        to_lst = make_to_lst(s_num, edges, rlst)
        if process_to_lst(to_lst, costs, used, que, clst, n, next_cost):
            return

def main():
    n, k = read_initial_inputs()
    clst, rlst = read_cost_and_range(n)
    edges = init_edges(n)
    read_edges(k, edges)
    dijkstra(n, clst, rlst, edges)

main()