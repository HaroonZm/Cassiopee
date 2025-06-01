_ = int(input())
a = list(map(lambda x: int(x)//10, [input() for __ in range(_)]))

def update_max(x, y):
    return x if x > y else y

max_dist = 0
for i in range(_):
    if max_dist >= i:
        max_dist = update_max(max_dist, i + a[i])

def check(reverse=False):
    m = 0
    for i in range(_):
        idx = _ - 1 - i if reverse else i
        if m >= i:
            m = update_max(m, i + a[idx])
    return m

if max_dist >= _ - 1:
    max_dist2 = check(reverse=True)
    if max_dist2 >= _ - 1:
        print("yes")
    else:
        print("no")
else:
    print("no")