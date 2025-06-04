def find_valid_index(n, t, e, x):
    """
    Recherche le premier index (1-based) dans la liste x où la condition min(r, x[i] - r) <= e
    est satisfaite, où r = t % x[i]. Renvoie cet index ou -1 si aucun n'est trouvé.

    Args:
        n (int): Nombre d'éléments dans le tableau x.
        t (int): Le nombre à utiliser pour le modulo.
        e (int): La tolérance maximale autorisée dans la condition.
        x (list[int]): Liste des diviseurs potentiels.

    Returns:
        int: L'indice (1-based) du premier x[i] satisfaisant la condition, ou -1 si aucun.
    """
    for i in range(n):
        # On calcule le reste de la division de t par x[i]
        r = t % x[i]
        # On vérifie si la condition de tolérance est respectée
        if min(r, x[i] - r) <= e:
            # Si oui, on retourne l'index (1-based)
            return i + 1
    # Aucun élément ne satisfait la condition, on retourne -1
    return -1

def main():
    """
    Fonction principale :
    - Lit l'entrée utilisateur depuis la console,
    - Parse les paramètres n, t, e et la liste x,
    - Appelle la fonction find_valid_index et affiche le résultat.
    """
    # Lecture et découpage de la première ligne pour obtenir n, t, e
    n, t, e = map(int, raw_input().split())
    # Lecture de la deuxième ligne pour la liste x
    x = list(map(int, raw_input().split()))
    # Recherche de l'index valide
    result = find_valid_index(n, t, e, x)
    # Affichage du résultat
    print result

# Point d'entrée du script
if __name__ == "__main__":
    main()