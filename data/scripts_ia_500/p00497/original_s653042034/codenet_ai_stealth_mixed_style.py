def main():
    n, m = (int(x) for x in input().split())
    t = []
    for _ in range(n+2):
        row = [0]*(n+2)
        t.append(row)

    i = 0
    while i < m:
        a, b, x = map(int, input().split())
        a -= 1
        b -= 1
        t[a][b] += 1
        t[a][b+1] -= 1
        t[a+x+1][b] -= 1
        t[a+x+1][b+x+2] += 1
        t[a+x+2][b+1] += 1
        t[a+x+2][b+x+2] -= 1
        i += 1

    for i in range(n+2):
        j = 1
        while j < n+2:
            t[i][j] = t[i][j] + t[i][j-1]
            j += 1

    for col in range(n+2):
        for row in range(1, n+2):
            t[row][col] = t[row][col] + t[row-1][col]

    for row in range(1, n+2):
        for col in range(1, n+2):
            t[row][col] += t[row-1][col-1]

    ans = sum(1 for i in range(n) for j in range(i+1) if t[i][j] != 0)

    print(ans)

main()