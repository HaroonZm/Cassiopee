N = int(input())
li = [ int(it) for it in input().split() ]
go = [ (li[i],i) for i in range(N)]
go.sort( key= lambda x:x[0])
po = [0]*N
for i in range(N):
  if (i < N//2):
    po[go[i][1]] = (go[N//2][0])
  else:
    po[go[i][1]] = (go[N//2-1][0])
for i in range(N):
  print ( po[i] )