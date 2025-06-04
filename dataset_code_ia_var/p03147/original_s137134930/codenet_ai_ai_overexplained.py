# Demander à l'utilisateur d'entrer un nombre entier qui sera affecté à la variable n.
# Cela représentera la taille de la liste d'entiers à traiter (par exemple, le nombre de colonnes d'un jardin).
n = int(input())

# Demander une ligne d'entrée à l'utilisateur, la découper en sous-chaînes selon les espaces,
# puis convertir chaque sous-chaîne en entier via map(int, ...).
# Le tout est transformé en une liste via list(), puis on ajoute un zéro à la fin grâce à la concaténation avec [0].
# Le zéro ajouté simplifie la gestion du dernier élément dans les boucles suivantes, pour éviter un IndexError.
h = list(map(int, input().split())) + [0]

# Initialiser la variable 'ans' à zéro. Cette variable va compter le nombre total d'actions réalisées.
ans = 0

# Démarrer une boucle 'while' qui va s'exécuter tant que la somme des éléments de la liste 'h' est strictement positive.
# Cela signifie que tant qu'il reste un entier strictement positif dans 'h',
# on continue de procéder aux opérations définies dans la boucle.
while sum(h):
    # Boucle 'for' classique sur l'entier i allant de 0 à n-1 (n exclus).
    # 'i' représente l'indice courant de la colonne (ou segment) considéré dans 'h'.
    for i in range(n):
        # Vérifier si la valeur à l'indice courant 'h[i]' est strictement supérieure à zéro
        # ET si la valeur suivante 'h[i+1]' vaut exactement zéro.
        # Cela détermine le bord droit d'une séquence (intervalle) consécutive de valeurs positives.
        if h[i] > 0 and h[i+1] == 0:
            # Si c'est le cas, cela signifie qu'on touche la fin d'un segment continu d'entiers positifs.
            # Donc, on augmente de 1 le compteur 'ans' puisqu'on effectue une nouvelle opération sur ce segment.
            ans += 1
        # Mettre à jour la valeur de 'h[i]' : elle devient le max entre zéro et 'h[i]' moins 1.
        # Cela réduit chaque valeur d'une unité (simule une diminution d'épaisseur, d'eau, ou autre),
        # sauf si la valeur était déjà nulle, auquel cas elle reste à zéro.
        h[i] = max(0, h[i] - 1)

# Une fois le 'while' terminé (c'est-à-dire quand tous les éléments de 'h' sont nuls),
# afficher la valeur finale de 'ans', qui correspond au nombre total d'opérations réalisées.
print(ans)