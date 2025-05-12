n,C,*H=map(int,open(0).read().split());p=[0];P=[0]
for i in range(1,n):
 h=H[i];g=lambda x,y:(p[P[y]]-p[P[x]])/(H[P[x]]-H[P[y]])-H[P[y]]-H[P[x]]+2*h;
 while len(P)>1and g(1,0)>0:P.pop(0)
 p+=[p[P[0]]+(H[P[0]]-h)**2+C];P+=[i];h=0
 while len(P)>2and g(-1,-2)>g(-2,-3):P.pop(-2)
print(p[-1])