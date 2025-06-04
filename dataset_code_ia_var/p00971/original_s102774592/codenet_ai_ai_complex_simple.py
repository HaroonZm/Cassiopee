import array
import os
import sys
import itertools
import functools
import operator
import bisect
import heapq
import collections

def main():
    S = next_input()
    T = next_input()
    print(eccentric_solution(S, T))

def eccentric_solution(S, T):
    A, B = S, T

    nA, nB = len(A), len(B)

    create_table = lambda n: [[n+1]*(n+1) for _ in range(2)]
    next_pos_A = create_table(nA)
    next_pos_B = create_table(nB)

    # Fill next_pos_A
    for idx, c in enumerate(A):
        d = int(c)
        indices = range(idx, -1, -1)
        # Use all(), any(), genexp for side-effect
        any(next_pos_A[d][j] == nA+1 and not next_pos_A[d].__setitem__(j, idx+1) for j in indices)
    for idx, c in enumerate(B):
        d = int(c)
        indices = range(idx, -1, -1)
        any(next_pos_B[d][j] == nB+1 and not next_pos_B[d].__setitem__(j, idx+1) for j in indices)

    # Precompute all future positions with fancy defaultdicts and map
    pos_dict = lambda n, nx: [
        [*map(lambda i: [], range(n+2))] for _ in range(2)
    ]
    fancy_listify = lambda seq, default: (seq if seq else [default])

    A_pos = [[[] for _ in range(nA+2)] for _ in range(2)]
    B_pos = [[[] for _ in range(nB+2)] for _ in range(2)]
    for b in (0,1):
        for i in range(nA+1):
            A_pos[b][next_pos_A[b][i]] += [i]
        A_pos[b][nA+1] += [nA+1]
    for b in (0,1):
        for i in range(nB+1):
            B_pos[b][next_pos_B[b][i]] += [i]
        B_pos[b][nB+1] += [nB+1]

    INF = max(nA,nB)+2
    # Use numpy-like indices via functools
    array_dist = [array.array('i', [INF]*(nB+2)) for _ in range(nA+2)]

    # Dijkstra-like search with set
    Q = {(nA+1, nB+1)}
    d = 0
    while Q:
        newQ = set()
        for (i,j) in Q:
            if array_dist[i][j] != INF:
                continue
            array_dist[i][j] = d
            for b in (0,1):
                for ni in A_pos[b][i]:  # could chain itertools.product, but keeping two loops
                    for nj in B_pos[b][j]:
                        if array_dist[ni][nj]==INF and (ni,nj) not in Q:
                            newQ.add((ni,nj))
        d += 1
        Q = newQ

    # Rebuild answer using chain, generator, and more
    ans = []
    i, j = 0,0
    d = array_dist[0][0]
    stepper = lambda x: x if x < len(array_dist) else len(array_dist)-1
    while (i, j) != (nA+1, nB+1):
        ni, nj = (next_pos_A[0][i] if i < nA+1 else nA+1,
                  next_pos_B[0][j] if j < nB+1 else nB+1)
        if array_dist[ni][nj] == d-1:
            ans.append('0')
        else:
            ans.append('1')
            ni, nj = (next_pos_A[1][i] if i < nA+1 else nA+1,
                      next_pos_B[1][j] if j < nB+1 else nB+1)
        i = ni
        j = nj
        d -= 1

    return ''.join(ans)

###############################################################################
DEBUG = 'DEBUG' in os.environ

def next_input():
    # over-complicated input function, using __next__ and iter
    return next(iter(lambda: sys.stdin.readline().rstrip(), ''))

def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)

if __name__ == '__main__':
    main()