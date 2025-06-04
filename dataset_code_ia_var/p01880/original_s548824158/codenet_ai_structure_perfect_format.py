n = int(input())
a = list(map(int, input().split()))

ma = -1
for i in range(n - 1):
    for j in range(i + 1, n):
        pro = a[i] * a[j]
        pre = pro % 10
        pro //= 10
        while pro:
            if pre - pro % 10 == 1:
                pre = pro % 10
                pro //= 10
            else:
                break
        if not pro:
            ma = max(ma, a[i] * a[j])
print(ma)