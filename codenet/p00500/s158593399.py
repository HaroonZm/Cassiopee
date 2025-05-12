def main():
    N = int(input())

    a = []
    for _ in range(N):
        a.append(list(map(int, input().split())))

    n = []
    c1 = 0
    for _ in range(3):
        hoge = []
        for x in range(N):
            hoge.append(a[x][c1])
        c1 += 1
        n.append(hoge)

    b = [0] * N
    for x in range(3):
        for y in range(N):
            c2 = 0
            for z in range(N):
                if n[x][y] == n[x][z]:
                    c2 += 1
                else:
                    pass
            if c2 == 1:
                b[y] += n[x][y]

    for x in range(N):
        print(b[x])

if __name__ == "__main__":
    main()