while True:
    n,k=map(int,raw_input().split())
    if k==0:
        break
    A=[['.' for _ in range(n)] for __ in range(n)]
    k=bin(k-1)[2:].zfill(n/2)
    if n%2==1 or len(k)>n/2:
        print "No\n"
        continue
    for i in range(n/2):
        if k[i]=='1':
            A[0][i*2]='E'
            A[0][i*2+1]='E'
    print ''.join(A[0])
    for i in range(n-1):
        for j in range(n):
            cnt=0
            if i>0 and A[i][j]==A[i-1][j]:
                cnt+=1
            if j>0 and A[i][j]==A[i][j-1]:
                cnt+=1
            if j<n-1 and A[i][j]==A[i][j+1]:
                cnt+=1
            if cnt==1:
                A[i+1][j]=A[i][j]
            elif A[i][j]=='.':
                A[i+1][j]='E'
            else:
                A[i+1][j]='.'
        print ''.join(A[i+1])
    print