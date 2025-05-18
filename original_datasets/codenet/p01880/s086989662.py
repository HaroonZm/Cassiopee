n = int(input())
a = list(map(int, input().split()))

safe = set()
for i in range(n - 1):
    for j in range(i + 1, n):
        pro = a[i] * a[j]

        digit = [pro % (10 ** k) // (10 ** (k - 1)) for k in range(1, 10)]

        while digit[-1] == 0:
            digit = digit[:-1]

        if len(digit) == 1:
            safe.add(pro)
            continue

        flag = True
        for k in range(len(digit) - 1):
            if digit[k + 1] - digit[k] != -1:
                flag = False
                break

        if flag:
            safe.add(pro)

if safe:
    print(max(safe))
else:
    print(-1)