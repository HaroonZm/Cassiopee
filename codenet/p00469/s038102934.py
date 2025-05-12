def s():
 from itertools import permutations as P
 for e in iter(input,'0'):
  n,k=int(e),int(input())
  C=[input()for _ in[0]*n]
  print(len(set(''.join(s)for s in P(C,k))))
if'__main__'==__name__:s()