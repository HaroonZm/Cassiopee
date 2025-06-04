n = int(input())
i = 1
while i <= n:
    if (i + 1) * i // 2 >= n:
        ans = []
        j = i
        while j > 0:
            if n - j >= 0:
                n -= j
                ans.append(j)
            j -= 1
        k = len(ans) - 1
        while k >= 0:
            print(ans[k])
            k -= 1
        exit()
    i += 1