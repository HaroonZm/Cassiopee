N = int(input())
T = list(map(int,input().split()))
A = list(map(int,input().split()))
H = [0]*N
flag=0

H[0]=T[0]
for i in range(1,N):
    if T[i]!=T[i-1]:
        H[i]=T[i]
    else:
        H[i] = -1*T[i]

H[N-1]=A[N-1]

for i in range(1,N):
    if A[N-i-1]!=A[N-i]:
        if (H[N-i-1]<0 and A[N-i-1] > -1*H[N-i-1]) or (H[N-i-1]>0 and A[N-i-1] > H[N-i-1]):
            flag=1
            break
        H[N-i-1]=A[N-i-1]
    else:
        H[N-i-1]=max(-1*A[N-i-1],H[N-i-1])
if N==1:
    if A[0]==T[0]:
        print(1)
    else:
        print(0)

elif flag==0:
    p = 10**9+7
    out = 1
    for i in range(N):
        if H[i]<0:
            out = out * (-1*H[i]) % p
    print(out)
else:
    print(0)