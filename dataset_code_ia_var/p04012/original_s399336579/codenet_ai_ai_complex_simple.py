from collections import Counter
from functools import reduce
w = input()
c = Counter(w)
parities = map(lambda x: x%2, c.values())
ans = reduce(lambda x, y: x|y, parities, 0)
print(('No','Yes')[ans==0])