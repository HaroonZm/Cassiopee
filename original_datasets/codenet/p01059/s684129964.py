n,m=map(int,input().split(" "))
a=list(map(int,input().split(" ")))
print(max(a[0]-1,n-a[-1],*[(a[i+1]-a[i])//2 for i in range(m-1)]))