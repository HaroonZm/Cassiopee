from functools import reduce
from operator import xor

nums = list(map(int, input().split()))
unique = list(filter(lambda z: sum(map(lambda w: w==z, nums))==1, nums))
reduce(lambda _,y: print(y), unique, None)