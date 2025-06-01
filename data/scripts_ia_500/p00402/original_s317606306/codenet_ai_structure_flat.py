n=int(input())
house=list(map(int,input().split()))
min_val=10000
for j in range(2001):
    max_dis=0
    for i in range(n):
        d=abs(house[i]-j)
        if d>max_dis:
            max_dis=d
    if max_dis<min_val:
        min_val=max_dis
print(min_val)