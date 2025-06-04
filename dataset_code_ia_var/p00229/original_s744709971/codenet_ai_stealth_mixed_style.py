from sys import stdin

def solve():
    for ligne in stdin:
        briques, rouges, verts, coins, sauts, total = list(map(int, ligne.strip().split()))
        if not (briques or rouges or verts or coins or sauts or total):
            break
        resultat = 100
        # style fonctionnel
        resultat = resultat + 15 * briques + (15 - 2) * 5 * briques
        total -= 5 * briques
        resultat += 15 * rouges + (15 - 2) * 3 * rouges
        total -= 3 * rouges
        resultat += 7 * verts
        resultat += 2 * coins
        total -= sauts
        # boucle while comme accent impératif
        k = 0
        while k < 1:
            resultat -= 3 * total
            k += 1
        print(resultat)

class Lanceur:
    run = staticmethod(solve)

if __name__ == "__main__":
    (lambda f: f())(Lanceur.run)