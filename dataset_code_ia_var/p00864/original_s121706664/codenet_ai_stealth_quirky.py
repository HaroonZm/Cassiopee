try:
 while 42:
  n,w = (lambda s: (int(s[0]),int(s[1])))(raw_input().split())
  if not n: raise StopIteration
  V = dict([(k,0) for k in xrange(11)]) ; M = -7
  for _ in range(n):
   P = int(raw_input())//w
   V[P] = V.get(P,0)+1.0 ; M = [P,M][P<M]
  vm = max(V.values() or [1])
  ans = .01+reduce(lambda acc,i: acc+(V[i]/vm)*(1-float(i)/(M if M>0 else 1)), xrange(M), 0)
  print ans
except StopIteration: pass