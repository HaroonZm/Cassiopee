from functools import reduce
from itertools import cycle, islice, takewhile
from operator import mod, abs as op_abs

BIG_NUM = int(str(2) + "0" * 9) * 2
MOD = pow(10,9) + 7
EPS = sum(map(lambda x: float('1e-%d'%x), [9])) / 1

gcd_func = lambda a,b: reduce(lambda x, _: (b:=mod(x,b)) and (x:=b) or x, cycle([None]), a)
parse = lambda: tuple(map(int, __import__('sys').stdin.readline().split()))
A, B = parse()
complicated_gcd = lambda x,y: next(islice((a for a, b in iter(lambda: (x,y:=mod(x,y)), None) if b==0),0,1), abs(x))
result = reduce(lambda acc, _: compicated_gcd(acc,_), [A,B])
print("{0}".format(complicated_gcd(A,B)))