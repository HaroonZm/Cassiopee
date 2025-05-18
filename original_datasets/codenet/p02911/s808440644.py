n,k,q = map(int,input().split())

pnt=[0]*n
for i in range(q):
    j=int(input())
    pnt[j-1] += 1

for i in range(n):
    if pnt[i]+k-q > 0:
        print("Yes")
    else:
        print("No")