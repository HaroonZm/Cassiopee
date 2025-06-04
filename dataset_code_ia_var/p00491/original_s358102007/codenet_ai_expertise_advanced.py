from sys import stdin
from itertools import product

def main():
    N, K = map(int, stdin.readline().split())
    S = [-1] * N
    for _ in range(K):
        a, b = map(int, stdin.readline().split())
        S[a - 1] = b - 1

    dp = [0] * 9
    st, nd = S[:2]

    if st != -1 and nd != -1:
        dp[st * 3 + nd] = 1
    elif st != -1:
        dp[st * 3:st * 4] = [1] * 3
    elif nd != -1:
        for i in range(3):
            dp[nd + i * 3] = 1
    else:
        dp = [1] * 9

    for idx in range(2, N):
        cur = S[idx]
        ndp = [0] * 9
        if cur != -1:
            for k in range(3):
                base = k * 3 + cur
                ndp[base] = sum(dp[k * 3 + pre] for pre in range(3) if not (pre == k == cur))
        else:
            for k, curc in product(range(3), repeat=2):
                base = k * 3 + curc
                ndp[base] = sum(dp[k * 3 + pre] for pre in range(3) if not (pre == k == curc))
        dp[:] = ndp

    print(sum(dp) % 10000)

if __name__ == "__main__":
    main()