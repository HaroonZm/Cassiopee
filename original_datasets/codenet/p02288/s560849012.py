H=int(input())+1
A=[0]+list(map(int,input().split()))
def h(i):
 l=2*i;r=l+1
 g=i
 if l<H and A[i]<A[l]:g=l
 if r<H and A[g]<A[r]:g=r
 if g>i:A[i],A[g]=A[g],A[i];h(g)
for i in range(H//2,0,-1):h(i)
print(' '+' '.join(map(str,A[1:])))