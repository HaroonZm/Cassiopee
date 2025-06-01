while True:
    N,K=map(int,input().split())
    if N==0 and K==0:
        break
    S=list(map(int,input().split()))
    needed=[0]*K
    for _ in range(N):
        B=list(map(int,input().split()))
        for i in range(K):
            needed[i]+=B[i]
    print("Yes" if all(S[i]>=needed[i] for i in range(K)) else "No")