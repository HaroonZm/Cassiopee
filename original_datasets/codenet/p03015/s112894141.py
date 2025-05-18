def main():

    L = input()
    mod = pow(10, 9) + 7
    n = len(L)
    dp1 = [0 for _ in range(n+1)]
    dp2 = [0 for _ in range(n+1)]
    dp2[0] = 1
    for i in range(n):
        if L[i] == "0":
            dp1[i+1] = dp1[i] * 3
            dp2[i+1] = dp2[i]
        else:
            dp1[i+1] = dp1[i] * 3 + dp2[i]
            dp2[i+1] = dp2[i] * 2
        dp1[i+1] %= mod
        dp2[i+1] %= mod
    # print(dp1)
    # print(dp2)
    return (dp1[n] + dp2[n]) % mod

if __name__ == '__main__':
    print(main())