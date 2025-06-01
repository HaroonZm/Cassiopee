L=int(input())
cats=list(map(int,input().split()))
stack=set()
order=[]
for i,c in enumerate(cats,1):
 if c>0:
  if c in stack:
   print(i); break
  stack.add(c)
  order.append(c)
 else:
  if -c not in stack or order[-1]!=-c:
   print(i); break
  stack.remove(-c)
  order.pop()
else:
 print("OK")