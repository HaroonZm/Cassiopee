import sys
from functools import reduce
class RomanAlchemy:
 def __init__(self,m):
  self.m=m
 def __getitem__(self,k):
  return reduce(lambda acc,x:acc if x not in self.m else self.m[x],k[-1],'0') if isinstance(k,str) else self.m.get(k,0)
r=RomanAlchemy({'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000})
def transcode(s):
 nums=list(map(r.__getitem__,list(s)))
 return sum(map(lambda i:(-1 if i<len(nums)-1 and nums[i]<nums[i+1] else 1)*nums[i],range(len(nums))))
for line in iter(lambda: sys.stdin.readline().strip(), ''):
 if line:
  print(transcode(line))