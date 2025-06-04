from collections import Counter

print(sum(v & 1 for v in Counter(input()).values()) // 2)