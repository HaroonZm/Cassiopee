# Demande à l'utilisateur de saisir une valeur entière via la fonction input(), 
# puis convertit cette valeur de chaîne de caractères en entier à l'aide de int().
X = int(input())

# Calcul du nombre de billets de 500 que l'on peut obtenir à partir du montant X :
# L'opérateur // effectue une division entière, c'est-à-dire qu'il donne le quotient sans reste.
# Ensuite, on multiplie ce nombre de billets par 1000, car chaque billet de 500 rapporte 1000 unités.
ans = (X // 500) * 1000

# Mise à jour de la valeur de X pour trouver le reste après avoir utilisé le maximum de billets de 500 :
# L'opérateur % donne le reste de la division entière (modulo).
X = X % 500

# Calcul du nombre de pièces de 5 que l'on peut obtenir à partir du montant restant X.
# On prend à nouveau la division entière pour savoir combien de fois 5 rentre dans X,
# puis on multiplie ce nombre par 5, car chaque pièce de 5 rapporte 5 unités.
ans += (X // 5) * 5

# Affichage du résultat final : le montant total obtenu en utilisant d'abord les billets de 500,
# puis les pièces de 5. La fonction print() affiche la valeur de ans dans la console.
print(ans)