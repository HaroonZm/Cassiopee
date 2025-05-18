import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

while True:
    n=int(input())
    if n==0:
        break
    books=[]
    read_t=0
    write_t=0
    for i in range(n):
        r,w=map(int,input().split())
        read_t+=r
        write_t+=w
        books.append((r,w))
    books=sorted(books)
    if books[-1][0]<=read_t//2:
        print(read_t+write_t)
        continue
    sukima=books[-1][0]-(read_t-books[-1][0])
    dp=[[0 for i in range(sukima+1)] for i in range(n)]
    for i in range(1,n):
        for j in range(1,sukima+1):
            dp[i][j]=max(dp[i-1][j],
            dp[i-1][j-books[i-1][1]]
            +books[i-1][1] if j-books[i-1][1]>=0 else 0)

    print(read_t+write_t+sukima-dp[-1][-1])