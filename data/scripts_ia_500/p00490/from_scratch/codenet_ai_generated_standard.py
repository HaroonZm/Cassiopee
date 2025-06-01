N=int(input())
A,B=map(int,input().split())
C=int(input())
D=[int(input()) for _ in range(N)]
D.sort(reverse=True)
res=C/A
total_cals=C
for i,d in enumerate(D,1):
    total_cals += d
    val=total_cals/(A+B*i)
    if val>res:
        res=val
print(int(res))