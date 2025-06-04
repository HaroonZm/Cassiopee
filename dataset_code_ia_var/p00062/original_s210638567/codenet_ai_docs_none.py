def shorten(f):
    if len(f) == 1:
        return f[0]
    else:
        g = []
        v = f[0]
        for i in f[1:]:
            g.append((v + i)%10)
            v = i
        return shorten(g)

while True:
    try:
        f = list(map(int, list(input().strip())))
        print(shorten(f))
    except EOFError:
        break