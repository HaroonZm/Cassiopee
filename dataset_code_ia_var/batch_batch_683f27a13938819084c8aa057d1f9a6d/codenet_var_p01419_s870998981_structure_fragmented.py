from collections import deque
import itertools as it
import sys

def set_recursion_limit():
    sys.setrecursionlimit(1000000)

def read_inputs():
    R, C, M = map(int, raw_input().split())
    S = read_grid(R)
    t_cost = read_costs(R)
    on_cost = read_costs(R)
    off_cost = read_costs(R)
    return R, C, M, S, t_cost, on_cost, off_cost

def read_grid(R):
    return [raw_input() for _ in range(R)]

def read_costs(R):
    return [map(int, raw_input().split()) for _ in range(R)]

def initialize_m(R, C):
    m = {}
    for y in range(R):
        for x in range(C):
            m[(x, y)] = []
    return m

def is_out_of_bounds(x, y, C, R):
    return x < 0 or y < 0 or x >= C or y >= R

def is_visited(used, x, y):
    return (x, y) in used

def is_wall(S, x, y):
    return S[y][x] == '#'

def is_goal(x, y, gx, gy):
    return x == gx and y == gy

def append_to_path_matrix(m, x, y, step):
    m[(x, y)].append(step)

def dfs_step(m, S, used, x, y, gx, gy, step, C, R):
    if is_out_of_bounds(x, y, C, R):
        return False
    if is_visited(used, x, y):
        return False
    used[(x, y)] = step
    if is_wall(S, x, y):
        return False
    if is_goal(x, y, gx, gy):
        append_to_path_matrix(m, x, y, step)
        return True
    ret = False
    ret = (ret or dfs_step(m, S, used, x-1, y, gx, gy, step+1, C, R))
    ret = (ret or dfs_step(m, S, used, x+1, y, gx, gy, step+1, C, R))
    ret = (ret or dfs_step(m, S, used, x, y-1, gx, gy, step+1, C, R))
    ret = (ret or dfs_step(m, S, used, x, y+1, gx, gy, step+1, C, R))
    if ret:
        append_to_path_matrix(m, x, y, step)
    return ret

def read_start_pos():
    sy, sx = map(int, raw_input().split())
    return sy, sx

def read_goal_pos():
    gy, gx = map(int, raw_input().split())
    return gy, gx

def update_route(M, sy, sx, m, S, R, C):
    cnt = 0
    last_gx = last_gy = None
    for loop in range(M - 1):
        gy, gx = read_goal_pos()
        used = {}
        dfs_step(m, S, used, sx, sy, gx, gy, cnt, C, R)
        cnt = m[(gx, gy)].pop()
        sx, sy = gx, gy
        last_gx = gx
        last_gy = gy
    if last_gx is not None and last_gy is not None:
        m[(last_gx, last_gy)].append(cnt)
    return m

def cost_onoff(ans, lst, on, off):
    if len(lst) > 0:
        ans += on + off
    return ans

def cost_path_steps(ans, lst, t, on, off):
    for i in range(len(lst) - 1):
        t1 = lst[i]
        t2 = lst[i + 1]
        ans += min(on + off, t * (t2 - t1))
    return ans

def compute_total_cost(R, C, t_cost, on_cost, off_cost, m):
    ans = 0
    for y in range(R):
        for x in range(C):
            t = t_cost[y][x]
            on = on_cost[y][x]
            off = off_cost[y][x]
            lst = m[(x, y)]
            ans = cost_onoff(ans, lst, on, off)
            ans = cost_path_steps(ans, lst, t, on, off)
    return ans

def main():
    set_recursion_limit()
    R, C, M, S, t_cost, on_cost, off_cost = read_inputs()
    m = initialize_m(R, C)
    sy, sx = read_start_pos()
    m = process_all_goals(M, sy, sx, m, S, R, C)
    ans = compute_total_cost(R, C, t_cost, on_cost, off_cost, m)
    print ans

def process_all_goals(M, sy, sx, m, S, R, C):
    cnt = 0
    current_sx, current_sy = sx, sy
    last_gx = last_gy = None
    for loop in range(M - 1):
        gy, gx = read_goal_pos()
        used = {}
        dfs_step(m, S, used, current_sx, current_sy, gx, gy, cnt, C, R)
        cnt = m[(gx, gy)].pop()
        current_sx, current_sy = gx, gy
        last_gx = gx
        last_gy = gy
    if last_gx is not None and last_gy is not None:
        m[(last_gx, last_gy)].append(cnt)
    return m

main()