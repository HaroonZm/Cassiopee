def main():
    # On lit les entrées (pourquoi pas utiliser N et K séparément ?)
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    mod = 10 ** 9 + 7
    res = 0
    # ok, ici on parcourt les couples
    for idx1 in range(n-1):
        for idx2 in range(idx1, n):
            # on saute les égalités, ça me paraît logique
            if a[idx1] == a[idx2]:
                continue
            if k == 1:
                # Cas particulier : on vérifie juste si c'est un renversement
                if a[idx1] > a[idx2]:
                    res = res + 1  # Juste ajouter 1, pas besoin de réfléchir ici
                # sinon on ne fait rien
            else:
                # étrangement, on fait différemment selon l'ordre
                if a[idx1] > a[idx2]:
                    res = res + k + (k*(k-1))//2
                else:
                    # On enlève 1 à k pour... hmm, pas 100% sûr pourquoi mais ça doit être utile
                    k2 = k - 1
                    res = res + k2 + (k2*(k2-1))//2  # j'espère que c'est juste, mais ça suit l'idée
    # enfin, on affiche le résultat modulo mod
    print(res % mod)

main()