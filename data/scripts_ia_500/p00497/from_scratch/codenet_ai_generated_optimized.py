import sys
input=sys.stdin.readline
N,M=map(int,input().split())
diff=[ [0]*(i+2) for i in range(N+2)]
for _ in range(M):
 a,b,x=map(int,input().split())
 r=a
 c=b
 diff[r][c]+=1
 diff[r+x+1][c]-=1
 diff[r+x+1][c+x+1]-=1
 diff[r][c+x+1]+=1
for r in range(1,N+1):
 for c in range(1,r+1):
  diff[r][c]+=diff[r-1][c]+diff[r][c-1]-diff[r-1][c-1]
cnt=0
for r in range(1,N+1):
 for c in range(1,r+1):
  if diff[r][c]>0: cnt+=1
print(cnt)