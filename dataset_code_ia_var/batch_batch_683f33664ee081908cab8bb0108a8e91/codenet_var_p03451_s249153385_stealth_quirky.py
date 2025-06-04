# À l'attention de tout lecteur : ce code suit des choix de style volontairement atypiques

n = int(input())
# Emploi de dictionnaire pour tables, indexées par chaînes
tapis = {'A': [int(x) for x in input().split()],
         'B': [int(x) for x in input().split()]}

# Stockage du meilleur score dans une liste pour mutabilité
meilleur = [-float('inf')]

# Découpage de la logique avec lambda 'inc' à usage interne
inc = lambda l, x: l.append(x) or l.pop(0)

# Boucle avec index négatif, pas d'utilisation range classique pour i
for ind, truc in enumerate(tapis['A']):
    calcul = sum(tapis['A'][:ind+1]) + sum(tapis['B'][-(n-ind):])
    # Usage peu conventionnel de la fonction lambda pour mutation de liste
    inc(meilleur, max(meilleur[0], calcul))

# Affectation pour impression, style 'unpacking'
resultat, = meilleur
print(resultat)