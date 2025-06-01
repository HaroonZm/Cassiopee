while True:
    n = int(input())
    if n == 0:
        break
    p = list(map(int, input().split()))
    s = 0
    for x in p:
        s += x
    j = list(map(int, input().split()))
    j.sort(reverse=True)
    ans = s * n
    i = 0
    while i < n - 1:
        s += j[i]
        temp = s * (n - 1 - i)
        if temp > ans:
            ans = temp
        i += 1
    print(ans)