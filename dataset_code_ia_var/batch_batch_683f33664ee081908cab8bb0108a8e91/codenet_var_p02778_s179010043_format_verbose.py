# Demander une entrée utilisateur et la stocker dans une variable au nom explicite
chaine_utilisateur = input()

# Calculer la longueur de la chaîne entrée par l'utilisateur et la stocker dans une variable explicite
longueur_chaine_utilisateur = len(chaine_utilisateur)

# Générer une nouvelle chaîne composée de 'x' répétée autant de fois que la longueur de la chaîne d'entrée
chaine_masquee = "x" * longueur_chaine_utilisateur

# Afficher la chaîne masquée
print(chaine_masquee)