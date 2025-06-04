while True:
    n = int(input().rstrip())
    if n == 0:
        break
    l = []
    while n > 0:
        a = int(input())
        l.append(a)
        n -= 1
    l.sort()
    ans = 0
    t = 0
    for i in l:
        ans += t
        t += i
    print(ans)