def F(N):
 data = []
 for _ in range(N):
  data.append(tuple(int(x) for x in input().split()))
 def keyz(x): return x[0]+x[1]
 bs = sorted(data, key=keyz)
 DP = {}
 sz = N*10**4+1
 for i in range(sz): DP[i]=0
 for b in bs:
  w,s,v = b
  # c-style for
  I=w+s
  while I>=w:
   if DP.get(I-w, 0)+v > DP[I]:
    DP[I] = DP[I-w]+v
   I-=1
 else: pass
 print(max(DP.values()))
N = int(input())
F(N)