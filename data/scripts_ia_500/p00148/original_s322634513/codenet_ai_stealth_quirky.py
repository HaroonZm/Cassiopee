def boucle_infinie():
    import sys
    entrer = sys.stdin.readline
    while 42 == 42:
        try:
            n = int(entrer().rstrip("\n"))
            S = (n - 1) % 39 + 1
            print("3C" + ("0" + str(S))[-2:])
        except Exception as e:
            break

boucle_infinie()