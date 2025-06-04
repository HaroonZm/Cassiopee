import re  # On importe le module 're' qui fournit des fonctions pour les expressions régulières (regex) en Python

# On lit un entier depuis l'entrée standard (en général, le clavier) et on le stocke dans la variable 'n'
# L'utilisateur doit entrer ce nombre, qui déterminera combien de lignes supplémentaires on va lire
n = int(input())

# On crée une liste 's' qui va contenir 'n+1' éléments (une de plus que 'n' pour inclure une ligne de référence)
# Pour chaque itération, on va lire une ligne d'entrée et la traiter de manière spécifique

s = [
    # On traite chaque ligne d'entrée ici
    ''.join(
        # On va joindre en une seule chaîne de caractères les éléments transformés
        map(
            # La fonction 'map' va appliquer une fonction de transformation à chaque élément de la liste d'entrée
            lambda x:
                # La fonction lambda va traiter chaque 'x' dans la liste
                # Si le premier caractère de 'x' est un chiffre (compris de '0' à '9')
                '{0:09d}'.format(int(x)) if '0' <= x[0] <= '9'
                # Alors on convertit 'x' en entier puis on le formate en chaîne de 9 chiffres avec des zéros devant au besoin
                # Le format '{0:09d}' signifie : format décimal, largeur 9, complété avec des '0' à gauche
                else x
                # Sinon, si 'x' ne commence pas par un chiffre, on retourne la chaîne inchangée
            ,
            # Maintenant, traitons la chaîne d'entrée :
            # Premièrement, on lit la ligne de l'entrée avec input()
            # Deuxièmement, on utilise re.sub pour entourer chaque groupe de chiffres (\d+) de deux espaces ' '
            # La regex r'\d+' correspond à une ou plusieurs chiffres
            # r' \g<0> ' signifie : remplace le groupe trouvé par ce même groupe entouré d'espaces
            re.sub(r'\d+', r' \g<0> ', input()).split()
            # Après le remplacement, on divise la chaîne par les espaces, donc chaque nombre ou mot devient un élément séparé
        )
    )
    # La compréhension de liste répète ce processus n+1 fois (pour 0 à n inclus)
    for _ in range(n + 1)
]

# Maintenant, on veut comparer chacune des entrées (à partir de la première ligne après la ligne de référence)
# On commence la boucle à 1 (car s[0] est la ligne de référence)
for i in range(1, n + 1):
    # Pour chaque valeur s[i], on la compare à la valeur de référence s[0]
    # L'opérateur '<' compare les deux chaînes lexicographiquement (ordre alphabétique)
    # Si s[i] < s[0], on affiche '-'
    # Sinon (si s[i] >= s[0]), on affiche '+'
    print('-' if s[i] < s[0] else '+')