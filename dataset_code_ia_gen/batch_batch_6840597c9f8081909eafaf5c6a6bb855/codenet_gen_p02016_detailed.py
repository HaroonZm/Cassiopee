# Programme qui lit une chaîne de caractères en entrée
# et affiche une sortie spécifique en fonction de la chaîne

# Lecture de l'entrée utilisateur (soit "ani" soit "otouto")
input_str = input()

# Vérification de la valeur de l'entrée
if input_str == "ani":
    # Si l'entrée est "ani", afficher "square1001"
    print("square1001")
elif input_str == "otouto":
    # Si l'entrée est "otouto", afficher "e869120"
    print("e869120")
else:
    # Optionnel : gérer les cas non prévus
    # Ici, on ne fait rien ou on pourrait afficher un message d'erreur
    pass