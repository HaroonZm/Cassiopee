n = int(input())
a = list(map(int, input().split()))

def compute_prefix(lst):
    seq = [lst[0]]
    for x in lst[1:]:
        seq.append(seq[-1] + x)
    return seq

prefix = compute_prefix(a)

res = []
for idx in range(n-1):
    diff = abs(2 * prefix[idx] - prefix[-1])
    res.append(diff)

min_diff = 1000000000
for v in res:
    if v < min_diff:
        min_diff = v

print(min_diff)