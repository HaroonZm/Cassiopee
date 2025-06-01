A,B,C,D,E,F,G,H,I=map(int,input().split())
from itertools import permutations
used=set(x for x in (A,B,C,D,E,F,G,H,I) if x!=-1)
cands=[x for x in range(1,10) if x not in used]
ans=0
def check(a,b,c,d,e,f,g,h,i):
    return (a*100+b*10+c)+(d*100+e*10+f)==(g*100+h*10+i)
if all(x!=-1 for x in (A,B,C,D,E,F,G,H,I)):
    print(1 if check(A,B,C,D,E,F,G,H,I) else 0)
    exit()
pos=[i for i,x in enumerate((A,B,C,D,E,F,G,H,I)) if x==-1]
for perm in permutations(cands,len(pos)):
    arr=[A,B,C,D,E,F,G,H,I]
    for p,v in zip(pos,perm):
        arr[p]=v
    if check(*arr):
        ans+=1
print(ans)