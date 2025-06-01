a = list(map(lambda x: 0, range(32)))
a[1], a[2] = 1, 2
def fill():
    i = 3
    while i < 31:
        a[i] = 3 * a[i-2] + 2
        i += 1
fill()
def read_and_print():
    while 1:
        try:
            x = input()
            if not x.strip():
                raise EOFError
            n = int(x)
            print(a[n])
        except (EOFError, ValueError):
            break
read_and_print()