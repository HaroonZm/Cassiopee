data = dict()
n = int(input())
i = 0
while i < n:
    line = input()
    p, val = line.split()
    if p in data:
        data[p] += int(val)
    else:
        data[p] = int(val)
    i += 1

elements = [(len(key), key) for key in data]
elements.sort()

for length, key in elements:
    print(key, data.get(key))