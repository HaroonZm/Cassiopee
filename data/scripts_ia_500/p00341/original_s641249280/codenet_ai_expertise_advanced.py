from collections import Counter

e = list(map(int, input().split()))
print("yes" if all(v == 1 for v in map(lambda x: len(set(x)), (e[i:i+4] for i in (0,4,8)))) else "no")