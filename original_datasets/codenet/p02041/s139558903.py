import bisect
N = int(input())
A = list(map(int,input().split()))

lis = []
hist = []

for a in A:
    i = bisect.bisect_left(lis,a)
    if i == len(lis):
        lis.append(a)
        hist.append([a])
    else:
        lis[i] = a
        hist[i].append(a)

ans = last = hist[-1][0]
for row in reversed(hist[:-1]):
    i = bisect.bisect_left(row[::-1], last)
    last = row[-i]
    ans += last
print(ans)