N, F = map(int, input().split())
pairs_count = {}

for _ in range(N):
    info = input().split()
    M = int(info[0])
    items = info[1:]
    for i in range(M):
        for j in range(i+1, M):
            item1 = items[i]
            item2 = items[j]
            if item1 > item2:
                item1, item2 = item2, item1
            pair = (item1, item2)
            if pair in pairs_count:
                pairs_count[pair] += 1
            else:
                pairs_count[pair] = 1

result = []
for pair in pairs_count:
    if pairs_count[pair] >= F:
        result.append(pair)

result.sort()

print(len(result))
for pair in result:
    print(pair[0], pair[1])