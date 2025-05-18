import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    N = int(input())
    W = list(map(int, input().split()))
    wts = [0 for _ in range(N + 1)]
    for i in range(N):
        wts[i + 1] = wts[i] + W[i]

    ans = 10 ** 9 + 7
    for i in range(N):
        ans = min(ans, abs(wts[i + 1] - (wts[N] - wts[i + 1])))

    print(ans)

if __name__ == '__main__':
    solve()