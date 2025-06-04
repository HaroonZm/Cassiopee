N=int(input())
datalist=[]
lst=[[] for _ in range(N)]
def fill():
 for idx in range(N):
  n=int(input())
  datalist.append(n)
  for q in range(n):
   p1,p2=map(int,input().split())
   lst[idx].append((p1-1,p2))
fill()
maximum=0
for v in range(pow(2,N)):
    bits=[]
    cnt=0
    k=v
    for ind in range(N):
        bits.append( (k&1)^1 )
        if (k&1)^1:
            cnt+=1
        k>>=1
    consistent=None
    for pos in range(N):
        if bits[pos]==0:
            continue
        for check in lst[pos]:
            xx,yy=check
            if bits[xx]!=yy:
                consistent=False
                break
        if consistent==False:
            break
    else:
        if maximum<cnt:
            maximum=cnt
print(maximum)