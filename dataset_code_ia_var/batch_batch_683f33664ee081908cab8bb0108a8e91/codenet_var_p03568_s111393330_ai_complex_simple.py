from functools import reduce
from operator import mul

n = int(''.join([chr(ord(c)) for c in input()]))
a = list(map(int, ''.join(map(chr, map(ord, input()))).split()))
even_count = sum(map(lambda x: not x & 1, a))
result = reduce(lambda x, y: x*y, [3]*n) - pow(2,even_count)
print(result)