N=int(input())
Q=int(input())
i=0
while i<Q:
    x,y=map(int,input().split())
    res=(min(x-1,N-x,y-1,N-y)%3)+1
    print(res)
    i+=1