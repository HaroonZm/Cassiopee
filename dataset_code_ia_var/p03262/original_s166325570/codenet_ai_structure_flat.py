import numpy as np
n, x = map(int, input().split())
pos = [int(i) for i in input().split()]
pos.append(x)
pos = np.array(pos)
pos = pos - x
diff = np.abs(np.diff(pos))
import math
from functools import reduce
result = diff[0]
for d in diff[1:]:
    result = math.gcd(result, d)
print(result)