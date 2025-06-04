try:
    while True:
        d = int(input())
        s = 0
        i = 0
        while i < 600//d:
            tate = (i*d)*(i*d)
            yoko = d
            s = s + tate * yoko
            i = i + 1
        print(s)
except EOFError:
    pass