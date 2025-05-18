import sys
input = sys.stdin.readline

def main():
    while True:
        n,m,t,p = map(int,input().split())
        if [n,m,t,p] == [0,0,0,0]:
            exit()
        dp = [[0]*(m*m+1) for i in range(n*n+1)]
        
        
        sx = 0
        sy = 0
        ex = n
        ey = m

        
        for i in range(n):
            for j in range(m):
                dp[sx+i][sy+j] = 1
        
        for i in range(t):
            d,c = map(int,input().split())
            if d == 1:
                for k in range(c):
                    for j in range(sy,ey):
                        dp[sx+c+k][j] += dp[sx+c-k-1][j]
                sx += c
                ex = max(ex,sx+c)
            else:
                for k in range(c):
                    for j in range(sx,ex):
                        dp[j][sy+c+k] += dp[j][sy+c-k-1]
                sy += c
                ey = max(ey,sy+c)
        res = 0
        for i in range(p):
            x,y = map(int,input().split())
            res = dp[sx+x][sy+y]
            print(res)
            
            
main()