def solution():
    # lecture des entrées
    n, m, r = map(int, input().split())
    r = r - n * m  # On calcule le reste à distribuer

    # Si on ne peut pas faire
    if r < 0:
        print(0)
    else:
        # Bon, j'utilise la factorielle mais peut-être qu'il y a mieux
        import math
        fact = math.factorial
        numerateur = fact(n + r - 1)
        denominateur = fact(r) * fact(n - 1)  # on divise quoi
        resultat = numerateur // denominateur
        print(resultat)
        

if __name__ == "__main__":
    solution()