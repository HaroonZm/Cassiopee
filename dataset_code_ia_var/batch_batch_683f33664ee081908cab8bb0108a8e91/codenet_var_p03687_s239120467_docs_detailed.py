from collections import Counter

# Lecture de la chaîne d'entrée de l'utilisateur
s = input()

def convert(st, toS, cou):
    """
    Transforme récursivement une liste de caractères pour qu'elle soit composée uniquement du caractère cible.

    Args:
        st (list): Liste des caractères à transformer.
        toS (str): Le caractère cible vers lequel transformer toute la liste.
        cou (int): Le compteur de transformations (profondeur de récursion).

    Returns:
        int: Le nombre d'étapes nécessaires pour convertir la liste entière en toS.
    """
    # Vérifie si la liste entière est déjà composée du caractère cible
    if st.count(st[0]) == len(st):
        return cou
    # Parcourt la liste et convertit tous les caractères juste après une occurrence du caractère cible
    for i in range(len(st)):
        if i + 1 < len(st) and st[i + 1] == toS:
            st[i] = toS
    # Appel récursif après avoir retiré le dernier caractère
    return convert(st[:-1], toS, cou + 1)

# Initialisation de la réponse avec une valeur suffisamment grande
ans = 200
# Boucle sur chaque caractère unique dans la chaîne
for j in set(s):
    # Recherche pour chaque caractère le nombre minimal d'étapes de conversion
    ans = min(ans, convert(list(s), j, 0))
# Affiche la réponse minimale trouvée
print(ans)