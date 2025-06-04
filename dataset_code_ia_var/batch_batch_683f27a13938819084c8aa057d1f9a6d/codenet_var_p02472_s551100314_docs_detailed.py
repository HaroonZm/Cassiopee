def main():
    """
    Lit une ligne d'entrée utilisateur contenant des entiers séparés par des espaces,
    convertit chaque valeur en entier, calcule la somme de ces entiers, 
    puis affiche le résultat.

    Aucun paramètre d'entrée ni valeur de retour.
    """
    # Lire une ligne de l'entrée standard (input utilisateur)
    input_line = input()
    # Séparer la chaîne en une liste de sous-chaînes en utilisant l'espace comme séparateur
    string_numbers = input_line.split()
    # Convertir chaque sous-chaîne en entier à l'aide de map et int
    int_numbers = map(int, string_numbers)
    # Calculer la somme de tous les nombres entiers obtenus
    result = sum(int_numbers)
    # Afficher la somme totale des entiers
    print(result)

# Appeler la fonction principale pour exécuter le programme
main()