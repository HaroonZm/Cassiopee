n=int(input())
plst=sorted(list(map(int,input().split())))
for i in range(n,0,-1):
    if len([p for p in plst if p>=i])>=i:
        print(i)
        break