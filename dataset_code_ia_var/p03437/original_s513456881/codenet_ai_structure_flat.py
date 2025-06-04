import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7

x, y = map(int, input().split())
if x % y == 0:
    print(-1)
else:
    print(x)