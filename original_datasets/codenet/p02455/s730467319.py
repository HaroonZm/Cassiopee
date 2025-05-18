S=set()
n=int(input())
for i in range(n):
    q,x=map(int,input().split())
    if q==0:
        if x in S:
            print(len(S))
        else:
            S.add(x)
            print(len(S))
    else:
        x={x}
        if S>=x:
            print(1)
        else:
            print(0)