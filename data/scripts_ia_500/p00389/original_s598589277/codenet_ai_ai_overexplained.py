# Lecture de deux valeurs entières séparées par un espace depuis l'entrée standard
# input() lit une ligne de texte (chaîne de caractères) depuis l'entrée utilisateur
# .split() divise cette chaîne en une liste de chaînes en utilisant l'espace comme séparateur par défaut
# [int(i) for i in ...] est une compréhension de liste qui convertit chaque élément de la liste de chaînes en entier
# On affecte donc ces deux entiers respectivement à N et K
N, K = [int(i) for i in input().split()]

# Initialisation d'une variable 'weight' à 1
# Cette variable semble représenter un "poids" ou un compteur utilisé dans la logique suivante
weight = 1

# Initialisation de la variable 'ans' à 1
# 'ans' est vraisemblablement la réponse ou le résultat final qu'on souhaite calculer
ans = 1

# On décrémente N de 1, donc on fait N = N - 1
# Cela pourrait refléter une étape préparatoire au traitement de la boucle
N -= 1

# Boucle tant que N est strictement supérieur à 0
while N > 0:
    # Initialisation de la variable d à 0 à chaque début d'itération
    d = 0

    # Vérification si 'weight' est divisible par K sans reste
    # Le modulo (%) donne le reste d'une division entière
    # Si weight % K == 0, cela signifie que weight est un multiple exact de K
    if weight % K == 0:
        # Si la condition est vraie, on assigne à d le résultat de la division entière weight // K
        # L'opérateur // effectue une division entière (tronquée vers le bas)
        d = weight // K
    else:
        # Sinon, on calcule toujours weight // K (division entière) mais on ajoute 1
        # Cela permet d'arrondir la division vers le haut, équivalent à un ceil de la division réelle
        d = weight // K + 1
    
    # On décrémente N de la valeur calculée d : on retire d de N
    N -= d

    # On augmente weight de cette même quantité d
    weight += d

    # On vérifie si N est toujours supérieur ou égal à zéro (après la décrémentation)
    if N >= 0:
        # Si oui, on incrémente ans de 1
        ans += 1
        
# Une fois la boucle terminée (N <= 0), on affiche la valeur finale de ans
# print() affiche à la sortie standard (généralement l'écran)
print(ans)