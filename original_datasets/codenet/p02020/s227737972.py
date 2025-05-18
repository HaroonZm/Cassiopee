N=int(input())
A=list(map(int,input().split()))

A.sort()

if sum(A)%2==0:
    print(sum(A)//2)

else:
    for i in range(N):
        if A[i]%2==1:
            break

    print((sum(A)-A[i])//2)