from collections import Counter

l = input().split()
print('yes' if sorted(Counter(l).values()) == [4, 4, 4] else 'no')