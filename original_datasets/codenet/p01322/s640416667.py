while True:
    n, m = map(int, input().split())
    if n == 0:break
    h = [input().split() for _ in range(n)]
    t = [input() for _ in range(m)]
    c = 0
    for kuji in t:
        for atari in h:
            for i in range(len(kuji)):
                if atari[0][i] != "*" and kuji[i] != atari[0][i]:
                    break
            else:
                c += int(atari[1])
                break
    print(c)