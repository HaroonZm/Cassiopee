def main():
    """
    Point d'entrée du programme. Lit une liste d'entiers depuis l'entrée standard,
    puis affiche le minimum entre le produit des deux premiers entiers et le troisième entier.
    """
    # Lire une ligne de l'entrée standard, la découper en éléments séparés par des espaces,
    # convertir chaque élément en entier et construire une liste 'a'
    a = read_integer_list_from_input()
    
    # Calculer le produit des deux premiers éléments de la liste
    product = a[0] * a[1]
    
    # Prendre le minimum entre ce produit et le troisième élément de la liste
    minimum_value = min(product, a[2])
    
    # Afficher le résultat
    print(minimum_value)

def read_integer_list_from_input():
    """
    Lit une ligne d'entrée utilisateur composée d'entiers séparés par des espaces et renvoie la liste correspondante.

    Returns:
        list[int]: Liste des entiers lus depuis l'entrée standard.
    """
    # Demander la saisie utilisateur, découper la chaîne par espaces, 
    # convertir chaque élément en entier, et construire la liste.
    return list(map(int, input().split()))

# Exécuter la fonction principale si ce fichier est exécuté comme script principal
if __name__ == "__main__":
    main()