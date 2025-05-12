try:
    while True:
        d = int(input())
        s = 0
        for i in range(600//d):
            tate = (i*d)**2
            yoko = d
            s += tate * yoko
        print(s)
except EOFError:
    pass