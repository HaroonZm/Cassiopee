import sys
def main():
    input=sys.stdin.readline
    h,w=map(int,input().split())
    a=[list(map(int,input().split())) for _ in range(h)]
    b=[list(map(int,input().split())) for _ in range(h)]
    ofset = 80*164
    #mask = (1 << (ofset*2)) - 1
    dp=[[0 for i in range(w)] for j in range(h)]
    dp[0][0] |= 1 << (a[0][0] - b[0][0] + ofset)
    dp[0][0] |= 1 << (b[0][0] - a[0][0] + ofset)
    for i in range(h):
        for j in range(w):
            if i < h - 1:
                A = abs(a[i+1][j] - b[i+1][j])
                dp[i+1][j] |= (dp[i][j] << A)
                dp[i+1][j] |= (dp[i][j] >> A)
            if j < w - 1:
                A = abs(a[i][j+1] - b[i][j+1])
                dp[i][j+1] |= (dp[i][j] << A)
                dp[i][j+1] |= (dp[i][j] >> A)
    ans = 10000000000
    for i in range(ofset, 80*330):
        if (dp[h-1][w-1]>>i)&1:
            ans = i - ofset
            break
    for i in reversed(range(ofset)):
        if (dp[h-1][w-1]>>i)&1:
            ans = min(ans, ofset - i)
            break
    print(ans)
if __name__=='__main__':
  main()