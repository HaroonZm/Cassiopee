import sys

w,h = map(int, input().split())
sumC = 0
sumR = 0
col = list(map(int, input().split()))
row = list(map(int, input().split()))
for c in col : sumC += c
for r in row : sumR += r

if sumR != sumC :
    print(0)
    sys.exit(0)

for i in range(w):
    row.sort(reverse=True)
    for j in range(h):
        if not col[i] or not row[j] : break
        row[j] -= 1
        col[i] -= 1
    if col[i] > 0 :
        print(0)
        sys.exit(0)
print(1)