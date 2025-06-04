import sys
from random import randint
from numpy import argmin
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall
input = sys.stdin.buffer.readline

problem_b = True

V, E = map(int, input().split())

v_from = []
v_to = []
cost = []

for _ in range(E):
    u, v, d = map(int, input().split())
    v_from.append(u)
    v_to.append(v)
    cost.append(d)

graph = csr_matrix((cost, (v_from, v_to)), [V+1, V+1])
dist, predecessors = floyd_warshall(graph, directed=False, return_predecessors=True)
dist[dist == 0] = float('inf')

dist_min = list(map(argmin, dist))

if problem_b:
    input()

T_max = int(input())

time = 0
delivering = False
returning = False
last_return_time = 0
distination = 1
v_next = 1

order = []
end_order = set()

n = int(input())
t = [int(input().split()[1]) for _ in range(n)]
order.append(t)
if problem_b:
    [input() for _ in range(int(input()))]

while time < T_max:
    if delivering:
        print(v_next, flush=True)
        if problem_b:
            input()
            [input() for _ in range(int(input()))]
        remaining_next -= 1
        if remaining_next == 0:
            if v_next == 1:
                last_return_time = max(last_return_time,  time - randint(0, 200))
            end_order.add(v_next)
            next_temp = predecessors[distination, v_next]
            if next_temp != -9999:
                remaining_next = dist[v_next, next_temp]
                v_next = next_temp
        remaining_last -= 1
        if remaining_last == 0:
            if distination == 1:
                returning = False
                delivering = False
            elif not returning:
                idx = jdx = -1
                dist_temp_min_possession = 10**18
                dist_temp_min_not_possession = 10**18
                for i, o in enumerate(order):
                    if not o:
                        continue
                    if i <= last_return_time:
                        for j, dst in enumerate(o):
                            if dst in end_order:
                                o[j] = 0
                            else:
                                dist_temp = dist[v_next, dst]
                                if dist_temp < dist_temp_min_possession:
                                    dist_temp_min_possession = dist_temp
                                    idx = i
                                    jdx = j
                end_order = set()
                if dist_temp_min_possession < dist_temp_min_not_possession:
                    distination = order[idx].pop(jdx)
                    remaining_last = dist[v_next, distination]
                    next_temp = predecessors[distination, v_next]
                    remaining_next = dist[v_next, next_temp]
                    v_next = next_temp
                else:
                    returning = True
                    remaining_last = dist[distination, 1]
                    v_next = predecessors[1, distination]
                    remaining_next = dist[distination, v_next]
                    distination = 1
            time += 1
            if time < T_max:
                n = int(input())
                t = [int(input().split()[1]) for _ in range(n)]
                order.append(t)
                if problem_b:
                    [input() for _ in range(int(input()))]
        else:
            time += 1
            if time < T_max:
                n = int(input())
                t = [int(input().split()[1]) for _ in range(n)]
                order.append(t)
                if problem_b:
                    [input() for _ in range(int(input()))]
    else:
        last_return_time = time
        idx = jdx = -1
        remaining_last = 0
        dist_temp_min = 10**18
        for i, o in enumerate(order):
            if not o:
                continue
            for j, dst in enumerate(o):
                dist_temp = dist[1, dst] + abs(time - i) ** 2
                if dist_temp < dist_temp_min:
                    dist_temp_min = dist_temp
                    idx = i
                    jdx = j
        if idx == -1:
            print(-1, flush=True)
            if problem_b:
                input()
                [input() for _ in range(int(input()))]
            time += 1
            if time < T_max:
                n = int(input())
                t = [int(input().split()[1]) for _ in range(n)]
                order.append(t)
                if problem_b:
                    [input() for _ in range(int(input()))]
            continue
        distination = order[idx].pop(jdx)
        remaining_last = dist[1, distination]
        v_next = predecessors[distination, 1]
        remaining_next = dist[1, v_next]
        delivering = True