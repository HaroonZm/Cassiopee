import sys

read = sys.stdin.buffer.read
input = sys.stdin.buffer.readline
inputs = sys.stdin.buffer.readlines

# rstrip().decode('utf-8')
# INF=float("inf")
MOD=10**9+7
# sys.setrecursionlimit(2147483647)
# import math
#import numpy as np
# import operator
# import bisect
# from heapq import heapify,heappop,heappush
#from math import gcd
# from fractions import gcd
# from collections import deque
# from collections import defaultdict
# from collections import Counter
# from itertools import accumulate
# from itertools import groupby
# from itertools import permutations
# from itertools import combinations
# from scipy.sparse import csr_matrix
# from scipy.sparse.csgraph import floyd_warshall
# from scipy.sparse.csgraph import csgraph_from_dense
# from scipy.sparse.csgraph import dijkstra
# map(int,input().split())

def framod(n, mod, a=1):
    for i in range(1,n+1):
        a=a * i % mod
    return a

def power(n, r, mod):
    if r == 0: return 1
    if r%2 == 0:
        return power(n*n % mod, r//2, mod) % mod
    if r%2 == 1:
        return n * power(n, r-1, mod) % mod

def comb(n, k, mod):
    a=framod(n, mod)
    b=framod(k, mod)
    c=framod(n-k, mod)
    return (a * power(b, mod-2, mod) * power(c, mod-2, mod)) % mod

def main():
	N,K=map(int,input().split())
	
	for i in range(1,K+1):
		if i<=N-K+1:
			print(comb(N-K+1,i,MOD)*comb(K-1,i-1,MOD)%MOD)
		else:
			print(0)
	

if __name__ == '__main__':
	main()