import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7

def resolve():
    x, y = map(int, input().split())
    print(-1 if x % y == 0 else x)

if __name__ == '__main__':
    resolve()