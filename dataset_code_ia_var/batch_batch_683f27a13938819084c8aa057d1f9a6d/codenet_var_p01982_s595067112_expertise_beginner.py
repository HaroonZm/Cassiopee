while True:
    n, l, r = input().split()
    n = int(n)
    l = int(l)
    r = int(r)
    if n == 0 and l == 0 and r == 0:
        break
    a = []
    for i in range(n):
        num = int(input())
        a.append(num)
    cnt = 0
    for x in range(l, r + 1):
        is_divisible = False
        for i in range(n):
            if x % a[i] == 0:
                is_divisible = True
                break
        if (i + 1) % 2 == 1 and is_divisible:
            cnt = cnt + 1
        elif not is_divisible:
            if n % 2 == 0:
                cnt = cnt + 1
    print(cnt)