N=200020
a=[0]*N
n=int(input())
for _ in range(n): a[sum(map(int,input().split()))]+=1
for i in range(N-1):
    a[i+1]+=a[i]//2
    a[i]&=1
    if a[i]:
        print(i,0)