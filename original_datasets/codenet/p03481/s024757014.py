x,y=map(int,input().split())

num=y//x
cnt=0
while num>=2:
    cnt+=1
    num//=2
print(cnt+1)