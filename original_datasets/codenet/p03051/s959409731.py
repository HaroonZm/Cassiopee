import sys, math, collections, heapq, itertools
F = sys.stdin
def single_input(): return F.readline().strip("\n")
def line_input(): return F.readline().strip("\n").split()
def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while a % b > 0:
        a, b = b, a % b
    return b

mod = 7 + 10 ** 9

def solve():
    N = int(single_input())
    A = [int(a) for a in line_input()]

    DP = [[0, 1] for i in range(2 ** 20)]
    memo = [0] * (2 ** 20)
    cumulative_xor = 0
    zeros = 0
    for i in range(N):
        cumulative_xor ^= A[i]
        if cumulative_xor == 0: zeros += 1  
        else:
            DP[cumulative_xor][1] += DP[cumulative_xor][0] * (zeros - memo[cumulative_xor])
            DP[cumulative_xor][1] %= mod
            DP[cumulative_xor][0] += DP[cumulative_xor][1]
            DP[cumulative_xor][0] %= mod
            memo[cumulative_xor] = zeros

    if cumulative_xor > 0: print(DP[cumulative_xor][1])
    else:
        ans = pow(2, zeros - 1, mod)
        for i in range(2**20): 
            ans += DP[i][0]
            ans %= mod
        print(ans)
        
    return 0
  
if __name__ == "__main__":
    solve()