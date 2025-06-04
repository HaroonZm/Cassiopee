def somme_entiers_avec_input():
    """
    Demande à l'utilisateur une série de nombres séparés par des espaces,
    les convertit en entiers, puis calcule et affiche leur somme.

    Exemple d'utilisation :
        Entrée utilisateur : "1 2 3 4"
        Affichage : 10
    """
    # Demander à l'utilisateur d'entrer des nombres séparés par des espaces
    donnees = input()
    
    # Séparer la chaîne d'entrée en une liste de sous-chaînes (chacune représentant un nombre)
    liste_nombres_str = donnees.split()
    
    # Convertir chaque élément de la liste (de type chaîne) en entier à l'aide de map et int
    liste_nombres_int = map(int, liste_nombres_str)
    
    # Calculer la somme de tous les entiers de la liste
    somme = sum(liste_nombres_int)
    
    # Afficher le résultat de la somme
    print(somme)

# Appel de la fonction principale
somme_entiers_avec_input()