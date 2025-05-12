import math
N,M=map(int,input().split())
A=[]
for i in range(1,int(math.sqrt(M))+1):
    if M%i==0:
        if M//i>=N:
            A.append(i)
            if i>=N and M//i>i:
                A.append(M//i)

A.sort()

ans=A[-1]

print(ans)