N = int(input())
K = int(input())
mylist=[]
count=0
x = list(map(int, input().split()))

for i in range(N):
    if K-x[i]>=x[i]:
        count=count+x[i]*2
    else:
        count=count+(K-x[i])*2
print(count)