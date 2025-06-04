n = int(input())
AZ = list(map(chr, range(97, 123)))
buckets = []
for __ in range(n):
    row = {ch: 0 for ch in AZ}
    for x in input():
        row[x] += 1
    buckets.append(row)
special = {char: (1 << 31) for char in AZ}
for thing in buckets:
    for c in thing:
        special[c] = thing[c] if thing[c] < special[c] else special[c]
y = ""
[ y := y + k * special[k] for k in sorted(special) if special[k] ]
print(y)