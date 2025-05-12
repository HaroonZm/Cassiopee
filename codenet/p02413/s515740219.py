r,c = map(int, input().split())
s=[]
T=[]
t=0
for k in range(r):
   x = list(map(int, input().split()))
   x.append(sum(x))
   s.append(x)
for i in range(c+1):
   t=0
   for j in range(r):
      t += s[j][i]
   T.append(t)
s.append(T)
for p in range(r+1):
   print(*s[p])