n = int(input())
a = [int(x) for x in input().split()]
s = 0
for elem in a:
    s += elem
ave = s / n

class Holder:
    pass

h = Holder()
h.ans = None
h.min_diff = None

for idx, val in enumerate(a):
    diff = abs(ave - val)
    if h.min_diff is None or diff < h.min_diff:
        h.ans = idx
        h.min_diff = diff

print((lambda x: x)(h.ans))