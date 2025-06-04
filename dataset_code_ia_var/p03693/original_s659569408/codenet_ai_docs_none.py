import sys, os

f = lambda: list(map(int, input().split()))
if 'local' in os.environ:
    sys.stdin = open('./input.txt', 'r')

def solve():
    a, b, c = f()
    if (a * 100 + b * 10 + c) % 4 == 0:
        print('YES')
    else:
        print('NO')

solve()