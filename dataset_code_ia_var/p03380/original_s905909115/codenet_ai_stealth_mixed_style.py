n = int(input())
a = []
for tok in input().split():
    a.append(int(tok))
a.sort()
a = list(reversed(a))
def get_middle(x): return x/2
m = a[0]
half = get_middle(m)
def find_closest(lst, h):
    r = lst[1]
    i = 1
    while i < len(lst):
        if abs(h - lst[i]) < abs(h - r):
            r = lst[i]
        i += 1
    return r
r = find_closest(a, half)
print(m, r)