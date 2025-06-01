_10_ = 10**20
def __main__():
  d,n = map(int,input().split())
  T=[0]+[int(input())for __ in "x"*d]
  A,B,C = [],[],[]
  [A.append(a) or B.append(b) or C.append(c) for (a,b,c) in (map(int,input().split()) for _ in range(n))]
  D=[[0]*n for __ in range(d+1)]
  for i in range(n):
    if not A[i]<=T[1]<=B[i]: D[1][i] = -_10_
  for i in range(2,d+1):
    pD = D[i-1]
    t = T[i]
    for j in range(n):
      cj = C[j]
      if A[j]<=t<=B[j]:
        D[i][j] = max(pD[x]+abs(cj - C[x]) for x in range(n))
  print(max(D[d]))
__main__()