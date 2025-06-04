from functools import reduce
from itertools import product, islice

def take1(it): return next(islice(it,1,None))

op = lambda a,b: (a+b+360*reduce(lambda x,y:x or y,map(lambda x:x>180,[abs(a-b)])))/2%360

print(take1(map(lambda ab: op(*ab), product([int(input())],[int(input())]))))