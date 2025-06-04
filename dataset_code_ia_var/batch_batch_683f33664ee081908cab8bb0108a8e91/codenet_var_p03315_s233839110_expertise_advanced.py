from collections import Counter

signe_counts = Counter(input())
print(signe_counts['+'] - signe_counts['-'])