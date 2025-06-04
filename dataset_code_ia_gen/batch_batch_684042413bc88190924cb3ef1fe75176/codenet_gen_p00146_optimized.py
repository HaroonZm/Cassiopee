import sys
sys.setrecursionlimit(10**7)

n = int(sys.stdin.readline())
warehouses = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
# s_i: number, d_i: distance, v_i: boxes count

# Sort by distance ascending to fix start at nearest warehouse
warehouses.sort(key=lambda x: x[1])

dist = [w[1] for w in warehouses]
weights = [w[2]*20 for w in warehouses]
numbers = [w[0] for w in warehouses]

# Precompute speed function denominator
def speed(w):
    return 2000/(70+w)

# Precompute distance between warehouses along straight line
def dist_bw(i,j):
    return abs(dist[i]-dist[j])

from functools import lru_cache

full_mask = (1<<n)-1

@lru_cache(None)
def dp(mask,last):
    if mask == full_mask:
        return 0
    res = float('inf')
    w_sum = 0
    for i in range(n):
        if (mask>>i)&1:
            w_sum += weights[i]
    w_sum += weights[last] if last>=0 else 0  # hold last warehouse's boxes

    curr_weight = w_sum
    # If last == -1 means starting state before first warehouse
    start_pos = -1 if last<0 else last

    # If last == -1, we must choose first warehouse to visit
    for nxt in range(n):
        if (mask>>nxt)&1==0:
            # Moving from last to nxt
            from_pos = dist[last] if last>=0 else 0
            to_pos = dist[nxt]
            d_move = abs(to_pos - from_pos)
            speed_move = 2000/(70+curr_weight)
            t_move = d_move / speed_move

            # hacking time zero, just add t_move + recursive dp
            new_mask = mask | (1<<nxt)
            cost = t_move + dp(new_mask,nxt)
            if cost < res:
                res = cost
    return res

# We want to find path: so store route
from math import inf

@lru_cache(None)
def dp_with_path(mask,last):
    if mask == full_mask:
        return 0, []
    res = inf
    path = []
    w_sum = 0
    for i in range(n):
        if (mask>>i)&1:
            w_sum += weights[i]
    w_sum += weights[last] if last>=0 else 0
    curr_weight= w_sum
    for nxt in range(n):
        if (mask>>nxt)&1==0:
            from_pos = dist[last] if last>=0 else 0
            to_pos = dist[nxt]
            d_move = abs(to_pos - from_pos)
            speed_move = 2000/(70+curr_weight)
            t_move = d_move / speed_move
            new_mask = mask | (1<<nxt)
            cost_next, path_next = dp_with_path(new_mask, nxt)
            cost = t_move + cost_next
            if cost < res:
                res = cost
                path = [nxt] + path_next
    return res, path

_, best_path = dp_with_path(0, -1)
print(' '.join(str(numbers[i]) for i in best_path))