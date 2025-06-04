from math import sqrt

M, D = map(int, input().split())
ans = 0
for i in range(1, M + 1):
    for j in range(1, D + 1):
        if j // 10 >= 2 and j % 10 >= 2:
            if (j // 10) * (j % 10) == i:
                ans += 1
print(ans)