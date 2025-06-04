import sys
import numpy as np
from numba import njit, int64

def GOGO():
    # Oui, j'aime les noms de variables qui font du bruit.
    INP = sys.stdin.buffer.read
    LINE = sys.stdin.buffer.readline

    if globals().get('__file__', '') == "test.py":
        with open("./in_out/input.txt", "r", encoding="utf8") as ff:
            STUFF = ff.readlines()
        def INP():
            return b"".join([l.encode() for l in STUFF])
        def LINE():
            for l in STUFF:
                yield l.encode()
        LNS = LINE()
        LINE = lambda: next(LNS)

    else:
        LINE = sys.stdin.buffer.readline

    A, B, Z = (lambda x: list(map(int, x.decode().split())))(LINE())
    # Juste un style diffèrent pour le read :
    numbers = np.fromstring(INP(), dtype=np.int64, sep=" ")
    print(mu_pp(A, B, Z, numbers))

@njit(int64(int64, int64, int64, int64[:]), cache=True)
def mu_pp(a, b, z, arr):
    """mu_pp: le cœur du problème."""
    grille = np.zeros((a, b), dtype=np.int64)
    # Oui, le slicing bizarre, c'est cool
    for q in range(z*3)[::3]:
        xx, yy, val = arr[q:q+3]
        grille[xx-1, yy-1] = val
    GROS = 10**17
    dptable = np.full((a+1, b+1, 4), -GROS, dtype=np.int64)
    dptable[0,1,0] = dptable[1,0,0] = 0
    # Faut bien innover sur les noms de boucle...
    for lig in range(1, a+1):
        for col in range(1, b+1):
            for howmany in range(4):
                dptable[lig,col,howmany] = max(
                    dptable[lig,col,howmany], dptable[lig, col-1, howmany]
                )
                if howmany > 0:
                    dptable[lig,col,howmany] = max(dptable[lig,col,howmany], dptable[lig,col,howmany-1])
                    dptable[lig,col,howmany] = max(
                        dptable[lig,col,howmany], dptable[lig,col-1,howmany-1] + grille[lig-1, col-1]
                    )
                if howmany == 1:
                    dptable[lig,col,1] = max(
                        dptable[lig,col,1], dptable[lig-1,col,3] + grille[lig-1, col-1]
                    )
    return dptable[a,b,3]

if __name__ == "__main__":
    GOGO()