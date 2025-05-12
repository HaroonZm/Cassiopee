def main():
    while True:
        line=raw_input()
        if line=="#":   break;
        solve(line)
        
def solve(line):
    length=len(line)
    INF=1<<29
    dp=[[[[INF for l in range(3)] for k in range(3)] for j in range(2)] for i in range(2)]
    dp[1][1][0][2]=0
    dp[1][0][0][2]=0
    for i in range(length):
        n=i%2
        n2=(i+1)%2
        pos=(int(line[i])+2)%3
        for l in range(3):
            for r in range(3):
                if l<=pos:
                    dp[n][1][l][pos]=min(dp[n][1][l][pos], min(dp[n2][0][l][r], dp[n2][1][l][r]+1) )
                if pos<=r:
                    dp[n][0][pos][r]=min(dp[n][0][pos][r], min(dp[n2][1][l][r], dp[n2][0][l][r]+1) )
        for l in range(3):
            for r in range(3):
                for j in range(2):
                    dp[n2][j][l][r]=INF
    ans=INF
    tmp=(length-1)%2
    for j in range(2):
        for l in range(3):
            for r in range(3):
                ans=min(ans, dp[tmp][j][l][r])
    print ans

if __name__=="__main__":    main()