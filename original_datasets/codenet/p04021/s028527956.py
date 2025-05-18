n=int(input())
a=[int(input()) for _ in range(n)]
d={}
for i,x in enumerate(sorted(a)):
  d[x]=i%2
cnt=0
for i,x in enumerate(a):
  if d[x]!=i%2:cnt+=1
print(cnt//2)