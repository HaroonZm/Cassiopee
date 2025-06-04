from collections import Counter

s = input()
pattern1 = ((i % 2 == 0) ^ (ch == '1') for i, ch in enumerate(s))
counts = Counter(pattern1)
print(min(counts[True], counts[False]))