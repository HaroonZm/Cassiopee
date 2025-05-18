l=[[0]*1001 for i in range(10)]
l[0][0]=1
for i in range(101):
    for j in range(9,0,-1):
        for k in range(i,1000):
            l[j][k]+=l[j-1][k-i]
while 1:
    n,k=map(int,raw_input().split())
    if n==k==0:
        break
    print l[n][k]