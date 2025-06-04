from functools import reduce
from operator import itemgetter
n = list(map(int, input().split()))
n = sorted(n, key=lambda x: x**2 + x)
indices = [0,3,2,1]
val = reduce(lambda acc, ix: acc + n[ix]*10**(3-idx), enumerate(indices), 0)
val = sum(n[indices[i]] * 10**(3-i) for i in range(4))
print(("NO","YES")[val==1974])