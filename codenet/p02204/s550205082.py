import sys
input = sys.stdin.readline

M,N=map(int,input().split())
A=list(map(int,input().split()))

if M==2:
    ANS0=0
    ANS1=0

    for i in range(N):
        if A[i]%2==i%2:
            ANS0+=1
        else:
            ANS1+=1

    print(min(ANS0,ANS1))

else:
    A.append(10**10)
    count=0
    ANS=0

    for i in range(N+1):
        if A[i]==A[i-1]:
            count+=1
        else:
            ANS+=count//2
            count=1
    print(ANS)