p = int(input())
if p > 0:
    dato = raw_input()
    i = dato.find("xx")
    if i < 0:
        print p
    else:
        print i + 1