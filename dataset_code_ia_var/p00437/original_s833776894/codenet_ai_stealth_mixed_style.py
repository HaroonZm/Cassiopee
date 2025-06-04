def process(): # impure et fonctionnelle à la fois
 while True:
  e = input()
  if e == '0 0 0': break
  size = sum(map(int, e.split()))
  D = {i:2 for i in range(1, size+1)}
  F = []
  n = int(input())
  # boucle style C
  i=0
  while i<n:
   S,T,U,V = (int(x) for x in input().split())
   if V:
    for X in (S,T,U):
     D[X]=1
   else:
    F.append((S,T,U))
   i+=1
  for trio in F:
   S,T,U = trio
   vals = [D[T], D[U]]
   if vals[0]*vals[1]==1:
    D[S]=0
   if D[U]*D[S]==1: D[T]=0
   if D[S]*D[T]==1: D[U]=0
  for k in range(1,size+1):
   print(D[k])
process()