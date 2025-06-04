def check_first_last_equal(s):
    """
    Vérifie si le premier et le dernier caractère d'une chaîne sont identiques.

    Paramètres :
        s (str) : La chaîne de caractères à analyser.

    Retourne :
        bool : True si le premier et le dernier caractère sont identiques, sinon False.
    """
    # On compare le premier caractère (s[0]) et le dernier caractère (s[-1]) de la chaîne.
    return s[0] == s[-1]

# Lecture de l'entrée utilisateur depuis la console.
user_input = input("Entrez une chaîne de caractères : ")

# Vérification de la condition et affichage du résultat approprié.
if check_first_last_equal(user_input):
    # Les caractères sont identiques, on affiche "Yes".
    print("Yes")
else:
    # Les caractères sont différents, on affiche "No".
    print("No")