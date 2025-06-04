# Demander à l'utilisateur de saisir une chaîne de caractères via le clavier.
# La fonction input() attend que l'utilisateur tape une entrée et appuie sur "Entrée".
user_input = input()

# Convertir la chaîne de caractères (user_input) en une liste de chacun des caractères qui la composent.
# On utilise la fonction list() pour transformer la chaîne en liste, chaque caractère de la chaîne devient un élément de la liste.
input_list = list(user_input)

# Créer un ensemble (set) à partir de la liste de caractères.
# Un ensemble est une collection non ordonnée d’éléments uniques : les doublons sont supprimés automatiquement.
unique_chars = set(input_list)

# Vérifier si le nombre d'éléments distincts dans l'ensemble unique_chars est 3 ou 1.
# La fonction len() retourne le nombre d'éléments dans l'ensemble.
if len(unique_chars) == 3 or len(unique_chars) == 1:
    # Si la longueur est exactement 3 (trois directions différentes) ou 1 (même direction répétée), alors afficher 'No'.
    print('No')
# Vérifier si tous les caractères 'N', 'S', 'E' et 'W' sont présents dans l'ensemble unique_chars.
elif 'N' in unique_chars and 'S' in unique_chars and 'E' in unique_chars and 'W' in unique_chars:
    # Si tous les éléments sont présents, les quatre directions sont couvertes, afficher 'Yes'.
    print('Yes')
# Sinon, vérifier si l'ensemble contient exactement 2 éléments différents.
elif len(unique_chars) == 2:
    # Premier cas : vérifier si les deux éléments sont précisément 'N' et 'S'.
    if 'N' in unique_chars and 'S' in unique_chars:
        # Si vrai, alors ce sont les deux directions opposées nord et sud, afficher 'Yes'.
        print('Yes')
    # Deuxième cas : vérifier si les deux éléments sont précisément 'W' et 'E'.
    elif 'W' in unique_chars and 'E' in unique_chars:
        # Si vrai, alors ce sont les deux directions opposées ouest et est, afficher 'Yes'.
        print('Yes')
    else:
        # Si ce ne sont ni ('N' et 'S') ni ('W' et 'E'), afficher 'No'.
        print('No')
else:
    # Si aucun des cas précédents n'a été satisfait, afficher 'No'.
    print('No')