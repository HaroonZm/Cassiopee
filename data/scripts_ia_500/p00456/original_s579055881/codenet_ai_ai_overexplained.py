# Initialisation de la liste W vide, qui va contenir les entiers saisis pour le groupe W
W = []
# Initialisation de la liste K vide, qui va contenir les entiers saisis pour le groupe K
K = []

# Boucle for qui va répéter 10 fois l'opération suivante :
# Pour chaque valeur de i allant de 0 à 9 (inclus), on effectue une itération
for i in range(10):
    # On demande à l'utilisateur de saisir un nombre entier via input()
    # input() renvoie une chaîne de caractères, on convertit cette chaîne en entier avec int()
    # On ajoute cet entier à la liste W grâce à la méthode append()
    W.append(int(input()))

# Boucle for qui va répéter 10 fois l'opération suivante :
# Pour chaque valeur de i allant de 0 à 9 (inclus), on effectue une itération
for i in range(10):
    # On demande à l'utilisateur de saisir un nombre entier via input()
    # input() renvoie une chaîne de caractères, on convertit cette chaîne en entier avec int()
    # On ajoute cet entier à la liste K grâce à la méthode append()
    K.append(int(input()))
    
    # Ici, dans la boucle, on trie la liste W à chaque étape
    # W.sort() trie la liste W directement (tri sur place) sans créer une nouvelle liste
    # L'argument reverse=True signifie que le tri est fait en ordre décroissant (du plus grand au plus petit)
    W.sort(reverse=True)
    
    # Pareil pour la liste K : tri en ordre décroissant
    K.sort(reverse=True)
    
    # Calcul de la somme des 3 premiers éléments de la liste W triée, donc les 3 plus grandes valeurs
    # W[:3] crée une sous-liste contenant les 3 premiers éléments de W
    # sum() additionne tous les éléments de cette sous-liste
    point_W = sum(W[:3])
    
    # Même calcul pour la liste K
    point_K = sum(K[:3])

# Après les deux boucles, on affiche les points calculés pour W et K
# print() affiche les valeurs dans la console séparées par un espace par défaut
print(point_W, point_K)