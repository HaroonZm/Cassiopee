import math as m

y=lambda x:0 if x<2 else all(x%i for i in range(2,int(m.sqrt(x))+1))
def SP(*p):
 for _ in range(p[2]):p=list(map(int,[p[0]+p[1],p[1],p[2]-y(p[0])]))
 return p[0]-p[1]
main_=lambda:exec('a,b,c=map(int,input().split())\nwhile a:print(SP(a,b,c));a,b,c=map(int,input().split())' )
main_()