def somme_deux_entiers():
    """
    Lit à chaque itération une ligne d'entrée utilisateur contenant deux entiers séparés par des espaces,
    calcule et affiche leur somme. Le traitement continue tant qu'aucune exception n'est levée (ex: entrée vide ou invalide).

    Fonctionne en boucle jusqu'à ce qu'une entrée invalide ou vide soit fournie, auquel cas la boucle se termine.
    Compatible avec Python 2. Pour Python 3, remplacer 'raw_input' par 'input' et adapter 'print'.
    """
    while True:
        try:
            # Lit une ligne depuis l'utilisateur et la découpe en éléments avec split()
            # map(int, ...) convertit chaque élément en entier
            inpt = map(int, raw_input().split())
            # Affiche la somme des deux premiers entiers de la liste
            print inpt[0] + inpt[1]
        except:
            # Si une exception survient (ex: IndexError, ValueError ou EOF), on quitte la boucle
            break

# Appel de la fonction principale
somme_deux_entiers()