n = int(input())
if n == 2:
    print(-1)
    exit()
if n % 2 == 1:
    for i in range(n):
        print(" ".join([str((item + i + 1) % n + 1) for item in range(n-1)]))
else:
    for i in range(n):
        ans = [(item + i + 1) % n + 1 for item in range(n-1) if item != n // 2 - 1]
        ans.insert(0, (n // 2 + i) % n + 1)
        if i < n // 2:
            ans[0], ans[1] = ans[1], ans[0]
        print(" ".join([str(item) for item in ans]))