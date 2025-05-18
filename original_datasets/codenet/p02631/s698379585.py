import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    A = [int(a) for a in input().split()]
    total = 0
    for a in A:
        total ^= a
    Ans = [-1] * N
    for i, a in enumerate(A):
        Ans[i] = total ^ a
    print(*Ans, sep = " ")

    return 0

if __name__ == "__main__":
    solve()