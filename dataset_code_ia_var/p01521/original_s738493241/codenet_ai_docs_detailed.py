def check_x_edges(s):
    """
    Vérifie si la première et la dernière lettre d'une chaîne sont 'x'.

    Args:
        s (str): La chaîne de caractères à vérifier.

    Returns:
        str: 'x' si le premier et le dernier caractère sont 'x', sinon 'o'.
    """
    # On s'assure que la chaîne est non vide avant de vérifier les bords
    if len(s) > 0 and s[0] == 'x' and s[-1] == 'x':
        return 'x'
    else:
        return 'o'

# Demande à l'utilisateur d'entrer une chaîne via la console (version Python 2)
s = raw_input()

# Appelle la fonction et affiche le résultat en fonction des caractères des bords
print check_x_edges(s)