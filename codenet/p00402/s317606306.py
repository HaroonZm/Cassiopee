n=int(input())
house=list(map(int,input().split()))

min=10000
for j in range(2001):
    dis=[]
    for i in range(n):
        dis.append(abs(house[i]-j))
    a=max(dis)
    #print(a)
    if min>a:
        min=a
    else:
        pass
print(min)