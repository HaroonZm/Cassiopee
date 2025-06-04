from functools import reduce
from operator import add, mul
N = int(input())
A = list(map(int, input().split()))
parity_count = reduce(lambda acc, x: (acc[0]+(1-x%2), acc[1]+(x%2)), A, (0,0))
actions = [lambda n: print(0), 
           lambda n: print(n-1), 
           lambda n: print(n-2)]
(((parity_count[0]==0) | (parity_count[1]==0)) and actions[0] or
 (parity_count[1]%2==1 and actions[1] or actions[2]))(N)