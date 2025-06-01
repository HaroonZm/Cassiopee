import sys
I=lambda:sys.stdin.read().strip().split('\n')
R=[list(map(int,x.split(',')))for x in I()]
for x in range(1,len(R)):
  W=len(R[x])
  for y in range(W):
    z=y-(W>len(R[x-1]))
    R[x][y]+=max((R[x-1][z*(y>0):z+2]))
print(*R[-1])