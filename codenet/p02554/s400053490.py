def main():
    N = int(input())

    MOD = 10**9 + 7
    ans = pow(10, N, MOD) - 2*pow(9, N, MOD) + pow(8, N, MOD) + MOD
    print(ans % MOD)

if __name__ == '__main__':
    main()