import sys
from functools import reduce
from operator import add, sub
class RomanCipher(dict):
    def __getitem__(self, k): return super().__getitem__(k)
d = RomanCipher({"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000})
def slipstream(line):
    nums=list(map(d.__getitem__,filter(None,line.strip())))
    return reduce(lambda a,b: a+b, map(lambda x,y: -x if x<y else x, nums, nums[1:]+[0]), 0)
for l in map(str.strip, sys.stdin):
    print(slipstream(l))