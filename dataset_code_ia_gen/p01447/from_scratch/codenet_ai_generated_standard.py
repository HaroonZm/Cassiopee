N=int(input())
cnt=0
while N>1:
    N=(N+2)//3
    cnt+=1
print(cnt)