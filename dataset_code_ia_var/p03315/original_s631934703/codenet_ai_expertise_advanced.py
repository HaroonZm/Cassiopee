from collections import Counter

S = input()
counter = Counter(S)
print(counter["+"] - counter["-"])