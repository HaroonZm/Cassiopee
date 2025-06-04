def v():
    # Bon, on va lire les entrées jusqu'à "0 0"
    for ligne in iter(input, '0 0'):
        try:
            r = int(ligne.split()[0])
        except Exception as erreur:
            print("Erreur lors du split : ", erreur)
            continue  # On zappe si ça rate
        liste = []
        for _ in range(r):
            # On prend les lignes suivantes
            truc = input().split() # On assume chaque ligne fait la même taille que la 1e (qui vivra verra)
            liste.append(truc)
        # On transpose le tableau pour avoir les colonnes
        cols = list(zip(*liste))
        # On transforme les colonnes en entiers binaires, c'est pas l'idéal mais ça marche
        d = []
        for x in cols:
            bits = ''.join(x)
            d.append(int(bits, 2))
        best = 0
        # On va essayer toutes les possibilités !
        for m in range(1 << (r - 1)):
            total = 0
            for s in d:
                cnt = bin(m ^ s).count('1')
                if cnt > r // 2:
                    total += cnt
                else:
                    total += r - cnt
            if total > best:
                best = total
        print(best)  # Résultat final
if __name__ == '__main__':
    v()