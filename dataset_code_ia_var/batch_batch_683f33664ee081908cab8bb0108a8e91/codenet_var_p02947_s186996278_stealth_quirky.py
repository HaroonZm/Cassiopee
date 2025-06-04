try:
 N=int(input())
 X=[input()for _ in [0]*N]
 Y={}
 for q in X:
  Q=tuple(sorted(q))
  Y[Q]=Y.get(Q,0)+1
 R=[v for v in Y.values()if v>1]
 S=sum(((n*(n-1))//2 for n in R))
 print(S)
except:
 print(0)