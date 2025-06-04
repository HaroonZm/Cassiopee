MOD = 10**9 + 7

def solve_arithmetical_restoration(A, B, C):
    n = len(A)
    # dp[pos][carry]: number of ways to fill digits from pos to end with incoming carry
    dp = [[0]*2 for _ in range(n+1)]
    dp[n][0] = 1

    for pos in range(n-1, -1, -1):
        ndp = [[0]*2 for _ in range(2)]
        for carry in range(2):
            ways = dp[pos+1][carry]
            if ways == 0:
                continue

            a_char = A[pos]
            b_char = B[pos]
            c_char = C[pos]

            a_digits = [int(a_char)] if a_char != '?' else list(range(10))
            b_digits = [int(b_char)] if b_char != '?' else list(range(10))
            c_digits = [int(c_char)] if c_char != '?' else list(range(10))

            for da in a_digits:
                if pos == 0 and da == 0 and n>1:
                    continue
                for db in b_digits:
                    if pos == 0 and db == 0 and n>1:
                        continue
                    for dc in c_digits:
                        if pos == 0 and dc == 0 and n>1:
                            continue
                        total = da + db + carry
                        if total % 10 == dc:
                            ndp[0][total // 10] += ways
                        # no else: if no match, skip
        for carry in range(2):
            dp[pos][carry] = ndp[0][carry] % MOD

    return dp[0][0] % MOD

def main():
    while True:
        A = input()
        if A == '0':
            break
        B = input()
        C = input()
        print(solve_arithmetical_restoration(A, B, C))

if __name__ == "__main__":
    main()