a1,b1=map(int,input().split())
a2,b2=map(int,input().split())
a3,b3=map(int,input().split())
l=[a1,a2,a3,b1,b2,b3]
L=[]
for i in range(1,5):
  L.append(l.count(i))
L.sort()
if L==[1,1,2,2]:print('YES')
else:print('NO')