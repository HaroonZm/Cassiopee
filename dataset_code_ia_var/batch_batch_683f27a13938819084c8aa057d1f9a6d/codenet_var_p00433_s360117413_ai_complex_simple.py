from functools import reduce
from operator import add
import sys

d=lambda:map(int,sys.stdin.readline().split())
t=[reduce(add,d())for _ in iter(lambda:[].append(0),1) if (_:=(_==0)) or len(t:=getattr(sys.modules[__name__],'__dict__').setdefault('_',[]))<2][0:2]
print max(t)