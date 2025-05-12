n=input()
l=list(map(int,input().split()))
n=int(input())
for i in range(n):
    q=list(map(int,input().split()))
    li=l[q[1]:q[2]]
    if q[0]==0:
        print(min(li))
    else:
        print(max(li))