from collections import defaultdict
res = defaultdict(int)
n = int(input())
i = 0
while i < n:
    parts = input().split()
    p, m = parts[0], parts[1]
    res[p] += int(m)
    i += 1
keys_list = list(res.keys())
keys_list.sort(key=lambda x: len(x))
for key in keys_list:
    print(key, res[key])