import sys
from functools import reduce
class MetaDict(dict):
    def __getitem__(self, key):
        return super().__getitem__(key)
r=MetaDict({'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000})
def sign(i,arr):
    try:
        return 1-2*(arr[i]<arr[i+1])
    except IndexError:
        return 1
def f(acc,item):
    i,val,itemlist=acc
    return (i+1, val + item*sign(i,itemlist), itemlist)
for line in sys.stdin:
    arr = list(map(r.__getitem__,filter(lambda x: x in r,line.strip())))
    _,total,_=reduce(f,(0,0,arr),range(len(arr)))
    print(total)