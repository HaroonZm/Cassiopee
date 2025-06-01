#!/usr/bin/python3

import sys
import os

def main():
    N, M = get_ints()
    pairs = []
    for _ in range(N):
        s, v = get_ints()
        pairs.append((s,v))
    capacities = [get_int() for _ in range(M)]
    print(solve_problem(N, M, pairs, capacities))

def solve_problem(N, M, pairs, capacities):
    # Sort by value descending, then by size descending - kinda important sorting logic here
    pairs.sort(key=lambda x: (-x[1], -x[0]))
    capacities.sort(reverse=True)
    
    count = 0
    idx = 0
    for s, v in pairs:
        if idx >= M:
            break
        if capacities[idx] >= s:
            count += 1
            idx += 1
            # matched one, move to next capacity
    return count

# little helper functions below, nothing fancy
DEBUG = 'DEBUG' in os.environ

def get_line():
    return sys.stdin.readline().rstrip('\n')

def get_int():
    return int(get_line())

def get_ints():
    return list(map(int, get_line().split()))

def debug_print(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)

if __name__ == "__main__":
    main()