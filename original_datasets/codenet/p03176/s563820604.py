def seg_tree_update(n,x):
    ind=2**m-1+n
    tree[ind]=x
    ind=(ind-1)//2
    while ind>=0:
        tree[ind]=max(tree[2*ind+1],tree[2*ind+2])
        ind=(ind-1)//2

def seg_tree_find_max(L,R):
    L,R=2**m-1+L,2**m-1+R
    qqq=0
    while L<R:
        if L%2==0:
            qqq=max(qqq,tree[L])
        if R%2==1:
            qqq=max(qqq,tree[R])
        L//=2
        R=R//2-1
        
    if L==R:
        qqq=max(qqq,tree[L])
    return qqq

N=int(input())
h=list(map(int,input().split()))
a=list(map(int,input().split()))

m=0
while pow(2,m)<N+1:
    m+=1
tree=[0]*(pow(2,m+1)-1)

for i in range(N):
    M=seg_tree_find_max(0,h[i])
    if tree[2**m-1+h[i]]<a[i]+M:
        seg_tree_update(h[i],a[i]+M)

ans=0
for i in range(N+1):
    ans=max(ans,tree[2**m-1+i])

print(ans)