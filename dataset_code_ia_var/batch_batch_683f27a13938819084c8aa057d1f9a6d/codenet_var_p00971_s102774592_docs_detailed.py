#!/usr/bin/python3

import array
import os
import sys

def main():
    """
    Entry point of the script.
    Reads two strings S and T from input, and prints the result of solve(S, T).
    """
    S = inp()
    T = inp()
    print(solve(S, T))

def solve(S, T):
    """
    Given two binary strings S and T, finds the shortest string X containing both S and T as subsequences,
    such that every substring of X of length equal to |X| - |S| - |T| + 2 contains at least one '0' and one '1'.
    
    Arguments:
    S -- The first input binary string.
    T -- The second input binary string.

    Returns:
    The shortest merged string X as described above.
    """
    sn = len(S)
    tn = len(T)

    # Precompute next occurrence indices for each bit ('0' and '1') in S
    sd = [[sn + 1] * (sn + 1), [sn + 1] * (sn + 1)]
    for i in range(sn):
        idx = ord(S[i]) - ord('0')  # 0 for '0', 1 for '1'
        # For each previous position, update first position from j to i where character idx occurs
        for j in range(i, -1, -1):
            if sd[idx][j] != sn + 1:
                break
            sd[idx][j] = i + 1  # Store the next position (1-based)

    # Precompute next occurrence indices for each bit in T
    td = [[tn + 1] * (tn + 1), [tn + 1] * (tn + 1)]
    for i in range(tn):
        idx = ord(T[i]) - ord('0')
        for j in range(i, -1, -1):
            if td[idx][j] != tn + 1:
                break
            td[idx][j] = i + 1

    # Prepare buckets: sb[b][pos] is a list of indices i such that the next b from i is at position pos in S
    sb = [[[] for _ in range(sn + 2)] for _ in range(2)]
    for b in (0, 1):
        for i in range(sn + 1):
            sb[b][sd[b][i]].append(i)
        sb[b][sn + 1].append(sn + 1)
    # Prepare buckets similarly for T
    tb = [[[] for _ in range(tn + 2)] for _ in range(2)]
    for b in (0, 1):
        for i in range(tn + 1):
            tb[b][td[b][i]].append(i)
        tb[b][tn + 1].append(tn + 1)

    # Set up BFS for minimal path
    INF = max(sn, tn) + 2  # A large value representing "infinity"
    arr_temp = [INF] * (tn + 2)
    # dists[i][j]: minimal number of moves to reach position (i, j)
    dists = [array.array('i', arr_temp) for _ in range(sn + 2)]
    q = set()
    q.add((sn + 1, tn + 1))  # Start from the end (sn+1, tn+1)
    d = 0  # Depth (number of moves)
    while q:
        nq = set()
        for i, j in q:
            if dists[i][j] != INF:
                continue
            dists[i][j] = d
            # Try advancing by adding either '0' or '1'
            for b in (0, 1):
                for ni in sb[b][i]:
                    for nj in tb[b][j]:
                        if dists[ni][nj] == INF and (ni, nj) not in q:
                            nq.add((ni, nj))
        d += 1
        q = nq

    # Recover the answer by reverse-engineering the BFS path from start (0, 0)
    ans = []
    i, j = 0, 0
    d = dists[0][0]
    while (i, j) != (sn + 1, tn + 1):
        # Try extending with '0'
        ni = sd[0][i] if i < sn + 1 else sn + 1
        nj = td[0][j] if j < tn + 1 else tn + 1
        if dists[ni][nj] == d - 1:
            ans.append('0')
        else:
            ans.append('1')
            ni = sd[1][i] if i < sn + 1 else sn + 1
            nj = td[1][j] if j < tn + 1 else tn + 1
        i = ni
        j = nj
        d -= 1

    return ''.join(ans)

###############################################################################
# AUXILIARY FUNCTIONS

DEBUG = 'DEBUG' in os.environ

def inp():
    """
    Reads a line from standard input and strips the trailing newline.
    
    Returns:
    The input line as a string.
    """
    return sys.stdin.readline().rstrip()

def read_int():
    """
    Reads an integer from the next line of input.
    
    Returns:
    The integer read from input.
    """
    return int(inp())

def read_ints():
    """
    Reads a line of input and converts it into a list of integers.
    
    Returns:
    A list of integers read from input.
    """
    return [int(e) for e in inp().split()]

def dprint(*value, sep=' ', end='\n'):
    """
    Prints debug messages to stdout if DEBUG environment variable is set.
    
    Arguments:
    *value -- values to print
    sep -- separator between values
    end -- line ending
    """
    if DEBUG:
        print(*value, sep=sep, end=end)

if __name__ == '__main__':
    main()