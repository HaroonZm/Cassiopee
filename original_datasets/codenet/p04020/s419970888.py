import sys

def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n = int(readline())
    mt = 0
    t = 0
    for i in range(n):
        a = int(readline())
        if a == 0:
            mt += t // 2
            t = 0
        else:
            t += a
    print(mt + t // 2)

if __name__ == '__main__':
    solve()