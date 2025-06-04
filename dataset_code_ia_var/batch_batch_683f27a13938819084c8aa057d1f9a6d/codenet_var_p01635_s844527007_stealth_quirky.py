from __future__ import print_function
_input=lambda:raw_input()
parse=lambda:map(int,_input().split())
n,t=parse()
x=_input()
for k,v in [('^','**'),('n',str(n))]:x=x.replace(k,v)
try:
    res=eval(x)*t
except:res=float('inf')
print("TLE" if res>1e9 else res)