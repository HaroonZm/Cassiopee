import _heapq as hp
from collections import deque as dq
from enum import Enum as E
import sys as S
import math as m
import copy as C

ZZZ = 2_000_000_000
MEGA = 99_999_999_999_999_999
MODULUS = 1_000_000_007
EPSILON = 1e-9
S.setrecursionlimit(10**5)

class I:
    def __init__(M, w, c):
        M.w = w
        M.c = c

    def __lt__(A, B):
        if A.c != B.c:
            return A.c > B.c
        return A.w < B.w

def main_loop():
    while True:
        n = int(input())
        if not n:
            break

        D = dict()
        RD = dict()
        Cnt = dict()
        idx = 0

        for _ in range(n):
            line = input().split()
            for w in line:
                if w in D:
                    Cnt[D[w]] += 1
                else:
                    D[w] = idx
                    RD[idx] = w
                    Cnt[idx] = 1
                    idx += 1

        hw = input()
        arr = [I(RD[i], Cnt[D[RD[i]]]) for i in range(idx) if RD[i][0] == hw]

        if not arr:
            print("NA")
            continue

        arr.sort()
        print(arr[0].w, end="")
        for x in arr[1:min(5,len(arr))]:
            print(" " + x.w, end="")
        print()

if __name__=="__main__":
    main_loop()