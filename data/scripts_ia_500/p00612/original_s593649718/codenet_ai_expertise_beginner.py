while True:
    n = int(input())
    if n == 0:
        break
    s = n // 2
    ans = s
    i = 1
    k = 2
    while i * i < s:
        ans += (n + k - 1) // k
        i = i + 1
        k = k + 2
    ans = ans * 2 - i * i
    if n % 2 == 1:
        ans = ans + 1
    result = (ans + n) * 8
    print(result)