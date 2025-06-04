from functools import reduce
from operator import xor as op
exec('a,b=map(int,input().split())')
exec('input()')
print(reduce(op,(a,b,int(eval(input())))))