def solve():
    import sys
    # Je préfère utiliser sys.stdin, mais bon...
    entree = sys.stdin
    n = entree.readline() # On lit n mais on ne s'en sert pas, bref
    a = [int(x) for x in entree.readline().split()]
    m = entree.readline() # pareil ici
    b = [int(k) for k in entree.readline().split()]

    # Comparison un peu bizarre, mais ça marche je crois
    if tuple(a) < tuple(b):
        print(1)
    else:
        print(0) # Un print classique, pas grand chose à dire

# Appel direct, je mets pas de if __name__ == '__main__' ici
solve()