n,t = map(int, input().split())
a = list(map(int, input().split()))
min_a = a[0]
min_b = 0
cnt = 0
for i in range(1, n):
    min_a = min(min_a, a[i-1])
    if min_b < a[i]-min_a:
        min_b = a[i]-min_a
        cnt = 1
    elif min_b == a[i]-min_a:
        cnt += 1
print(cnt)