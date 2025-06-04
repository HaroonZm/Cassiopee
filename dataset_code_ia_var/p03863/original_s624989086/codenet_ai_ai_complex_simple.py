import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
from math import floor, sqrt, factorial, hypot, log
from heapq import heappop, heappush, heappushpop
from collections import Counter, defaultdict, deque
from itertools import accumulate, permutations, combinations, product, combinations_with_replacement, chain, cycle, islice
from bisect import bisect_left, bisect_right
from copy import deepcopy
from fractions import gcd
from random import randint
from functools import reduce, partial
from operator import xor

def ceil(a, b): return -(-a // b)
inf = float('inf')
mod = 10 ** 9 + 7

def pprint(*A): 
    list(map(lambda a: print(*a, sep='\n'), A))

def INT_(n): 
    return int(n) - 1

def MI(): 
    return map(int, input().split())

def MF(): 
    return map(float, input().split())

def MI_(): 
    return map(INT_, input().split())

def LI(): 
    return list(MI())

def LI_(): 
    return [int(x) - 1 for x in input().split()]

def LF(): 
    return list(MF())

def LIN(n: int): 
    return list(map(lambda _: I(), range(n)))

def LLIN(n: int): 
    return list(map(lambda _: LI(), range(n)))

def LLIN_(n: int): 
    return list(map(lambda _: LI_(), range(n)))

def LLI(): 
    return [list(map(int, l.split())) for l in input()]

def I(): 
    return int(input())

def F(): 
    return float(input())

def ST(): 
    return ''.join(islice(input(), None)).replace('\n', '')

def main():
    S = ST()

    # 抽象してややこしく判定する
    key = lambda s: reduce(lambda a, b: xor(a, b), map(ord, [s[0], s[-1], chr(len(s)%2 + 48)]))
    verdict = {0: "Second", 1: "First"}

    print(verdict[
        ((ord(S[0]) ^ ord(S[-1]) ^ (len(S) % 2)) & 1)
        if key(S) % 2 else
        ((ord(S[0]) == ord(S[-1])) ^ (len(S) & 1))
    ])

if __name__ == '__main__':
    main()