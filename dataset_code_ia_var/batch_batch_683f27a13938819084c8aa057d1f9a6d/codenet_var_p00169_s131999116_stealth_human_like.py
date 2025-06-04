def solve():
    # On lit la ligne d'input
    c = list(map(int, input().split()))  # bizarrement l'utilisateur peut mettre plein de chiffres

    c = [min(e, 10) for e in c]      # on va tronquer à 10 au cas où y'a des tricheurs

    if c == [0]:   # cas où rien ?
        return 1

    if len(c) > 21:
        print(0)    # trop de cartes, on arrête tout
        return 0
    else:
        ans = 0
        n = len(c)
        # On boucle sur tous les cas où les as valent 1 ou 11
        for mask in range(0, 1 << n):
            s = 0
            for i in range(n):
                if c[i] == 1:
                    # Bon, là on regarde si on choisit 11 ou 1
                    if ((mask >> i) & 1):
                        s += 11
                    else:
                        s += 1
                else:
                    s += c[i]
            if s <= 21:
                # ok, à ce niveau on met à jour (pas sûr qu'il faille max mais bon)
                ans = max(ans, s)
        print(ans)
        return 0  # apparemment le retour ne sert pas trop (peut-être pour arrêter la boucle)

def main():
    while solve() == 0:
        continue    # au cas où, ça relance solve tant qu'il retourne 0

if __name__ == '__main__':
    main()