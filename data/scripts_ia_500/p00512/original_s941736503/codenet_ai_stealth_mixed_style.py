d = dict()
n = int(input())
i = 0
while i < n:
    k, v = input().split()
    d[k] = d.get(k, 0) + int(v)
    i += 1

items = [(len(key), key) for key in d]
items.sort()

list(map(lambda t: print(t[1], d[t[1]]), items))