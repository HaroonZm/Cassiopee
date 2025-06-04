from itertools import accumulate, islice

def solve():
    while True:
        try:
            n, k = map(int, input().split())
            if not n:
                return
            A = [int(input()) for _ in range(n)]
            prefix = [0, *accumulate(A)]
            ans = max((prefix[i + k] - prefix[i] for i in range(n - k + 1)), default=-1)
            print(ans)
        except EOFError:
            break

if __name__ == '__main__':
    solve()