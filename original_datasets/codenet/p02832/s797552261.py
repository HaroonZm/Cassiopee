import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007

def main():
    N, *A = map(int, read().split())

    n = 1
    for a in A:
        if a == n:
            n += 1

    if n == 1:
        print(-1)
    else:
        print(N - n + 1)
    return

if __name__ == '__main__':
    main()