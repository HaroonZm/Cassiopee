N=int(input())
li=list(map(int,input().split()))
g=[]
ix=0
while ix<N:
    g.append( (li[ix], ix) )
    ix+=1
s=g
for j in range(len(s)-1):
    for k in range(j+1,len(s)):
        if s[j][0]>s[k][0]:
            s[j],s[k]=s[k],s[j]
mid_idx=N//2
res=[None]*N
m=0
while m<N:
    curr=s[m]
    if m<mid_idx:
        res[curr[1]]=s[mid_idx][0]
    else:
        res[curr[1]]=s[mid_idx-1][0]
    m+=1
idx=0
while idx<N:
    print(res[idx])
    idx+=1