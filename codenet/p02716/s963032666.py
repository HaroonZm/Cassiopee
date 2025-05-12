import sys
input = sys.stdin.buffer.readline

def main():
    N = int(input())
    a = list(map(int,input().split()))
    INF = -10**15
    
    dp = [[[INF,INF],[False,False]] for _ in range(N)]
    dp[0][0][0],dp[0][0][1],dp[0][1][1] = 0,a[0],True
    dp[1][0][0] = 0
    if a[0] < a[1]:
        dp[1][0][1],dp[1][1][1] = a[1],True
    else:
        dp[1][0][1] = a[0]
    
    for i in range(2,N):
        if i%2 != 0:
            dp[i][0][0] = dp[i-1][0][0]
            if dp[i][0][0] < dp[i-2][0][0]+a[i]:
                dp[i][0][0] = dp[i-2][0][0]+a[i]
                dp[i][1][0] = True
            dp[i][0][1] = dp[i-1][0][1]
            if dp[i-1][1][0] == False:
                if dp[i][0][1] < dp[i-1][0][0]+a[i]:
                    dp[i][0][1] = dp[i-1][0][0]+a[i]
                    dp[i][1][1] = True
            if dp[i][0][1] < dp[i-2][0][1]+a[i]:
                dp[i][0][1] = dp[i-2][0][1]+a[i]
                dp[i][1][1] = True
        else:
            dp[i][0][0] = dp[i-1][0][1]
            if dp[i-1][1][0] == False:
                if dp[i][0][0] < dp[i-1][0][0]+a[i]:
                    dp[i][0][0] = dp[i-1][0][0]+a[i]
                    dp[i][1][0] = True
            if dp[i][0][0] < dp[i-2][0][0]+a[i]:
                dp[i][0][0] = dp[i-2][0][0]+a[i]
                dp[i][1][0] = True
            dp[i][0][1] = dp[i-2][0][1]+a[i]
            if dp[i-1][1][1] == False:
                if dp[i][0][1] < dp[i-1][0][1]+a[i]:
                    dp[i][0][1] = dp[i-1][0][1]+a[i]
            dp[i][1][1] = True
    
    if N%2 == 0:
        print(dp[-1][0][1])
    else:
        print(dp[-1][0][0])
 
if __name__ == "__main__":
    main()