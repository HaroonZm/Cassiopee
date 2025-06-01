while True:
    n = int(input())
    if n == 0:
        break
    ans = 0
    while n <= 500:
        n += 500
        ans += 1
    while n <= 900:
        n += 100
        ans += 1
    while n <= 950:
        n += 50
        ans += 1
    while n <= 990:
        n += 10
        ans += 1
    while n <= 995:
        n += 5
        ans += 1
    while n <= 999:
        n += 1
        ans += 1
    print(ans)