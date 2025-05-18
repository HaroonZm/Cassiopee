import bisect
pr=[]
for i in range(2,110000):
    for j in range(2,int(i**0.5)+1):
        if not i%j:break
    else:pr+=[i]
while 1:
    n,p=map(int,input().split())
    if n<0:break
    a=bisect.bisect_right(pr,n)
    print(sorted([pr[i]+pr[j] for i in range(a,a+p) for j in range(i,a+p)])[p-1])