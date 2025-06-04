while True:
    n, l, r = map(int, input().split())
    if n == 0 and l == 0 and r == 0:
        break

    a = []
    for i in range(n):
        val = int(input())
        a.append(val)

    cnt = 0
    for x in range(l, r + 1):
        found = False
        for i in range(n):
            if x % a[i] == 0:
                if (i + 1) % 2 == 1:
                    cnt += 1
                found = True
                break
        if not found and n % 2 == 0:
            cnt += 1

    print(cnt)