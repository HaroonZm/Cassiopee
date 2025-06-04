from functools import reduce
from itertools import takewhile, count

a = list(map(int, input().split()))

gen = (a[0] * 2**i for i in count(0))
ans = sum(1 for _ in takewhile(lambda x: x <= a[1], gen))

print(ans)