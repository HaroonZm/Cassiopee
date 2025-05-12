a,b,c,d = map(int,input().split())
li =[0]*100
for i in range(a,b):
  li[i]+=1
for i in range(c,d):
  li[i]+=1
print(li.count(2))