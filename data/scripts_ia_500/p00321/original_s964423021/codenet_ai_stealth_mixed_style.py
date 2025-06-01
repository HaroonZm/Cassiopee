import collections
n,f = [int(x) for x in input().split()]
counter = {}
for _ in range(n):
    data = input().split()
    m = int(data[0])
    arr = sorted(data[1:])
    i = 0
    while i < m:
        j = i + 1
        while j < m:
            pair = (arr[i], arr[j])
            counter[pair] = counter.get(pair, 0) + 1
            j += 1
        i += 1

filtered = list(filter(lambda x: x[1]>=f, counter.items()))
filtered.sort(key=lambda x: x[0])
print(len(filtered))
for pair, count in filtered:
    print(pair[0], pair[1])