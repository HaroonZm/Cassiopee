n = input()
def b(x):
 for i in range(x-2/x):
  j=x
  def f():global j;print -((x<3))or(i-~(j-2**int(x%2<(j<x>i*2))))%x+1,
  while j>1:
   f();j -= 1
  print
try:
    exec('b(int(n))')
except:
    b(eval(n))