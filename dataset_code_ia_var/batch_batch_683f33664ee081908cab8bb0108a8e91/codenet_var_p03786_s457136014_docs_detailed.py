def get_minimal_elements_count(n, a):
    """
    Calcule le nombre minimal d'éléments d'une liste après avoir retiré
    le plus grand préfixe dont la somme doublée est inférieure à la valeur du prochain élément.
    
    Args:
        n (int): Le nombre d'éléments dans la liste.
        a (List[int]): La liste des entiers.

    Returns:
        int: Le nombre minimal d'éléments conservés après filtrage.
    """
    # Trier la liste pour faciliter la comparaison séquentielle
    a.sort()
    
    # Initialiser la somme accumulée avec le premier élément
    s = a[0]
    # m suivra la position du dernier index à retirer
    m = 0

    # Parcourir la liste à partir du second élément
    for i in range(1, n):
        # Si la somme des éléments précédents doublée est inférieure à l'élément courant,
        # alors on met à jour 'm' pour indiquer qu'un nouveau préfixe est éliminé
        if s * 2 < a[i]:
            m = i
        # Ajouter l'élément courant à la somme
        s += a[i]
    
    # Le total d'éléments restants est n - m
    return n - m

def main():
    """
    Fonction principale qui lit les entrées utilisateur, effectue le traitement
    et affiche le résultat.
    """
    # Lire le nombre d'éléments depuis l'utilisateur
    n = int(raw_input())
    # Lire la liste des éléments et la convertir vers des entiers
    a = [int(x) for x in raw_input().split()]
    # Calculer et afficher le résultat
    print(get_minimal_elements_count(n, a))

# Appel du point d'entrée du programme
if __name__ == '__main__':
    main()