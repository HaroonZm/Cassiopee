from functools import reduce
from operator import xor

def recursive_input(n, acc=None):
    if acc is None:
        acc = []
    return acc if n==0 else recursive_input(n-1, acc + [raw_input()])

def to_float_part(x):
    return str(abs(x-int(x)))[1:]

def obscure_neg(b):
    s = 1<<31
    l = [b^s, '-'] if b&s else [b, '']
    return l

n = reduce(lambda x,y:int(x),[input()])
for v in recursive_input(n):
    b,neg = obscure_neg(int(v,16))
    f = pow(2,7)
    a = sum(map(int,[b*1.0//f]))
    r = reduce(str.__add__,[neg, str(a), to_float_part(b*1.0/f)])
    print r