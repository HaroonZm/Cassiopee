MOD = 10**9 + 7
L = input()

def solve(L):
    dp = [1, 0]     # dp[0]: eqDp, dp[1]: lessDp

    i = 0
    while i < len(L):
        if L[i] == '1':
            temp_eq = dp[0]*2
            temp_less = dp[1]*3 + dp[0]
        else:
            temp_eq = dp[0]
            temp_less = dp[1]*3

        dp[0] = temp_eq % MOD
        dp[1] = temp_less % MOD
        i += 1

    r = sum(dp) % MOD
    return r

class A:pass
setattr(A,"f",solve)
print((lambda s: A.f(s))(L))