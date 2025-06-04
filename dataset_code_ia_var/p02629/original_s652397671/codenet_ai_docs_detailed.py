char_list = [chr(ord('a') + num) for num in range(26)]
# Création d'une liste contenant les lettres minuscules de l'alphabet anglais ('a' à 'z').

N = int(input())
# Lecture d'un entier depuis l'entrée standard.

def Base_10_to_n(X, n):
    """
    Convertit un nombre entier X en une représentation sous la forme d'une base n,
    où les chiffres sont mappés à partir de la liste char_list (qui ici correspond à des lettres).
    Utilise une logique spéciale pour gérer les cas où X est un multiple de n, imitant la numérotation des colonnes Excel (mais avec des lettres en minuscules).

    Args:
        X (int): Le nombre entier en base 10 à convertir.
        n (int): La base cible (doit être <= à la longueur de char_list).

    Returns:
        str: La chaîne représentant X dans la base n, où chaque 'digit' est une lettre issue de char_list.
    """
    # Cas où le reste de X/n n'est pas nul et que X est supérieur ou égal à n
    if X % n != 0 and (int(X // n)):
        # Appel récursif pour traiter la partie "quotient" puis ajout du caractère correspondant au reste.
        return Base_10_to_n(int(X // n), n) + str(char_list[((X % n) - 1) % n])
    # Cas où X est un multiple de n et supérieur à n
    elif X % n == 0 and (int(X // n)):
        if X // n == 1:
            # Si le quotient est 1, renvoyer directement la lettre correspondant à 0 (i.e. 'z')
            return str(char_list[((X % n) - 1) % n])
        else:
            # Pour d'autres cas, ajuster X pour éviter de dépasser les bornes et poursuivre la conversion
            return Base_10_to_n(int((X - 1) // n), n) + str(char_list[((X % n) - 1) % n])
    # Cas de base : pour X < n ou lors du dernier chiffre
    return str(char_list[((X % n) - 1) % n])

# Affichage du résultat de la conversion de N en base 26, utilisant les lettres minuscules de 'a' à 'z'.
print(Base_10_to_n(N, 26))