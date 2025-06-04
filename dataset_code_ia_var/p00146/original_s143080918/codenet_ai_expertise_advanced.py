from collections import defaultdict
import sys
import heapq
from itertools import combinations

def calctime(w, dist):
    return dist * (70.0 + w) / 2000

def solve():
    dist = [[float('inf') if i == j else abs(d[i] - d[j]) for j in range(n)] for i in range(n)]

    total_states = 1 << n
    w = [float('inf')] * total_states
    time = [[float('inf')] * n for _ in range(total_states)]
    last = [[-1] * n for _ in range(total_states)]
    for i in range(n):
        mask = 1 << i
        time[mask][i] = 0
        w[mask] = v[i] * 20

    for mask in range(1, total_states):
        for last_node in range(n):
            if not (mask & (1 << last_node)) or time[mask][last_node] == float('inf'):
                continue
            curr_w = w[mask]
            for next_node in range(n):
                if mask & (1 << next_node):
                    continue
                next_mask = mask | (1 << next_node)
                next_w = curr_w + v[next_node] * 20
                t = time[mask][last_node] + calctime(curr_w, dist[last_node][next_node])
                if t < time[next_mask][next_node]:
                    w[next_mask] = next_w
                    time[next_mask][next_node] = t
                    last[next_mask][next_node] = last_node

    final_mask = total_states - 1
    min_time, last_node = min((time[final_mask][i], i) for i in range(n))
    ans = []
    mask = final_mask
    while mask:
        ans.append(s[last_node])
        prev = last[mask][last_node]
        mask ^= 1 << last_node
        last_node = prev
    ans.reverse()
    return ans

input = sys.stdin.readline
n = int(input())
s, d, v = {}, {}, {}
for i in range(n):
    S, D, V = map(int, input().split())
    s[i], d[i], v[i] = S, D, V

ans = solve()
print(' '.join(map(str, ans)))