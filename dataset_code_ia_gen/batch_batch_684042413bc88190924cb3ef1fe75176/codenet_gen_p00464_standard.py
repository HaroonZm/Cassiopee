import sys
input=sys.stdin.readline

while True:
    H,W,N=map(int,input().split())
    if H==0 and W==0 and N==0:
        break
    A=[list(map(int,input().split())) for _ in range(H)]
    r,c=0,0
    for _ in range(N-1):
        if A[r][c]==1:
            c+=1
        else:
            r+=1
        if r>=H or c>=W:
            break
    while r<H and c<W:
        d=A[r][c]
        A[r][c]=1-d
        if d==1:
            c+=1
        else:
            r+=1
    print(r+1,c+1)