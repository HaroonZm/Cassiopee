id1=lambda:input()
id2=lambda:map(int,id1().split())
Q=1
while Q:
 for S in [int(id1())]:
  if not S:Q=0;break
  dm=[-1,-1]
  for Z in range(S):
   P,D,E=id2()
   if D+E>dm[1]:dm=[P,D+E]
  print(*dm)