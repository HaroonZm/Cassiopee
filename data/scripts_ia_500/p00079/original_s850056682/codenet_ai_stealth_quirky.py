def R():
 x=input()
 try:return[list(map(float,x.split(",")))]
 except:return[]
def T(a,b,c):
 return(abs((a[0]-c[0])*(b[1]-c[1])-(a[1]-c[1])*(b[0]-c[0]))/2)
v=[*R()][0]
a=[*R()][0]
b=[*R()][0]
S=T(v,a,b)
while True:
 try:
  a=b
  b=[*R()][0]
  S+=T(v,a,b)
 except:
  break
print(S)