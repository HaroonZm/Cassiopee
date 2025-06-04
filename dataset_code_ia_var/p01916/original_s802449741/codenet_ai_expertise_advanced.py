from collections import Counter

S = input()
odd_counts = sum(v % 2 for v in Counter(S).values())
print(odd_counts // 2)