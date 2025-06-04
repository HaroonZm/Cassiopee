from collections import Counter

s = input()
counter = Counter(s)
print(counter['+'] - counter['-'])