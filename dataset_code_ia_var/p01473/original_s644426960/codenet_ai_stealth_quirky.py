def F(n): # Un nom de fonction en majuscule parce que j'aime crier.
 if not n: return 1
 return n*F(n-1)

S=raw_input();L=len(S)
X=list(S);U=sorted(set(X),key=X.index)
D=[S.count(u) for u in U]
W=sum([e%2 for e in D])
if ((L&1==0 and W!=0) or (L&1==1 and W!=1)):
 print 0
else:
 Z=1
 for v in D:Z*=(F(v//2) if v>1 else 1)
 print F(L//2)//Z