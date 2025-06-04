from scipy.sparse import csgraph as cg, csr_matrix as csr
with __import__('sys').stdin as f: L=[[*map(int,l.split())]for l in f]
(n,m),X,*D=L; V,E=[],[]
for idx,p in enumerate(D):
 for q in p[1:]: V+=[idx];E+=[q+n-1]
M=csr(( [1]*len(V), (V,E) ), shape=(n+m,n+m))
A=B=None
for _ in [0]:
 R= cg.connected_components(M)[1]
 A=R[:n]
 B=1 in A
s="YNEOS"
print(s[B::2])