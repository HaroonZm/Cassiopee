# Demander à l'utilisateur de saisir deux entiers séparés par un espace, puis les convertir en entiers.
# 'n' représente le nombre de sommets (ou d'éléments), 'm' le nombre de paires (ou d'arêtes).
n, m = map(int, input().split())

# Créer une liste nommée 'ans' d'une longueur de 'n', initialisée à 0 pour chaque élément.
# Cette liste servira à compter le nombre d'occurrences pour chaque sommet (ou élément).
ans = [0] * n

# Boucle répétée 'm' fois, car on va lire et traiter 'm' paires de valeurs.
for i in range(m):
    # Lire une ligne d'entrée, la séparer en deux entiers 'a' et 'b'.
    a, b = map(int, input().split())
    # Incrémenter de 1 la valeur à la position 'a-1' de la liste 'ans'.
    # Ceci parce que les indices en Python commencent à 0 alors que les entrées utilisateurs commencent à 1.
    ans[a - 1] += 1
    # Incrémenter également de 1 la valeur à la position 'b-1' car chaque paire connecte deux sommets.
    ans[b - 1] += 1

# Boucler sur toutes les valeurs de 'j' allant de 0 à n-1 (pour parcourir tous les sommets ou éléments).
for j in range(n):
    # Afficher la valeur à la position 'j' de la liste 'ans', qui représente le nombre d'occurrences ou de connexions pour l'élément j+1.
    print(ans[j])