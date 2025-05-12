def root(x):
  while p[x]>=0:x=p[x]
  return x
def unite(a,b):
  a,b=root(a),root(b)
  if a!=b:
    if p[a]>p[b]:a,b=b,a
    p[a]+=p[b]
    p[b]=a
n,m,*t=map(int,open(0).read().split())
p=[-1]*n
c=[0]*n
for a,b in zip(*[iter(t)]*2):
  a-=1
  b-=1
  unite(a,b)
  c[a]+=1
  c[b]+=1
a=root(0),root(1)
f=p[a[0]]<p[a[1]]
t=[0,0]
for i in range(n):
  j=root(i)
  if j==a[f]:
    t[f]+=c[i]
  else:
    t[f^1]+=c[i]
    unite(a[f^1],j)
r=0
for i in(0,1):
  n=-p[root(i)]
  r+=n*(n-1)-t[i]>>1
print(r)