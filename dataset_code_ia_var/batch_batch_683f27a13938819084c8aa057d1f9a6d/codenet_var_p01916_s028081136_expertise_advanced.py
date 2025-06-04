from collections import Counter

s = input()
odd_count = sum(v & 1 for v in Counter(s).values())
print(odd_count // 2)