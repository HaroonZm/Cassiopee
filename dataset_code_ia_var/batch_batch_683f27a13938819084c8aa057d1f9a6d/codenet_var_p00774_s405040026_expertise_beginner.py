def main(n):
    f = []
    for i in range(n):
        line = input().split()
        row = []
        for x in line:
            row.append(int(x))
        f.append(row)
    something_changed = True
    ans = 0
    while something_changed:
        something_changed = False
        for i in range(n):
            to_remove = []
            for k in range(3):
                if f[i][k] == 0:
                    continue
                if f[i][k] == f[i][k + 1] and f[i][k + 1] == f[i][k + 2]:
                    to_remove.append(k)
                    to_remove.append(k + 1)
                    to_remove.append(k + 2)
            if to_remove == []:
                continue
            temp = []
            for x in to_remove:
                if x not in temp:
                    temp.append(x)
            to_remove = temp
            b = f[i][to_remove[0]]
            something_changed = True
            for x in to_remove:
                ans = ans + b
                f[i][x] = 0
        if something_changed:
            for i in range(n-1, -1, -1):
                for k in range(5):
                    x = i
                    while f[x][k]:
                        if x < n - 1:
                            if f[x+1][k] == 0:
                                f[x+1][k] = f[x][k]
                                f[x][k] = 0
                                x = x + 1
                                continue
                        break
    print(ans)

while True:
    n = int(input())
    if n == 0:
        break
    main(n)