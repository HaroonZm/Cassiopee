n = int(input())
a = list(map(int, input().split()))

counts = {}
for num in a:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

pairs = []
for key in counts:
    if counts[key] >= 2:
        pairs.append((key, counts[key]))

pairs.sort(reverse=True)

if len(pairs) == 0 or (len(pairs) == 1 and pairs[0][1] < 4):
    print(0)
else:
    if pairs[0][1] >= 4:
        print(pairs[0][0] * pairs[0][0])
    else:
        print(pairs[0][0] * pairs[1][0])