from collections import Counter

l = map(int, input().split())
c = Counter(l)
print("YES" if c[5] == 2 and c[7] == 1 else "NO")