#!/usr/bin/env python3
# vim: set fileencoding=utf-8

# pylint: disable=unused-import, invalid-name, missing-docstring, bad-continuation

"""Module docstring
"""

import sys
from collections import defaultdict

sys.setrecursionlimit(pow(2, 31) - 1)

# from typing import Dict, List, Optional, Set, Tuple

# def dfs(vertex: int, succ: Dict[int, List[int]], dp: Dict[int, int]) -> int:
def dfs(vertex, succ, dp):
    if vertex in dp:
        return dp[vertex]
    length = 0
    for s in succ[vertex]:
        length = max(length, 1 + dfs(s, succ, dp))
    dp[vertex] = length
    return length

# def solve(values: List[int], nb_vertices: int, nb_edges: int) -> int:
def solve(values, _nb_vertices, _nb_edges) -> int:
    succ = defaultdict(list)
    for s, d in values:
        succ[s].append(d)
    # all edges have a 0 length path starting at the edge
    dp = defaultdict(lambda: -1)
    for vertex in frozenset(succ.keys()):
        if vertex in dp:
            dp[vertex] = max(dp[vertex], dfs(vertex, succ, dp))
        else:
            dp[vertex] = dfs(vertex, succ, dp)
    return max(dp.values())

def do_job():
    "Do the work"
    # first line is number of test cases
    N, M = map(int, input().split())
    values = []
    for _ in range(M):
        values.append(tuple(map(int, input().split())))
    result = solve(values, N, M)
    print(result)

if __name__ == "__main__":
    do_job()