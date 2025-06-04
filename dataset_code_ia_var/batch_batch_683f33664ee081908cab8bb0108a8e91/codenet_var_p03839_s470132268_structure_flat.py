from itertools import accumulate

n, k = map(int, input().split())
a = list(map(int, input().split()))
x = []
for i in a:
    if i > 0:
        x.append(i)
    else:
        x.append(0)

ans = 0
acc = [0]
for v in accumulate(x):
    acc.append(v)
aaa = [0]
for v in accumulate(a):
    aaa.append(v)

i = 0
while i <= n - k:
    tmp = acc[i] + acc[-1] - acc[i+k]
    if tmp > ans:
        ans = tmp
    add = tmp + aaa[i+k] - aaa[i]
    if add > ans:
        ans = add
    i += 1

print(ans)