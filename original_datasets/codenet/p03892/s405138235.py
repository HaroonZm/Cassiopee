import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

from fractions import gcd

A,B,C,D = map(int,input().split())

dx = abs(A-C)
dy = abs(B-D)

g = gcd(dx,dy)
answer = (dx + dy) - g
print(answer)