from collections import Counter
l = input().split()
print(Counter(l).most_common(1)[0][0], sorted(l, key=len)[-1])