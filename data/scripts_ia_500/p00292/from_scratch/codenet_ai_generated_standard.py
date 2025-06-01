N=int(input())
for _ in range(N):
    K,P=map(int,input().split())
    print(K%P if K%P!=0 else P)