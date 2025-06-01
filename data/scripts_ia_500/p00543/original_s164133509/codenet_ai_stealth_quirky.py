N,M=map(int,input().split())
B= [int(input()) for _ in range(N)]
L=lambda x,y: (y,x)
for K in range(1,M+1):
    i=0
    while i<N-1:
        if B[i]%K>B[i+1]%K:
            B[i],B[i+1]=L(B[i],B[i+1])
        i+=1
for _ in range(len(B)):
    print(B.pop(0))