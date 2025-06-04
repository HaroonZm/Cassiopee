def calcul_difference():
    """
    Demande à l'utilisateur de saisir un nombre entier depuis l'entrée standard,
    convertit cette entrée en un entier, puis affiche la différence entre 1110 et ce nombre.

    La fonction ne prend pas d'arguments et ne retourne rien.
    Elle affiche directement le résultat à l'écran.
    """
    # Afficher un message pour inviter l'utilisateur à entrer un nombre entier
    valeur_str = input("Veuillez entrer un nombre entier : ")
    
    # Convertir la chaîne de caractères saisie en entier
    valeur = int(valeur_str)
    
    # Calculer la différence entre 1110 et le nombre entré
    difference = 1110 - valeur
    
    # Afficher le résultat
    print(difference)

# Appel de la fonction principale
calcul_difference()