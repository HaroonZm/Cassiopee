import sys as _; import fractions as __
_.setrecursionlimit(1000000)

def __call__(func, *args, **kwargs):
    return func(*args, **kwargs)

@staticmethod
def _idx(x): return int(x)-1

show_rows = lambda l: [print(r) for r in l] or None

inpINT=lambda:__call__(int,input())
MII=lambda:map(int,input())
MII_sp = lambda: map(int,input().split())
MII_idx = lambda: map(_idx, input())
MII_sp_idx = lambda: map(_idx, input().split())
LII = lambda: list(map(int, input()))
LII_sp = lambda: list(map(int, input().split()))
def LII_2D(_n): return [LII() for __times in range(_n)]
def LII_sp_2D(_n): return [LII_sp() for __x in [-~0]*_n]

def _gcd(a, b):
    return __.gcd(a,b)

@classmethod
def lcm(cls, x, y): return (x*y)//_gcd(x,y)

A,B=[*MII_sp()]
print(lcm(None, A, B))