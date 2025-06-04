n = int(input())
for _ in range(n):
    s, d = map(int, input().split())
    while True:
        if s == d:
            print(0)
            break
        ans = 0
        stack = []
        ss, dd = s, d
        while ss != dd:
            if ss % 2 != 0:
                ans += 1
                ss += 1
            if dd % 2 != 0:
                ans += 1
                dd -= 1
            stack.append((ss, dd, ans))
            ss //= 2
            dd //= 2
        print(ans)
        break