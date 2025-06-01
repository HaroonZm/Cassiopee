n = int(input())
a = list(map(int, input().split()))
a.append(0)

ends = []
top = 0
up = True

for i in range(n + 1):
    if not up:
        if i == n or a[i + 1] > a[i]:
            ends.append((a[i], True))
            ends.append((top, False))
            up = True
    else:
        if i != n and a[i + 1] < a[i]:
            top = a[i]
            up = False

def sort_key(end):
    if end[1]:
        return end[0] * 2 + 1
    else:
        return end[0] * 2

ends.sort(key=sort_key)

max_overlaps = 0
overlaps = 0

for end in ends:
    if end[1] == True:
        overlaps += 1
        if overlaps > max_overlaps:
            max_overlaps = overlaps
    else:
        overlaps -= 1

print(max_overlaps)