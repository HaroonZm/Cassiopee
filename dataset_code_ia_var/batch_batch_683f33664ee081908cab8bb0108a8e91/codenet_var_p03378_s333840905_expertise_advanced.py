from collections import Counter

n, m, x = map(int, input().split())
clist = list(map(int, input().split()))

counter = Counter(item < x for item in clist)
print(min(counter[True], counter[False]))