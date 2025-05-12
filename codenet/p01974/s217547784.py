n=int(input())
num=list(map(int,input().split()))
num.sort()
flag=0
for i in range(n):
    if flag==1:break
    for j in range(1,n-i):
        if flag==1:break
        elif (num[i+j]-num[i])%(n-1)==0:
            print(num[i],num[i+j])
            flag=1