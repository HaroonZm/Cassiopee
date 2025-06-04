n,k=map(int,input().split())
w=[int(input()) for _ in range(n)]
left,right=max(w),sum(w)
while left<right:
    mid=(left+right)//2
    count,current=1,0
    for weight in w:
        if current+weight<=mid:
            current+=weight
        else:
            count+=1
            current=weight
    if count<=k:
        right=mid
    else:
        left=mid+1
print(left)