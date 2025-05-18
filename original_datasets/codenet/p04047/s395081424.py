n=int(input())
a=list(map(int,input().split()))
a.sort()
b=a[::2]
print(sum(b))