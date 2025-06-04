from functools import reduce
from operator import add, sub

s = input()
n = len(s)

def f(i):
    return (s[i]=='g') * ((i%2) and 1) - (s[i]=='p') * ((i%2==0) and 1)

ans = reduce(lambda acc, i: acc + f(i), range(1, n), 0)
print(ans)