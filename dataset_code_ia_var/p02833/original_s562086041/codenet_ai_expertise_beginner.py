n = int(input())

if n < 10:
    print(0)
    exit()

if n % 2 == 1:
    print(0)
    exit()
else:
    ans = n // 10
    tmp = 10
    while n // tmp > 0:
        tmp = tmp * 5
        ans = ans + (n // tmp)
    print(ans)