n = int(input())
a = list(map(int, input().split()))
ma = -1
i = 0
while i < n - 1:
    j = i + 1
    while j < n:
        pro = a[i] * a[j]
        temp = pro
        pre = temp % 10
        temp //= 10
        ok = True
        while temp:
            if pre - temp % 10 == 1:
                pre = temp % 10
                temp //= 10
            else:
                ok = False
                break
        if ok and (temp == 0):
            if a[i] * a[j] > ma:
                ma = a[i] * a[j]
        j += 1
    i += 1
print(ma)