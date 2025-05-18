import sys

sys.setrecursionlimit(10 ** 6)
from bisect import *
from collections import *
from heapq import *

int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline()[:-1]
def MI(): return map(int, sys.stdin.readline().split())
def MI1(): return map(int1, sys.stdin.readline().split())
def MF(): return map(float, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI1(): return list(map(int1, sys.stdin.readline().split()))
def LF(): return list(map(float, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
dij = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def main():
    while 1:
        n,p0=MI()
        if n==0:break
        i=0
        s=[0]*n
        p=p0
        while 1:
            if p:
                s[i]+=1
                if s[i]==p0:
                    break
                p-=1
            else:
                p+=s[i]
                s[i]=0
            i=(i+1)%n
        print(i)

main()