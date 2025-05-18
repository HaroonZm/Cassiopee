n,m,d=map(int,input().split())
field=[]
for i in range(n):
    field.append(input())
ans=0
for i in field:
    ren=0
    j=i.split("#")
    for k in j:
        if len(k)>=d:ans+=len(k)-d+1
field_r = [list(x) for x in zip(*field)]
for i in range(m):
    field_r[i]="".join(map(str,field_r[i]))
for i in field_r:
    ren=0
    j=i.split("#")
    for k in j:
        if len(k)>=d:ans+=len(k)-d+1
print(ans)