#!/mnt/c/Users/moiki/bash/env/bin/python
def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    c = a % b
    return gcd(b, c)
def lcd(a,b):
    return a*b//gcd(a,b)
from functools import reduce
# N,M = map(int, input().split())
N = int(input())
a = list(map(int, input().split()))

r = reduce(lcd, a)
# print(r)
ans = 0
for ea in a:
    ans += (r-1)%ea
print(ans)