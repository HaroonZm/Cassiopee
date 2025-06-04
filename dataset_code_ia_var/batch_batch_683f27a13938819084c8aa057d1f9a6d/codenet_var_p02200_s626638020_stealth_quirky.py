n=eval(input())
a=[*map(int,input().split())]
c=[(a[i-1]<a[i]) for i in range(1,n)]
print(sum(c))