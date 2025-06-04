l = []
for x in input().split():
    l.append(int(x))
def extr(a):
    return min(a), max(a)
m, n = extr(l)
print(f"{m} {n}")