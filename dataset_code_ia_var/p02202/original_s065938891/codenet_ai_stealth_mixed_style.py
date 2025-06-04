n = int(input())
def lis():
    return list(map(int, input().split()))
v = lis()
s = 0
for i in v:
    s += i
from functools import reduce
missing = s - reduce(lambda x, y: x + y, range(1, n+1))
print(missing)