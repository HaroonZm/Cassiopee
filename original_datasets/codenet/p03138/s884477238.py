import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)

def main():
    n, k = map(int, readline().split())
    a = list(map(int, readline().split()))
    zero_plus = [0] * 60  # 0を選んだときに増える数
    one_plus = [0] * 60

    for x in a:
        s = format(x, "b")
        s = s[::-1]
        l = len(s)
        for i in range(60):
            if i >= l:
                one_plus[i] += 1
            elif s[i] == "0":
                one_plus[i] += 1
            else:
                zero_plus[i] += 1

    dp = dict()
    dp[True] = [-INF] * 61
    dp[False] = [0] * 61

    k_bin = format(k, "b")
    k_bin_length = k.bit_length()

    for i in range(59, -1, -1):
        cur = 2 ** i
        d = k_bin_length - i - 1
        if d < 0:
            dp[False][i] = dp[False][i + 1] + zero_plus[i] * cur
        else:
            zero = cur * zero_plus[i]
            one = cur * one_plus[i]
            if k_bin[d] == "1":
                dp[True][i] = max(dp[False][i + 1] + zero, dp[True][i + 1] + one, dp[True][i + 1] + zero)
                dp[False][i] = dp[False][i + 1] + one
            else:
                dp[True][i] = max(dp[True][i + 1] + zero, dp[True][i + 1] + one)
                dp[False][i] = dp[False][i + 1] + zero

    print(max(dp[True][0], dp[False][0]))

if __name__ == '__main__':
    main()