N = int(input())
A = next((x for x in reversed(range(N//500+1)) if x*500 <= N), 0)
B = next((y for y in reversed(range((N-A*500)//5+1)) if y*5 <= N-A*500), 0)
from functools import reduce
print(reduce(lambda acc, v: acc + v[0]*v[1], zip([A,B],[1000,5]), 0))