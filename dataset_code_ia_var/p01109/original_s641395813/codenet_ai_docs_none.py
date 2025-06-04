while True:
    n = int(input())
    if n == 0:
        break
    a = input().split()
    tot = 0
    ans = 0
    for i in a:
        tot += int(i)
    for i in a:
        if (tot / n) >= int(i):
            ans += 1
    print(ans)