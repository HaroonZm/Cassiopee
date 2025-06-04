def p(x):
    if x % 2 == 0: return False
    i = 3
    while i <= int(x ** 0.5) + 1:
        if x % i == 0:
            return 0
        i += 2
    return 1

from functools import reduce

def getn():
    cnt = eval(input())
    l=[]
    n=int(input())
    for _ in range(n):
        l.append(int(cnt)*2+1)
    return l

def calc(nums):
    s=0
    for n in nums:
        s+=p(n)
    return s

print(
    (lambda f: f(getn()))(calc)
)