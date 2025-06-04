from collections import Counter
S = input()
c = Counter(S)
print(c['+'] - c['-'])