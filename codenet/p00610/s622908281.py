def checkback(B,i,j):
    samesum= (B[i][j]==B[i][j-1]) +(B[i][j]==B[i][j+1]) +(B[i][j]==B[i-1][j])
    if samesum==2:
        return not B[i][j]
    else:
        return B[i][j]

while(1):
    [N,K]=map(int,raw_input().split())
    if N==0:
        break
    if N%2 or K>2**(N/2):
        print "No\n"
    else:
        n=N/2
        A=[0 for i in range(N)]
        K-=1
        for i in range(1,n+1):
            A[2*(i-1)]= K/2**(n-i)
            A[2*(i-1)+1]= K/2**(n-i)
            K%=2**(n-i)
        B=[[-1 for i in range(N+2)] for j in range(N+2)]
        B[1][1:N+1]=A[:]
        for i in range(2,N+1):
            for j in range(1,N+1):
                B[i][j]=checkback(B,i-1,j)
        for i in range(1,N+1):
            ls=""
            for j in range(1,N+1):
                ls+=".E"[B[i][j]]
            print ls
        print"\n",