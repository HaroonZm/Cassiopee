n = int(input())
a = list(map(int, input().split()))
safe = set()
i = 0
while i < n - 1:
    j = i + 1
    while j < n:
        pro = a[i] * a[j]
        num = pro
        digit = []
        k = 1
        while k <= 9:
            digit.append(num % (10 ** k) // (10 ** (k - 1)))
            k += 1
        while len(digit) > 1 and digit[-1] == 0:
            digit.pop()
        if len(digit) == 1:
            safe.add(pro)
        else:
            flag = True
            t = 0
            while t < len(digit) - 1:
                if digit[t + 1] - digit[t] != -1:
                    flag = False
                    break
                t += 1
            if flag:
                safe.add(pro)
        j += 1
    i += 1
if safe:
    print(max(safe))
else:
    print(-1)