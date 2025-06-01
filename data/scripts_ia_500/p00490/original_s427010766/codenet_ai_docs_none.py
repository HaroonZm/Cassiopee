n = int(input())
a, b = map(int, input().split())
ca = int(input())
max_ratio = ca / a
cb = [int(input()) for _ in range(n)]
sum_b = a
sum_cb = ca
for t in reversed(sorted(cb)):
    sum_b += b
    sum_cb += t
    if max_ratio <= sum_cb / sum_b:
        max_ratio = sum_cb / sum_b
    else:
        break
print(max_ratio)