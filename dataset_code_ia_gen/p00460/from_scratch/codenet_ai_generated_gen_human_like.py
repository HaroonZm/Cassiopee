import sys
sys.setrecursionlimit(10**7)

MOD = 100000

def solve(N, M, S):
    # dp[row][sum] = number of ways to form a strictly increasing sequence of length row with sum = sum from [1..M]
    # For each column, we pick a strictly increasing sequence from top to bottom.
    # The conditions imply:
    # - Each column strictly increasing top to bottom
    # - Each element larger than any element in any column to the left → global strictly increasing order by rows and columns
    #
    # The entire card is like N sequences of length N, creating a total strictly increasing N*N elements arranged in N rows and N cols.
    # Actually, condition 5 implies that for each position (r,c), the value is > all values in columns to the left (c'<c)
    # Since columns themselves increase downwards, and elements are strictly larger than left columns, the entire matrix is strictly increasing when read row-wise from left to right, top to bottom.
    #
    # So the whole matrix numbers are arranged as one strictly increasing sequence of length N*N.
    #
    # We want to count the number of strictly increasing sequences of length N*N, with elements in [1..M], sum = S.
    #
    # But condition 4 says: each column values are ascending top to bottom.
    # Condition 5 says: any element is strictly greater than any element to the left columns.
    #
    # Together this means the matrix flattened column-wise is strictly increasing
    # as well as the rows.
    #
    # The conditions imply the matrix is basically a strictly increasing sequence (length N*N) arranged row-wise.
    # After assigning, we check sum = S, count how many sequences satisfy sum=S.
    #
    # So problem reduces to:
    # Count the number of strictly increasing sequences of length N*N choosing numbers from [1..M], sum S.
    #
    #
    # Approach:
    # dp[pos][prev][sum] : number of strictly increasing sequences of length pos, last number prev, and sum = sum
    #
    # But M and S can be large → dp with prev in [1..M], sum in [1..S] is huge.
    #
    # Use combinational approach:
    # Count the number of strictly increasing sequences of length length from numbers 1..M with sum = S.
    #
    # This is equivalent to counting compositions of sum into length distinct strictly increasing numbers from [1..M].
    #
    # We can use DP with optimization for strict increasing sequences sum counts:
    #
    # Define dp[length][sum]: number of strictly increasing sequences of length "length" and sum = "sum" drawn from 1..M.
    # Use combinatorial DP:
    # dp[0][0] = 1
    # For x in [1..M]:
    #   For length from N*N down to 1:
    #     For sum from x to S:
    #       dp[length][sum] += dp[length-1][sum - x]
    #
    # Result dp[N*N][S] modulo MOD.
    #
    # We implement the DP for each input.

def main():
    import sys
    input = sys.stdin.readline

    while True:
        N, M, S = map(int, input().split())
        if N == 0 and M == 0 and S == 0:
            break

        length = N * N
        dp = [0] * (S + 1)
        dp[0] = 1

        for x in range(1, M + 1):
            # Update dp from end to start to avoid reuse in same iteration and ensure strict
            for l in range(length, 0, -1):
                # for sum from S down to x
                # But to save memory we flatten l dimension later
                # Instead, use a 2D dp for length and sum for clarity
                pass

        # Because we need length dimension, we do 2D DP

def solve(N, M, S):
    length = N * N
    MOD = 100000
    # dp[length+1][S+1], dp[i][j] = number of strictly increasing sequences of length i sum j
    dp = [ [0]*(S+1) for _ in range(length+1)]
    dp[0][0] = 1
    for x in range(1, M+1):
        for i in range(length-1, -1, -1):
            for j in range(S - x +1):
                if dp[i][j]:
                    dp[i+1][j+x] = (dp[i+1][j+x] + dp[i][j]) % MOD
    return dp[length][S] % MOD

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    while True:
        N,M,S = map(int,input().split())
        if N==0 and M==0 and S==0:
            break
        print(solve(N,M,S))