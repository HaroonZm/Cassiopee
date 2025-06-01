from functools import reduce
class MagicList(list):
 def __mul__(s,o):return reduce(lambda x,y:x*y,map(int,s))
 def __rmul__(s,o):return list.__mul__(s,o)
def funky_map(func,iterable):return list(map(func,iterable))
def nested_input_loop(n,func):return [func()for _ in range(n)]
def identity(x):return x
def triple_zero(x):return x=='0 0 0'
def parse_ints(x):return list(map(int,x.split()))
def prod(lst):return reduce(lambda x,y:x*y,lst,1)
def average(lst):return sum(lst)/len(lst)if lst else 0
inputs=iter(iter(input,'0 0 0'))
while True:
 try:
  e=next(inputs)
 except StopIteration:break
 if triple_zero(e):break
 d=MagicList([2]*int(-~sum(parse_ints(e))))
 m=int(input())
 f=[]
 def process_line():return tuple(map(int,input().split()))
 def inner_loop():
  nonlocal d,f
  s,t,u,v=process_line()
  if v:d[s]=d[t]=d[u]=1
  else:f.append((s,t,u))
 list(map(identity,[inner_loop() for _ in range(m)]))
 for s,t,u in f:
  if d[t]*d[u]==1:d[s]=0
  if d[u]*d[s]==1:d[t]=0
  if d[s]*d[t]==1:d[u]=0
 print(*d[1:],sep='\n')