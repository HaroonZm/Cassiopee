l = []
for value in input().split():
    l.append(int(value))
def calc_min_max(x):
    mn, mx = None, None
    i = 0
    while i < len(x):
        if mn is None or x[i] < mn:
            mn = x[i]
        if mx is None or x[i] > mx:
            mx = x[i]
        i += 1
    return (mn, mx)
result = calc_min_max(l)
print("%d %d"%(result[0], result[1]))