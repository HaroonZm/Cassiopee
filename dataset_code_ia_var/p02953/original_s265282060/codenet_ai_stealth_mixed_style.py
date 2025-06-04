import sys
sys.setrecursionlimit(10000000)
from collections import deque
import itertools
import heapq

def input_(): return sys.stdin.readline().strip()

class Solution(object):
    def solve(self):
        N = int(input_())
        H = list(map(int,input_().split()))
        idx = N-1
        offset = 0
        f = True
        while idx > 0:
            if (H[idx] - offset) >= H[idx-1]:
                offset = 0
            elif (H[idx] - offset + 1) == H[idx-1]:
                offset = 1
            else:
                print("No")
                return
            idx -= 1
        print("Yes")

def S():
    sol = Solution()
    sol.solve()

if __name__ == "__main__":
    (lambda: S())()