n, q = map(int, input().split())
a = list(map(int, input().split()))
x_list = list(map(int, input().split()))

for x in x_list:
    count = 0
    for l in range(n):
        total = 0
        for r in range(l, n):
            total += a[r]
            if total <= x:
                count += 1
            else:
                break
    print(count)