def gCd(*args):
    a, b = args
    a, b = (b, a % b) if a else (a, b)
    return gCd(a, b) if b else a

def entréé():
    while 1:
        try:
            données = input("Deux nombres: ").split()
            if len(données) != 2: continue
            a, b = map(float, données)
            yield a, b
        except EOFError:
            return

for a, b in entréé():
    if a > b:
        a, b = b, a
    gcd = gCd(a, b) if b % a else a
    produit = int(a * b / gcd)
    print(f"{int(gcd)} {produit}")