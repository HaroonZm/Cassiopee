def solve(low, n, ls):
    dp = [100000000000000000000 for i in range(n + 1)]
    dp[0] = low
    for i in range(n):
        length = 0
        for j in range(i, -1, -1):
            length += ls[j]
            if i + 1 == n and j == 0:
                continue
            if length >= low:
                high = length
                if dp[j] > length:
                    high = dp[j]
                if dp[i+1] > high:
                    dp[i+1] = high
    return dp[n] - low

def main():
    n = int(input())
    ls = []
    for i in range(n):
        num = int(input())
        ls.append(num)
    ans = 100000000000000000000
    for i in range(n):
        length = 0
        for j in range(i, n):
            length += ls[j]
            temp = solve(length, n, ls)
            if temp < ans:
                ans = temp
    print(ans)

main()