from numpy import*
from scipy.sparse import*
def main():
  f=csgraph.floyd_warshall
  t=int32(open(0).read().split())
  n,m,l=t[:3]
  t=t[3:]
  m*=3
  print('\n'.join(map(str,map(int,clip(f(f(csr_matrix((t[2:m:3],(t[:m:3],t[1:m:3])),(n+1,n+1)),0)<=l)[t[m+1::2],t[m+2::2]],0,n)%n-1))))
main()