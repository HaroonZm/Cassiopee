from functools import reduce
from operator import mul

lst1 = list(map(lambda x: x<<0, [1,3,5,7,8,10,12]))
lst2 = list(filter(lambda x: x%2==0 or x==9, range(4,12)))
lst3 = [reduce(lambda a,b:a|b, [2])]

x, y = map(int, __import__('sys').stdin.readline().split())

sublists = [lst1, lst2]
membership = lambda v: tuple(any(v==z for z in sub) for sub in sublists)
indicator = tuple(membership(x)), tuple(membership(y))

if any(all(z) for z in zip(*indicator)):
    print(''.join(chr(89+i) for i in range(2)))
else:
    print(''.join([chr(78),chr(111)]))