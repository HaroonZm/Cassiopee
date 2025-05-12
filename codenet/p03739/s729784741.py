import sys
from itertools import accumulate

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007

def solve(A):
    ans = 0
    s = A[0]
    for a in A[1:]:
        prev, s = s, s + a
        if prev > 0 and s >= 0:
            ans += s + 1
            s = -1
        if prev < 0 and s <= 0:
            ans += -s + 1
            s = 1

    return ans

def main():
    N, *A = map(int, read().split())

    a0 = A[0]

    ans1 = 0
    if A[0] <= 0:
        ans1 = -A[0] + 1
        A[0] = 1
    ans1 += solve(A)

    A[0] = a0

    ans2 = 0
    if A[0] >= 0:
        ans2 = A[0] + 1
        A[0] = -1
    ans2 += solve(A)

    print(min(ans1, ans2))

    return

if __name__ == '__main__':
    main()