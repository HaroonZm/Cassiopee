def can_rearrange_array(N, a):
    """
    Détermine si un tableau d'entiers peut être réarrangé selon des contraintes spécifiques.

    Pour chaque nombre du tableau :
      - Les multiples de 4 ajoutent 2 au compteur 'now'
      - Les autres nombres pairs ajoutent 1 à 'now'
      - Les nombres impairs n'affectent pas le compteur

    Critère d'acceptation :
      - Si N est impair, 'now' doit être au moins égal à N-1
      - Si N est pair, 'now' doit être au moins égal à N

    Args:
        N (int): Le nombre d'éléments dans le tableau.
        a (List[int]): Le tableau d'entiers.

    Returns:
        str: "Yes" si la condition est satisfaite, sinon "No".
    """
    now = 0  # Initialise le compteur qui mesure la "force de pairité" du tableau

    # Parcourt tous les éléments du tableau
    for i in range(N):
        if a[i] % 4 == 0:
            # Un multiple de 4 compte pour 2 points
            now += 2
            continue  # Passe à l'élément suivant directement
        if a[i] % 2 == 0:
            # Un nombre pair mais pas multiple de 4 compte pour 1 point
            now += 1
        # Les nombres impairs ne modifient pas le compteur

    # Vérifie la condition selon que N soit pair ou impair
    if N % 2 == 1:
        # N est impair : 'now' doit être au moins N-1
        if now >= N - 1:
            return "Yes"
        else:
            return "No"
    else:
        # N est pair : 'now' doit être au moins N
        if now >= N:
            return "Yes"
        else:
            return "No"

def main():
    """
    Lit les entrées, appelle la fonction principale et affiche la sortie.
    """
    # Lecture du nombre d'éléments
    N = int(input())
    # Lecture et conversion en liste d'entiers
    a = list(map(int, input().split()))
    # Appelle la fonction et affiche le résultat
    result = can_rearrange_array(N, a)
    print(result)

# Point d'entrée du script
if __name__ == "__main__":
    main()