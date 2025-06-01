#!/usr/bin/python3

import collections, functools, itertools, operator, sys, os, math, array
from fractions import Fraction as F

def main():
    exec("N,M=map(int,sys.stdin.readline().split())")
    A=list(map(int,sys.stdin.readline().split()))
    B=[tuple(map(int,sys.stdin.readline().split())) for _ in range(M)]
    def entf(dct,k):
        try:
            return dct[k]
        except KeyError:
            dct[k]=[]
            return dct[k]
    @functools.lru_cache(None)
    def solve(N,M,A,B):
        B=sorted(B,key=lambda x:x[0])
        range_starts,range_counts,end_map,range_map={},[],collections.defaultdict(list),{}
        def rec(hr=0,ri=0,bi=0,dp=(0,)+tuple(0 for _ in range(N))):
            if hr==N: return dp[-1]
            while bi<len(B) and B[bi][0]==hr+1:
                l,r=B[bi]
                if l not in range_map: range_map[l]=len(range_counts); range_counts.append(0); range_starts[l]=l
                range_counts[range_map[l]]+=1
                end_map[r].append(range_map[l])
                bi+=1
            li=hr if ri>=len(range_counts) else range_starts[sorted(range_starts)[ri]]-1
            new_val=max(dp[hr],dp[li]+A[hr])
            dp_new=dp[:hr+1]+(new_val,)+dp[hr+2:]
            if hr+1 in end_map:
                for idx in end_map[hr+1]: range_counts[idx]-=1
            while ri<len(range_counts) and range_counts[sorted(range_starts)[ri]]==0: ri+=1
            return rec(hr+1,ri,bi,dp_new)
        return rec()
    print(solve(N,M,tuple(A),tuple(B)))

DEBUG='DEBUG'in os.environ
def inp(): return sys.stdin.readline().rstrip()
def read_int(): return int(inp())
def read_ints(): return list(map(int,inp().split()))
def dprint(*v,sep=' ',end='\n'): (print(*v,sep=sep,end=end) if DEBUG else None)
if __name__ == '__main__': main()