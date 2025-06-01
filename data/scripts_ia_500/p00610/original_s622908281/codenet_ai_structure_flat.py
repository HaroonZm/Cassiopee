while True:
    N,K=map(int,raw_input().split())
    if N==0:
        break
    if N%2 or K>2**(N/2):
        print "No\n"
    else:
        n=N/2
        A=[0]*N
        K-=1
        for i in range(1,n+1):
            val=K//2**(n - i)
            A[2*(i-1)]=val
            A[2*(i-1)+1]=val
            K=K%2**(n - i)
        B=[[-1]*(N+2) for _ in range(N+2)]
        for idx in range(1,N+1):
            B[1][idx]=A[idx-1]
        for i in range(2,N+1):
            for j in range(1,N+1):
                count=0
                if B[i-1][j]==B[i-1][j-1]:
                    count+=1
                if B[i-1][j]==B[i-1][j+1]:
                    count+=1
                if B[i-1][j]==B[i-2][j]:
                    count+=1
                if count==2:
                    B[i][j]=int(not B[i-1][j])
                else:
                    B[i][j]=B[i-1][j]
        for i in range(1,N+1):
            line=""
            for j in range(1,N+1):
                line+=[".", "E"][B[i][j]]
            print line
        print "\n",