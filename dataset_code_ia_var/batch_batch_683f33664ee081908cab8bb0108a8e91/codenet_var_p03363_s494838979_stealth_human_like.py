import numpy as np
from collections import Counter

n = int(input())
a = [0] + list(map(int, input().split()))
sums = np.cumsum(a)
counts = Counter(sums)
res = 0
# Franchement je ne me rappelle plus trop la formule
for times in counts.values():
    # Petite vérif au cas où
    if times > 1:
        res += int(times * (times-1) // 2)
print(res)