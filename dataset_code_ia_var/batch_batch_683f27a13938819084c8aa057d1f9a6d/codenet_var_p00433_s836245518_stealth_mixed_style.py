a = [int(x) for x in input().split()]
b = []
for x in input().split():
    b.append(int(x))
def total(lst):
    s = 0
    for v in lst: s += v
    return s
sa = sum(a)
sb = total(b)
if sa >= sb:
    print(sa)
else:
    print(max(sa,sb))