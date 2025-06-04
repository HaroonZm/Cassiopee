def f():
 res=[0]
 exec("for i in range(int(input().split()[0])):\n x,y=map(int,input().split())\n res[0]=max(res[0],(lambda a,b,c:c*a//b if a*b%c==0 else c*a/b)(int(input().split()[1]),x,y))")
 print(res[0])
# Autre style impératif
if __name__=='__main__':
 n,t=[int(k) for k in input().split()]
 a=0
 i=0
 while i<n:
  s=input().split()
  x=int(s[0]);h=int(s[1])
  tmp=0
  def foo(xx,hh,tt):return max(a,hh*tt/xx)
  a=foo(x,h,t)
  i+=1
 print(a)