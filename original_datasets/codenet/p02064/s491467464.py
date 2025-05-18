import sys
from operator import itemgetter
from fractions import gcd
from math import ceil, floor, sqrt
from copy import deepcopy
from collections import Counter, deque
import heapq
from functools import reduce
# local only
# if not __debug__:
#     fin = open('in_1.txt', 'r')
#     sys.stdin = fin
# local only
sys.setrecursionlimit(200000)
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return map(int, input().rstrip().split())
def lmi(): return list(map(int, input().rstrip().split()))
def li(): return list(input().rstrip())
def debug(*args, sep=" ", end="\n"): print("debug:", *args, file=sys.stderr, sep=sep, end=end) if not __debug__ else None
def exit(*arg): print(*arg); sys.exit()
# template

def main():
    N, s, t = mi()
    s -= 1; t -= 1
    print("?", s + 1, t + 1, flush=True)
    st = ii()
    lis = [0] * N
    lis[t] = st
    lit = [0] * N
    lit[s] = st
    for i in range(N):
        if i != s and i != t:
            print("?", s + 1, i + 1, flush=True)
            lis[i] = ii()
            print("?", t + 1, i + 1, flush=True)
            lit[i] = ii()
    # print(lis, lit)
    sub = []
    for i in range(N):
        if lis[i] + lit[i] == st:
            sub.append((i, lis[i]))
    sub.sort(key=itemgetter(1))
    # print(sub)
    if len(sub) == 2:
        print("!", s + 1, t + 1, flush=True)
        sys.exit()
    ans = []
    q = deque(sub)
    lastnode = s
    q.popleft()
    ans.append(s)
    u, w = q.popleft()
    ans.append(u)
    lastnode = u
    while True:
        u, w = q.popleft()
        if u == t:
            ans.append(u)
            lastnode = u
            break
        print("?", lastnode + 1, u + 1, flush=True)
        tmp = ii()
        if lis[lastnode] + tmp + lit[u] == st:
            ans.append(u)
            lastnode = u
            continue
        else:
            continue
    print("!", *list(map(lambda x: x + 1, ans)))

if __name__ == '__main__':
    main()