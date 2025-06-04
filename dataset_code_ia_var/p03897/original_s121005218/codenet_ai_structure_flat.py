n = int(input())
ans = []
i = 0
while i < n - 1:
    if i % 2:
        ans.append((i, 0))
    i += 1
i = 0
while i < n - 1:
    if i % 6 == 1:
        j = 2
        while j < n:
            if j % 2 == 0:
                ans.append((i, j))
            j += 1
    if i % 6 == 4:
        j = 0
        while j < n:
            if j % 2:
                ans.append((i, j))
            j += 1
    i += 1
j = 0
while j < n:
    if (n - 1 + j) % 2:
        ans.append((n - 1, j))
    j += 1
i = 0
print(len(ans))
while i < len(ans):
    print(ans[i][0], ans[i][1])
    i += 1