from collections import deque
import sys
sys.setrecursionlimit(10**7)

N = int(input())
P = list(map(int,input().split()))

Q = [-1]*N
for i,p in enumerate(P):
    Q[p-1] = i

S = ''
a = 1
def rec(l,r):
    global S,a
    if l==r:
        return
    while l < r:
        ai = Q[a-1]
        if ai >= r:
            print(':(')
            exit()
        a += 1
        S += '('
        rec(l,ai)
        S += ')'
        l = ai + 1
rec(0,N)

print(S)