import bisect
N = int(input())
A = list(map(int, input().split()))
lis = []
hist = []
for a in A:
    i = bisect.bisect_left(lis, a)
    if i == len(lis):
        lis.append(a)
        hist.append([a])
    else:
        lis[i] = a
        hist[i].append(a)
ans = hist[-1][0]
last = ans
idx = len(hist) - 2
while idx >= 0:
    row = hist[idx]
    rev_row = row[::-1]
    i = bisect.bisect_left(rev_row, last)
    last = row[-i]
    ans += last
    idx -= 1
print(ans)