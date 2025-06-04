# Importation du module sys, qui fournit l'accès à certaines fonctions utilisées ou maintenues par l'interpréteur Python.
import sys

# Assignation à 'read' de la fonction qui lit l'ensemble du flux d'entrée standard sous forme de chaîne de caractères.
read = sys.stdin.read

# Assignation à 'readline' de la fonction qui lit une ligne du flux d'entrée standard.
readline = sys.stdin.readline

# Lecture de la première ligne d'entrée, suppression des blancs en début/fin, découpage en éléments selon les espaces,
# conversion des éléments en entiers, et dépaquetage pour obtenir la variable 'n' uniquement.
n, = map(int, readline().split())

# Lecture de la chaîne de caractères 's' depuis l'entrée standard avec la fonction input, attendue sur une nouvelle ligne.
s = input()

# Lecture de la chaîne de caractères 't' depuis l'entrée standard avec la fonction input, attendue sur une nouvelle ligne.
t = input()

# Définition d'une constante 'MOD', valant 10 puissance 9 plus 7, utilisée pour prendre le reste lors de calculs afin d'éviter le débordement de grands nombres.
MOD = 10**9 + 7

# Initialisation de la variable 'v' à la valeur 2. Cette variable 'v' sert à mémoriser l'état précédent :
# 2 : état initial, aucune tuile posée
# 0 : la tuile précédente était verticale (1x1, correspond à une seule lettre à la fois)
# 1 : la tuile précédente était horizontale (2x1, couvre deux lettres à la fois)
v = 2

# Initialisation de la variable 'ans' qui contiendra le nombre de façons de poser les tuiles, initialisée à 1 (car il y a au moins une manière de commencer).
ans = 1

# Initialisation de 'i', l'indice de boucle, à 0. Il sert à parcourir les caractères des chaînes 's' et 't' au même rythme.
i = 0

# Démarrage d'une boucle while qui continuera tant que la valeur de 'i' est inférieure à 'n' (le nombre de colonnes de la grille).
while i < n:
    # Si le caractère à la position 'i' est égal dans 's' et 't', cela signifie que l'on peut placer une tuile verticale (1x1).
    if s[i] == t[i]:
        # On avance d'une case dans les chaînes, car la tuile verticale ne couvre que cette position.
        i += 1

        # Si la tuile précédente était verticale (v==0), alors il y a 2 fois plus de façons de placer cette tuile.
        if v == 0:
            ans *= 2

        # Si nous sommes dans l'état initial (aucune tuile encore placée), il y a 3 façons de placer la première tuile verticale.
        if v == 2:
            ans *= 3

        # Le nouvel état devient 0, car la dernière tuile placée est verticale.
        v = 0

        # On prend le reste modulo MOD pour éviter les grands nombres. Cela garantit que 'ans' reste dans la plage des entiers de taille raisonnable.
        ans %= MOD

    # Sinon, cela signifie que les caractères à la position i sont différents, donc une tuile doit recouvrir deux cellules (tuile horizontale 2x1).
    else:
        # On avance de deux cases dans les chaînes, car la tuile horizontale couvre deux positions à la fois.
        i += 2

        # Si la tuile précédente était verticale (v==0), il y a 2 façons possibles de placer la tuile horizontale actuelle.
        if v == 0:
            ans *= 2

        # Si la tuile précédente était horizontale (v==1), il y a 3 façons possibles de continuer avec une autre horizontale.
        if v == 1:
            ans *= 3

        # Si nous sommes dans l'état initial (v==2), il y a 6 façons possibles de disposer deux tuiles horizontales l'une à la suite de l'autre.
        if v == 2:
            ans *= 6

        # Le nouvel état devient 1, car la dernière tuile placée est horizontale.
        v = 1

        # On applique le modulo à nouveau pour éviter les entiers trop grands.
        ans %= MOD

# Après avoir traité toutes les colonnes, on affiche le résultat final (toujours modulo MOD par sécurité).
print(ans % MOD)