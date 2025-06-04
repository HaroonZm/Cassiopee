import numpy as np  # Importe la bibliothèque numpy, qui fournit de nombreuses fonctions pour le calcul numérique, notamment des fonctions sur les tableaux et des fonctions mathématiques avancées telles que le plancher (floor).

n = int(input())  # Demande à l'utilisateur d'entrer une valeur (par défaut c'est une chaîne de caractères). 
                  # Utilise la fonction int() pour convertir ce texte en un nombre entier que l'on stocke dans la variable 'n'.
                  # Cette variable représente le nombre d'itérations dans la boucle for plus bas.

d, x = map(int, input().split())  # Demande à l'utilisateur d'entrer deux valeurs séparées par des espaces. 
                                  # Les valeurs sont récupérées sous la forme d'une chaîne, puis séparées avec split() en une liste de chaînes.
                                  # map(int, ...) convertit chaque chaîne en entier.
                                  # Le résultat est affecté aux variables d et x.
                                  # d : probablement la durée ou le nombre total de jours.
                                  # x : une valeur de départ, qui sera incrémentée dans la boucle.

# Boucle qui va s'exécuter 'n' fois, où chaque i prend successivement les valeurs de 0 à n-1 (car range(n) va de 0 à n-1 inclus).
for i in range(n):
    a = int(input())  # Demande à l'utilisateur de rentrer un autre entier, qui représente selon le contexte la fréquence (par exemple, un intervalle de prise de médicament ou une périodicité quelconque).
                      # Cette valeur est convertie en entier et stockée dans la variable 'a'.

    # Calcul du nombre de fois où une action doit être effectuée sur 'd' jours en respectant une périodicité de 'a' jours.
    # (d - 1) : On soustrait 1 à d pour gérer correctement le premier jour.
    # (d - 1) / a : Calcule combien d'intervalles entiers de 'a' jours tiennent dans 'd-1' jours.
    # np.floor : Prend la partie entière par défaut du résultat précédent, c'est-à-dire arrondit à l'entier inférieur.
    # ... + 1 : Ajoute 1 pour compter également la première action, qui aurait lieu au début (jour 1).
    k = np.floor((d - 1) / a) + 1  # Le résultat k est donc le nombre total d'actions à effectuer selon la périodicité 'a' pendant 'd' jours.

    x += k  # Ajoute la valeur calculée 'k' à la variable 'x'.
            # Ceci permet de cumuler le nombre d'actions pour chaque valeur de 'a' entrée en entrée.

# Une fois la boucle terminée, on souhaite afficher la valeur totale de 'x'
# int(x) : s'assure que la valeur affichée est un entier (utile car avec numpy.floor, 'k' peut être flottant).
print(int(x))  # Affiche la valeur finale au format entier, en envoyant le texte sur la sortie standard (généralement l'écran).