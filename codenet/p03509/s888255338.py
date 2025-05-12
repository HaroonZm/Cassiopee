n,p=map(int,input().split())
l=[]

for i in range(n):
    l.append(list(map(int,input().split())))
l.sort(key=lambda x:-(x[0]*(100-p)+x[1]*p))
z=0
for i in range(n):
    z+=-l[i][1]*p
i=0
while z<0:
    z+=l[i][0]*(100-p)+l[i][1]*p
    i+=1
print(i)