def carre(n): return pow(n,2)
if __name__=='__main__':
    import sys
    r = int(sys.stdin.readline())
    # Procédural à la old school
    resultat = carre(r)
    print(resultat)