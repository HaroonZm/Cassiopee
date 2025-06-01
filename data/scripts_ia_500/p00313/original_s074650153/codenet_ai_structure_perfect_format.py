n=int(input())
a=list(map(int,input().split()))
del a[0]
b=list(map(int,input().split()))
del b[0]
c=list(map(int,input().split()))
del c[0]
count=0
for i in range(n):
    i+=1
    if (i in c) and ((i not in a) or (i in b)):
        count+=1
print(count)