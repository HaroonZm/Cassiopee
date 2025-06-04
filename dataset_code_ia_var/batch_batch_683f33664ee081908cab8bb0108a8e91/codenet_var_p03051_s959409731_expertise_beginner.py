import sys

def single_input():
    return sys.stdin.readline().strip()

def line_input():
    return sys.stdin.readline().strip().split()

def main():
    mod = 7 + 10 ** 9
    N = int(single_input())
    A = list(map(int, line_input()))

    DP = []
    for i in range(2 ** 20):
        DP.append([0, 1])
    memo = [0] * (2 ** 20)
    cumulative_xor = 0
    zeros = 0

    for i in range(N):
        cumulative_xor = cumulative_xor ^ A[i]
        if cumulative_xor == 0:
            zeros += 1
        else:
            temp = DP[cumulative_xor][0] * (zeros - memo[cumulative_xor])
            DP[cumulative_xor][1] = DP[cumulative_xor][1] + temp
            DP[cumulative_xor][1] = DP[cumulative_xor][1] % mod
            DP[cumulative_xor][0] = DP[cumulative_xor][0] + DP[cumulative_xor][1]
            DP[cumulative_xor][0] = DP[cumulative_xor][0] % mod
            memo[cumulative_xor] = zeros

    if cumulative_xor > 0:
        print(DP[cumulative_xor][1])
    else:
        ans = pow(2, zeros - 1, mod)
        for i in range(2 ** 20):
            ans = ans + DP[i][0]
            ans = ans % mod
        print(ans)

if __name__ == "__main__":
    main()