X,N=map(int, input().split())
p=list(map(int, input().split()))

if len(p)==0:
    print(X)
    exit()

for i in range(N+1):
    if p.count(X-i)==0:
        print(X-i)
        exit()
    if p.count(X+i)==0:
        print(X+i)
        exit()