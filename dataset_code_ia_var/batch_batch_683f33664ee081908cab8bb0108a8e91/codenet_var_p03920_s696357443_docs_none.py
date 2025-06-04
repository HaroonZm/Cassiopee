n = int(input())
for i in range(1, n + 1):
    if (i + 1) * i // 2 >= n:
        ans = []
        for j in range(i, 0, -1):
            if n - j >= 0:
                n -= j
                ans.append(j)
        print(*ans[::-1], sep="\n")
        exit()