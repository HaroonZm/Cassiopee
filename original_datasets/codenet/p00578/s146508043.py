def sort_key(end):
    if end[1]:
        return end[0]*2+1
    return end[0]*2

n = int(input())
a = [int(i) for i in input().split()]
a.append(0)

ends = []
top = 0
up = True
for i in range(0, n+1):
    if not up and (i == n or a[i+1] > a[i]):
        ends.append((a[i], True))
        ends.append((top, False))
        up = True
    elif i != n and up and a[i+1] < a[i]:
        top = a[i]
        up = False
ends.sort(key=sort_key)
max_overlaps = 0
overlaps = 0
for end in ends:
    if end[1]:
        overlaps += 1
        if overlaps > max_overlaps:
            max_overlaps = overlaps
    else:
        overlaps -= 1
print(max_overlaps)