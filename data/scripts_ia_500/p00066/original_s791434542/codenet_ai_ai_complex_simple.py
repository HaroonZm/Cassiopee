from functools import reduce
from operator import eq
def check(a):
 r=lambda s:[a[i]for i in s]
 f=lambda k:any(map(lambda x:all(map(eq([k]*3,r(x))),[0,1,2,3,4,5,6,7,8][i*3:i*3+3] for i in range(3)))) or all(map(eq([k]*3,r([i, i+3, i+6])),range(3))) or all(map(eq([k]*3,r([0,4,8])))) or all(map(eq([k]*3,r([2,4,6]))))
 return reduce(lambda acc,k:k if f(k) else acc,'d',['o','x'])
while 1:
 try:
  from itertools import permutations as p, chain
  line=list(input())
  _=lambda x,y:all(map(lambda z:z[0]==z[1],zip(x,y)))
  def g(a):
   c=lambda i,j,k:i+j+k
   s=[range(i*3,i*3+3)for i in range(3)]
   t=[range(i,9,3)for i in range(3)]
   d=[range(0,9,4),range(2,7,2)]
   for k in 'ox':
    if any(_([k]*3,[a[n]for n in L]) for L in chain(s,t,d)): return k
   return 'd'
  print(g(line))
 except EOFError:break