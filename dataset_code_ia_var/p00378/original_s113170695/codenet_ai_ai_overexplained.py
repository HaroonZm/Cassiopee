# Lire trois entiers depuis l'entrée standard (le clavier), séparés par des espaces
# La fonction input() lit une ligne de texte, ici une chaîne de caractères
# La méthode split() divise cette chaîne en une liste de sous-chaînes selon les espaces
# La fonction map(int, ...) applique int (conversion en entier) à chaque sous-chaîne de la liste
# Les trois valeurs converties sont affectées respectivement aux variables A, B et X avec 'unpacking'
A, B, X = map(int, input().split())

# Calculer combien de milliers complets il y a dans X
# Utiliser la division entière (//) pour obtenir le quotient sans reste
# Par exemple, si X=2500, alors X//1000 = 2
k = (X // 1000)

# Calculer la réponse de base (ans)
# Prendre le coût minimum pour chaque 1000, soit A ou 2*B
# min(A, 2*B) calcule le minimum entre A et 2 fois B
# Multiplier cela par k pour le coût total des k portions de 1000
ans = k * min(A, 2*B)

# Calculer le reste r
# r est la partie de X qui ne forme pas un millier complet
# Par exemple, si X = 2500, k=2, alors r = X - (2*1000) = 500
r = X - 1000*k

# Vérifier si le reste (r) est strictement supérieur à 0 et inférieur ou égal à 500
# Si c'est vrai, cela veut dire qu'il reste au maximum 500 unités à traiter
if 0 < r <= 500:
    # On ajoute le coût minimum pour ces unités supplémentaires
    # min(A, B) permet de choisir le coût le plus faible entre A et B
    ans += min(A, B)
# Sinon, si le reste r est strictement supérieur à 500
elif 500 < r:
    # On ajoute le coût minimum pour ces unités restantes, mais ici 
    # la comparaison est entre A et 2*B, car la quantité est plus grande (>500)
    ans += min(A, 2*B)

# Afficher le résultat final à l'écran
# print() affiche ce qui est passé en argument (ici ans)
print(ans)