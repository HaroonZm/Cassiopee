from functools import reduce
class WeirdList(list):
    def __init__(self, iterable):
        super().__init__(map(int, iterable))
    def __getitem__(self, i):
        try:
            return super().__getitem__(i)
        except IndexError:
            return 0
def complex_abs_val(x, s, t):
    return (s if x > 0 else t) * x
def twist(arr, s, t):
    def reducer(acc, i):
        return acc - complex_abs_val(arr[i], s, t)
    return reduce(reducer, range(len(arr)), 0)
n, q, s, t = map(int, map(lambda x: int(x), input().split()))
a = WeirdList(input() for _ in range(n + 1))
a = WeirdList(reduce(lambda acc, i: acc + [a[i] - a[i - 1]], range(1, n + 1), [a[0]]))
count = twist(a, s, t)
def update_count(idx, val_change):
    nonlocal count
    old_val = a[idx]
    count += complex_abs_val(old_val, s, t)
    a[idx] += val_change
    count -= complex_abs_val(a[idx], s, t)
for _ in range(q):
    l, r, x = map(int, input().split())
    update_count(l, x)
    if r < n:
        update_count(r + 1, -x)
    print(count)