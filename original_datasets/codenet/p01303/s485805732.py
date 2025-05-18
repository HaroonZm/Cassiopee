d=int(input())
for i in range(d):
    X,Y,W,H=map(int,input().split())
    count=0
    n=int(input())
    for j in range(n):
        x,y=map(int,input().split())
        if X<=x<=X+W and Y<=y<=Y+H:count+=1
    print(count)