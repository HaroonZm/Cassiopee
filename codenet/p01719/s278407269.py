import sys

def main():
    n,d,x = map(int, sys.stdin.readline().split())

    pp = []
    for i in range(d):
        pp.append( list(map(int,sys.stdin.readline().split())) )

    dp = [0] * 100001
    curr_x = x
    for k in range(d - 1):
        next_x = curr_x
        for i in range(curr_x + 1):
            dp[i] = 0
        for i in range(n):
            for j in range(curr_x + 1):
                if j - pp[k][i] >= 0:
                    dp[j] = max(dp[j], dp[j - pp[k][i]] + pp[k + 1][i])
                next_x = max(next_x, (curr_x - j) + dp[j])
        curr_x = next_x

    print(curr_x)

if __name__ == '__main__':
    main()