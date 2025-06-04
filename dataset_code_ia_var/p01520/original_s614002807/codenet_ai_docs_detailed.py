def find_valid_index(n, t, e, xlst):
    """
    Parcourt une liste de valeurs et détermine le premier indice (base 1) qui
    satisfait une certaine condition arithmétique liée à t et e.

    Paramètres
    ----------
    n : int
        Nombre d'éléments dans xlst.
    t : int
        Valeur de référence utilisée dans le calcul de la borne supérieure.
    e : int
        Valeur d'erreur/tolérance incluse dans le calcul de la borne.
    xlst : list of int
        Liste des valeurs utilisées comme diviseurs dans la condition.

    Retourne
    -------
    int
        Le premier indice (base 1) qui satisfait la condition, ou -1 si aucun ne la satisfait.
    """
    # Parcours de chaque élément dans xlst avec son indice
    for i, x in enumerate(xlst):
        # Calcul de la borne inférieure pour le coefficient 'a'
        a = (t - e - 1) // x
        # Vérification que la prochaine valeur multiple de x ne dépasse pas la borne supérieure (t + e)
        if (a + 1) * x <= t + e:
            # Retourne l'indice (base 1) si condition satisfaite
            return i + 1
    # Retourne -1 si aucune condition n'est satisfaite
    return -1

def main():
    """
    Fonction principale qui lit les entrées, exécute la logique et affiche le résultat.
    Sollicite les entrées utilisateur, prépare les arguments, puis affiche le résultat du calcul.
    """
    # Lecture et décomposition de la première ligne d'entrée
    n, t, e = map(int, input().split())
    # Lecture des valeurs de xlst à partir de la deuxième ligne d'entrée
    xlst = list(map(int, input().split()))
    # Appel de la fonction principale de recherche d'indice et affichage du résultat
    result = find_valid_index(n, t, e, xlst)
    print(result)

# Exécution du script principal si lancé directement
if __name__ == "__main__":
    main()