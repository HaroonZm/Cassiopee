# Lire une ligne de l'entrée utilisateur, la découper selon les espaces
# et convertir chaque élément séparé en entier pour obtenir deux valeurs : n et k
# n représente le nombre d'éléments dans la séquence, k est la taille de la sous-séquence à considérer
n, k = [int(item) for item in input().split()]

# Lire une deuxième ligne de l'entrée, la découper en utilisant les espaces,
# puis convertir chaque élément obtenu en entier pour former une liste d'entiers 'a'
# Cette liste contient les n éléments de la séquence principale
a = [int(item) for item in input().split()]

# Initialiser une liste 'asum' de taille (n + 1), remplie de zéros.
# Cette liste servira à mémoriser les sommes préfixées
# asum[i] contiendra la somme des k premiers éléments de la liste a, c'est-à-dire, a[0] + a[1] + ... + a[i-1]
asum = [0] * (n + 1)

# Initialiser une deuxième liste 'aplussum' également de taille (n + 1) et remplie de zéros.
# Cette liste servira à stocker la somme préfixée des valeurs positives de a uniquement
# aplussum[i] correspondra à la somme des max(a[j], 0) pour tous les j de 0 à i-1,
# c'est-à-dire, uniquement la somme des éléments positifs de la séquence jusque-là
aplussum = [0] * (n + 1)

# Parcourir l'ensemble des indices i de 0 à n-1,
# à chaque itération, mettre à jour les valeurs de 'asum' et 'aplussum' à l'indice i+1
for i in range(0, n):
    # La somme préfixée jusqu'à i+1 est la somme jusqu'à i plus l'élément courant a[i]
    asum[i+1] = asum[i] + a[i]
    # La somme préfixée positive jusqu'à i+1 est la somme positive jusqu'à i
    # ajoutée de l'élément courant a[i] si celui-ci est strictement positif, sinon on ajoute zéro
    aplussum[i+1] = aplussum[i] + max(a[i], 0)

# Initialiser les bornes gauche (l) et droite (r) de la fenêtre d'extraction du sous-tableau courant.
# l commence à 1 pour pointer le début du premier sous-tableau (en 1-indexé)
# r pointe à la fin du sous-tableau de taille k, soit k (donc la fenêtre cible est [l, r], inclusif)
l = 1
r = k

# Initialiser la variable 'ans' à zéro pour contenir la meilleure réponse trouvée
ans = 0

# Parcourir toutes les fenêtres de taille k possibles dans la séquence
# Tant que la borne droite de notre fenêtre ne dépasse pas la longueur de la séquence initiale
while r <= n:
    # Calculer la somme des éléments positifs qui ne sont pas dans la fenêtre courante [l, r].
    # Pour cela :
    # ca prend la somme des positifs de toute la séquence (aplussum[n])
    # on retire la somme des positifs depuis le début jusqu'à la position r (exclus)
    # et on ajoute la somme des positifs jusqu'avant l (c'est-à-dire les positifs d'avant la fenêtre)
    lr = aplussum[n] - aplussum[r] + aplussum[l-1]

    # Calculer la somme totale des éléments de la fenêtre courante [l, r]
    # On utilise la méthode de somme préfixée pour obtenir efficacement cette somme
    # En prenant la différence entre la somme préfixée jusqu'à r et celle jusqu'à l-1
    # max(..., 0) garantit que si la somme de la fenêtre est négative, on considère quand même zéro
    mid = max(asum[r] - asum[l-1], 0)

    # Mettre à jour la meilleure réponse trouvée jusqu'ici (ans)
    # en prenant le maximum entre la valeur déjà enregistrée (ans)
    # et la somme entre lr (somme des positifs hors fenêtre) et mid (somme "optimisée" de la fenêtre)
    ans = max(ans, lr + mid)

    # Incrémenter les bornes de la fenêtre pour déplacer la sous-séquence d'une position vers la droite
    l += 1
    r += 1

# Afficher, après avoir vérifié toutes les positions possibles, la meilleure réponse trouvée
print(ans)