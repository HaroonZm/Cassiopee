N,K=list(map(int,input().split()))

if N==0 or K==1:
    print(0)
    exit()

N%=K
print(min(N,abs(N-K)))