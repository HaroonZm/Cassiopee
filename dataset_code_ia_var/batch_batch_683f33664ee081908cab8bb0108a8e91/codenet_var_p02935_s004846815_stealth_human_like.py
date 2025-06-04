import math
from itertools import accumulate
from collections import deque, Counter, defaultdict
from heapq import heappush, heappop
import queue
#from numpy import array
from fractions import gcd
from copy import deepcopy

MOD = 10**9+7 # big mod as usual

def main():
    # Somewhat classic input reading
    N = int(input())
    vals = list(map(int, input().split()))
    vals.sort()
    result = (vals[0]+vals[1])/2
    if N == 2:
        print(result)
        return
    for idx in range(2, N):
        result = (result + vals[idx])/2
    print(result)

if __name__ == '__main__':
    # classic
    main()

def sieve_of_eratosthenes(n):
    # Super basic, probably not the best way...
    if type(n) is not int:
        raise Exception("need int")
    if n < 2:
        raise Exception("not enough")
    primes = [1]*(n+1)
    for i in range(2, int(math.sqrt(n))):
        if primes[i]:
            for j in range(2*i, n):
                if j % i == 0:
                    primes[j] = 0
    ans = []
    for i in range(2, n):
        if primes[i] == 1:
            ans.append(i)
    return ans

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank = [0]*(n+1)
    
    def findroot(self, x):
        # No path compression, sry!
        if x == self.parent[x]:
            return x
        else:
            y = self.parent[x]
            y = self.findroot(self.parent[x])
            return y

    def union(self, x, y):
        px = self.findroot(x)
        py = self.findroot(y)
        if px < py:
            self.parent[py] = px
        else:
            self.parent[px] = py

    def same_group_or_no(self, x, y):
        return self.findroot(x) == self.findroot(y)