def abbreviate_word():
    """
    Lit une chaîne de caractères en entrée utilisateur, 
    puis affiche une version abrégée sous la forme :
    première lettre + nombre de caractères intermédiaires + dernière lettre.
    Exemple : 'localisation' devient 'l10n' car elle compte 12 caractères.
    """
    # Demande à l'utilisateur de saisir une chaîne de caractères
    s = input()
    # Calcule le nombre de caractères entre le premier et le dernier caractère
    n = str(len(s) - 2)
    # Construit la chaîne abrégée : première lettre + nombre calculé + dernière lettre
    result = s[0] + n + s[-1]
    # Affiche le résultat
    print(result)

# Appelle la fonction principale si le script est exécuté directement
if __name__ == "__main__":
    abbreviate_word()