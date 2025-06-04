def difference_sorted_set_elements():
    """
    Lit deux ensembles d'entiers depuis l'entrée standard, calcule la différence des ensembles (A - B),
    trie le résultat et affiche chaque élément de la différence triée sur une nouvelle ligne.
    """
    # Lecture et ignorance de la première entrée (taille de l'ensemble A), non utilisée
    input()
    
    # Lecture des éléments de l'ensemble A (depuis une ligne), conversion en entiers et création d'un set
    A = set(map(int, input().split()))
    
    # Lecture et ignorance de la troisième entrée (taille de l'ensemble B), non utilisée
    input()
    
    # Lecture des éléments de l'ensemble B (depuis une ligne), conversion en entiers et création d'un set
    B = set(map(int, input().split()))
    
    # Calcul de la différence entre les ensembles A et B
    difference = A - B
    
    # Trie les éléments de la différence dans l'ordre croissant
    sorted_difference = sorted(difference)
    
    # Affiche chaque élément de la différence triée sur une ligne séparée
    for value in sorted_difference:
        print(value)

if __name__ == '__main__':
    # Appel de la fonction principale pour exécuter le programme
    difference_sorted_set_elements()