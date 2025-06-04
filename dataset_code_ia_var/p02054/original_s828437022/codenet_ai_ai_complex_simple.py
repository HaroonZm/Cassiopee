from functools import reduce
import operator

def binarize(x): return int(int(x)%2)

def decider(f):
    return (lambda *a: (lambda s: s("Hom") if s else s("Tem"))((sum(map(binarize, a))>1)))

get_input = (lambda: list(reduce(operator.iconcat, [input().split()], [])))
print((lambda args: decider(binarize)(*args))((lambda :get_input())()))