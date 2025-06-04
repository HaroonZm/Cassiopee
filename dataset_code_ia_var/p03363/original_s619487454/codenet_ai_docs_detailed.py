def c(a, b):
    """
    Calcule le coefficient binomial 'a choose b', c'est-à-dire le nombre de combinaisons possibles
    pour choisir b éléments parmi a sans répétition et sans ordre.

    Args:
        a (int): Nombre total d'éléments.
        b (int): Nombre d'éléments à choisir.

    Returns:
        int: Le nombre de combinaisons possibles.
    """
    u = 1
    # Multiplie les entiers de (a - b + 1) à a pour obtenir le numérateur du coefficient binomial.
    for i in range(a - b + 1, a + 1):
        u *= i
    # Divise par le produit des entiers de 1 à b pour obtenir le dénominateur.
    for i in range(1, b + 1):
        u //= i
    return u

def main():
    """
    Lit un tableau d'entiers et calcule le nombre de paires d'indices (i, j) (i < j)
    de sorte que la somme des éléments entre les indices i et j soit zéro.
    Affiche le résultat.
    """
    # Lecture de la taille du tableau d'entiers à traiter
    n = int(input())
    # Lecture de la liste d'entiers et création du tableau 'a'
    a = list(map(int, input().split()))
    
    # Génère la liste des sommes cumulées de 'a' pour tous les préfixes (y compris le préfixe vide).
    # Les sommes cumulées servent à calculer efficacement les sommes des sous-tableaux.
    b = [a[0]]
    for i in range(n - 1):
        b.append(b[-1] + a[i + 1])
    # Ajoute une valeur supplémentaire correspondant au préfixe vide (somme nulle au départ)
    b.append(0)
    # Trie la liste des préfixes pour regrouper les préfixes de même valeur
    b.sort()
    
    cnt = 0    # Compteur pour suivre le nombre d'occurrences consécutives de la même somme cumulée
    ans = 0    # Variable pour stocker le nombre total de paires
    
    # Initialisation de la variable qui retient la valeur courante à comparer
    p = b[0]
    
    # Parcourt la liste triée de sommes cumulées pour compter les doublons
    for i in range(n + 1):
        if b[i] == p:
            # Si la valeur est identique à la précédente, on incrémente le compteur
            cnt += 1
        else:
            # Pour chaque groupe de préfixes de même valeur,
            # on ajoute au total le nombre de paires qu'on peut former dans ce groupe
            p = b[i]
            ans += c(cnt, 2)  # c(cnt, 2) correspond au nombre de façons de prendre 2 indices dans le groupe
            cnt = 1   # Réinitialise le compteur pour le nouveau groupe
    # Après la boucle, on traite le dernier groupe si il y en a plus d'un
    if cnt > 1:
        ans += c(cnt, 2)
    # Affiche le résultat final
    print(ans)

# Exécution du programme principal
if __name__ == "__main__":
    main()