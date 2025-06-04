def get_count():
    """
    Lit trois paires d'entiers représentant des connexions entre quatre noeuds
    (numérotés de 1 à 4), et calcule la fréquence de chaque noeud impliqué dans les connexions.

    Returns:
        list: Une liste de longueur 4 contenant le compte des apparitions pour chaque noeud.
    """
    # Initialise un compteur pour chaque noeud (noeuds 1 à 4 deviennent index 0 à 3)
    cnt = [0] * 4

    # Boucle pour lire trois paires d'entiers, c'est-à-dire trois connections
    for _ in range(3):
        # Lit la paire d'entiers, les convertit en int, et les assigne à a et b
        a, b = tuple(map(int, input().split()))
        # Incrémente le compteur pour chaque noeud impliqué dans la connexion
        cnt[a-1] += 1
        cnt[b-1] += 1

    # Retourne la liste des comptes pour chaque noeud
    return cnt

def main():
    """
    Détermine si tous les noeuds ont un degré d'au plus 2 après avoir lu trois connexions.

    Affiche "YES" si aucune des valeurs du tableau de compte n'atteint 3 ou plus, sinon "NO".
    """
    # Récupère la liste des comptes de chaque noeud après la lecture des connexions
    cnt = get_count()

    # Vérifie si un des noeuds a été impliqué dans au moins trois connexions
    for c in cnt:
        if c >= 3:
            print("NO")
            exit()
    # Si aucun noeud n'a un compte supérieur ou égal à 3, affiche "YES"
    print("YES")

if __name__ == "__main__":
    main()