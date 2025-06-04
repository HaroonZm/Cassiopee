N = int(input())
A = list(map(int, input().split()))

lis = []
hist = []

for a in A:
    i = 0
    while i < len(lis) and lis[i] < a:
        i += 1
    if i == len(lis):
        lis.append(a)
        hist.append([a])
    else:
        lis[i] = a
        hist[i].append(a)

ans = hist[-1][0]
last = ans
for row in hist[-2::-1]:
    row_rev = row[::-1]
    idx = 0
    while idx < len(row_rev) and row_rev[idx] < last:
        idx += 1
    last = row_rev[idx]
    ans += last

print(ans)