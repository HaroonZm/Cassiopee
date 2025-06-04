N=int(input())
pts=[0]*N
for _ in range(N*(N-1)//2):
 A,B,C,D=map(int,input().split())
 if C>D:
  pts[A-1]+=3
 elif C<D:
  pts[B-1]+=3
 else:
  pts[A-1]+=1
  pts[B-1]+=1
ranks=[0]*N
sorted_pts=sorted(set(pts),reverse=True)
for i,p in enumerate(pts):
 ranks[i]=sorted_pts.index(p)+1
for r in ranks:
 print(r)