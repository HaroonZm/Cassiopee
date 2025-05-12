# import sys
# import math
# import itertools
# from collections import deque
# from collections import defaultdict
# import heapq
# import copy
# import bisect
# import numpy as np
# from scipy.special import comb

# def my_input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(100000)
# INF = 1001001001001
# MOD = 1000000007

def main():

    N, M = map(int, input().split())
    ac = [0 for _ in range(N)]
    wa = [0 for _ in range(N)]

    for _ in range(M):
        p, s = input().split()
        p = int(p) - 1
        if s == 'AC':
            ac[p] = 1
        else:
            if ac[p] == 0:
                wa[p] += 1

    # print(ac)
    # print(wa)

    for i in range(N):
        if ac[i] == 0:
            wa[i] = 0

    print(str(sum(ac)) + " " + str(sum(wa)))

if __name__ == '__main__':
    main()