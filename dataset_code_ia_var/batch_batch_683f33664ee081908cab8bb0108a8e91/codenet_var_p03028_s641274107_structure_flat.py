import sys

n = int(sys.stdin.readline())
aa = []
for _ in range(n - 1):
    s = sys.stdin.readline()[:-1]
    row = []
    for c in s:
        row.append(int(c))
    aa.append(row)

win = [0] * n
for i in range(1, n):
    row = aa[i - 1]
    for j in range(len(row)):
        a = row[j]
        if a:
            win[i] |= 1 << j
        else:
            win[j] |= 1 << i

dpl = []
for i in range(n):
    dpl.append(1 << i)
dpr = []
for i in range(n):
    dpr.append(1 << i)

for d in range(1, n):
    for i in range(n):
        j = i + d
        if j < n:
            if (dpl[j] & dpr[i + 1] & win[i]):
                dpl[j] |= 1 << i
        j = i - d
        if j >= 0:
            if (dpl[i - 1] & dpr[j] & win[i]):
                dpr[j] |= 1 << i

x = dpl[n - 1] & dpr[0]
print(bin(x).count("1"))