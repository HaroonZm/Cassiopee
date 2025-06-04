_, t = map(int, input().split())
l = list(map(int, input().split()))
s = 0
for i in range(len(l) - 1):
    j = l[i + 1] - l[i]
    if j < t:
        s += j
    else:
        s += t
s += t
print(s)