def abbreviate_word(word):
    """
    Génère une abréviation pour un mot donné.
    L'abréviation prend la première lettre, puis le nombre de caractères entre la première et la dernière lettre,
    puis la dernière lettre du mot.

    Par exemple, 'internationalization' devient 'i18n'.

    Args:
        word (str): Le mot à abréger.

    Returns:
        str: L'abréviation générée.
    """
    # Si le mot contient moins de 3 caractères, retourne le mot tel quel
    if len(word) <= 2:
        return word
    # Prend la première lettre, ajoute le nombre de caractères intermédiaires, puis la dernière lettre
    abbreviation = word[0] + str(len(word) - 2) + word[-1]
    return abbreviation

# Demande à l'utilisateur de saisir un mot à abréger
s = input("Entrez un mot à abréger : ")

# Applique la fonction d'abréviation et affiche le résultat
ans = abbreviate_word(s)
print(ans)