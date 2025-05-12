n = input()
a, b = map(int, raw_input().split())
ca = input()
max = ca / a
cb = [input() for i in range(n)]
sum_b = a
sum_cb = ca
for t in reversed(sorted(cb)):
    sum_b += b
    sum_cb += t
    if max <= sum_cb / sum_b: max = sum_cb / sum_b
    else: break
print max