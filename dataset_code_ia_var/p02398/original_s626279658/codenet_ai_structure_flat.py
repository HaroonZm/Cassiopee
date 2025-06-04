a,b,c=map(int,input().split())
cnt=0
k=a
while k<=b:
    if c%k==0:
        cnt+=1
    k+=1
print(cnt)