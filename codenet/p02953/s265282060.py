import sys

sys.setrecursionlimit(10 ** 7)
# import bisect
# import numpy as np
# from collections import deque
from collections import deque
# map(int, sys.stdin.read().split())
import itertools
import heapq

def input():
    return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    H =list(map(int,input().split()))
    off = 0
    flag =1
    for i in range(N-1,0,-1):
        if H[i] - off >=H[i-1]:
            off =0
            continue
        elif H[i]-off +1 == H[i-1]:
            off =1
        else:
            print("No")
            exit()

    print("Yes")

if __name__ == "__main__":
    main()