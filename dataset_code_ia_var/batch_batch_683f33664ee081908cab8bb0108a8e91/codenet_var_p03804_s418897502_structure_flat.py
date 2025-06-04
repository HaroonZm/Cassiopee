n, m = map(int, input().split())
a = []
b = []
for i in range(n):
    a.append(input())
for i in range(m):
    b.append(input())
OKFlag = False
i = 0
while i < n * n:
    SPRow, SPColumn = divmod(i, n)
    if SPRow + m - 1 <= n - 1 and SPColumn + m - 1 <= n - 1:
        j = 0
        while j < m * m:
            MPRow, MPColumn = divmod(j, m)
            if a[SPRow + MPRow][SPColumn + MPColumn] == b[MPRow][MPColumn]:
                if MPRow == m - 1 and MPColumn == m - 1:
                    OKFlag = True
                j += 1
                continue
            else:
                break
        i += 1
        continue
    else:
        i += 1
        continue
print("Yes" if OKFlag else "No")