from itertools import permutations
n=int(input())
q=[list(map(int,input().split())) for _ in range(n)]
l=list(range(8))
Q=list(permutations(l,8))
def OK(s):
    a=list(s)
    b=list(s)
    for i in range(len(s)):
        a[i]-=i
        b[i]+=i
    for i,j in enumerate(a[:-1]):
        if j in a[i+1:]:
            return False
    for i,j in enumerate(b[:-1]):
        if j in b[i+1:]:
            return False
    return True
for i in Q:
    chk=i
    for x,y in q:
        if i[x]!=y:
            chk=[]
            break
    if chk:
        if OK(i):
            A=i
            break
ans=[['.']*8 for _ in range(8)]
for i,j in enumerate(A):
    ans[i][j]='Q'
    print(''.join(map(str,ans[i])))