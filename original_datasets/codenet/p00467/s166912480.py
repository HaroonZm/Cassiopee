for e in iter(input,'0 0'):
 N,M=map(int,e.split())
 S=[int(input())for _ in[0]*N]
 p=b=1
 for i in range(M):
  d=int(input())
  p+=d
  if N<=p:
   if b:print(-~i);b=0
   continue
  p+=S[~-p]
  if(N<=p)*b:print(-~i);b=0