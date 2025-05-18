d,e=[input().split()for _ in'12'];e[3:5]=e[4],e[3]
t=0
for p in('012345','152304','215043','310542','402351','513240'):
 f=[d[int(j)]for j in p];f[3:5]=f[4:2:-1]
 if f[0]==e[0]:
  f=f[1:5]*2
  for j in range(4):
   if f[j:j+4]==e[1:5]:t=1
print(('No','Yes')[t])