import sys
from random import randint as _randint
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall

input = sys.stdin.buffer.readline

# 問題AとB両方同じコードだと嬉しいね
PROBLEM_B = True

def parse_graph():
    V, E = map(int, input().split())
    src = []; dst = []; weights = []
    for __ in range(E):
        usp = list(map(int, input().split()))
        src.append(usp[0]); dst.append(usp[1]); weights.append(usp[2])
    return V, E, src, dst, weights

V, E, v_from, v_to, cost = parse_graph()
graph = csr_matrix((cost, (v_from, v_to)), shape=(V+1, V+1))
_dist, _pred = floyd_warshall(csgraph=graph, directed=False, return_predecessors=True)
_dist[_dist == 0] = float('inf')
min_nodes = [np.argmin(row) for row in _dist]

if PROBLEM_B:
    input()
T_MAX = int(input())

T = 0; delivering = 0; returning = None
last_return = 0
destination, vnext = 1, 1
all_orders = []
delivered_here = set()
def order_in():
    nonlocal_orders = globals().get('all_orders', [])
    count = int(input())
    xs = []
    for _ in range(count):
        xs.append(int(input().split()[1]))
    nonlocal_orders.append(xs)
    if PROBLEM_B:
        [input() for _ in range(int(input()))]
    globals()['all_orders'] = nonlocal_orders

def step_time():
    global T
    T += 1
    if T < T_MAX:
        order_in()

def PF(x):
    print(x, flush=True)
    if PROBLEM_B:
        input()
        [input() for _ in range(int(input()))]

order_in()

while T < T_MAX:
    # State: delivering
    if delivering:
        PF(vnext)
        remaining_next -= 1
        if remaining_next == 0:
            if vnext == 1:
                last_return = max(last_return, T - _randint(0,200))
            delivered_here.add(vnext)
            tmp = _pred[destination, vnext]
            if tmp != -9999:
                remaining_next = _dist[vnext, tmp]
                vnext = tmp
        remaining_last -= 1
        if remaining_last == 0:
            if destination == 1:
                returning = False
                delivering = False
            elif not returning:
                i_j = [-1, -1]; mn1, mn2 = 10**18, 10**18
                idx, jdx = i_j
                for i, O in enumerate(all_orders):
                    if not O:
                        continue
                    if i <= last_return:
                        for j, d in enumerate(O):
                            if d in delivered_here:
                                O[j] = 0
                            else:
                                dval = _dist[vnext, d]
                                if dval < mn1:
                                    mn1, idx, jdx = dval, i, j
                delivered_here = set()
                if mn1 < mn2:
                    destination = all_orders[idx].pop(jdx)
                    remaining_last = _dist[vnext, destination]
                    tmp = _pred[destination, vnext]
                    remaining_next = _dist[vnext, tmp]
                    vnext = tmp
                else:
                    returning = True
                    remaining_last = _dist[destination, 1]
                    vnext = _pred[1, destination]
                    remaining_next = _dist[destination, vnext]
                    destination = 1
            step_time()
        else:
            step_time()
    # State: idle
    else:
        last_return = T
        idx = jdx = -1
        remaining_last = 0
        dmin = 10**18
        for i, lst in enumerate(all_orders):
            if not lst:
                continue
            for j, u in enumerate(lst):
                val = _dist[1, u] + abs(T-i)**2
                if val < dmin:
                    dmin=val
                    idx, jdx = i, j
        if idx == -1:
            PF(-1)
            step_time()
            continue
        destination = all_orders[idx].pop(jdx)
        remaining_last = _dist[1, destination]
        vnext = _pred[destination, 1]
        remaining_next = _dist[1, vnext]
        delivering = True