from bisect import bisect_left
def input_int(): return int(input())
def input_list(): return [int(x) for x in input().split()]
N=input_int()
arr=input_list()
arr.sort()
maximum = arr[-1]
half, ceil_half = maximum // 2, maximum // 2 + 1
get_idx = lambda v: bisect_left(arr, v)
indices = []
for value in (half, ceil_half):
    idx = get_idx(value)
    for d in (0, -1, 1):
        pos = idx+d
        if 0 <= pos < N and arr[pos] != maximum:
            indices += [pos]
found = None
best_diff = None
target_values = [half]
if maximum % 2: target_values.append(ceil_half)
for k in set(indices):
    for mid in target_values:
        if best_diff is None or abs(arr[k]-mid) <= best_diff:
            best_diff = abs(arr[k]-mid)
            found = k
print(f'{maximum} {arr[found]}')