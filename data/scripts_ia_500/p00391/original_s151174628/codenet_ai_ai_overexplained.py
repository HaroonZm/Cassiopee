# La fonction input() lit une ligne de texte depuis l'entrée standard (par exemple, le clavier).
# Ici, on ne stocke pas ce que l'utilisateur saisit, on l'ignore directement.
input()

# La variable A va contenir une liste d'entiers.
# input() lit une ligne de texte.
# split() sépare cette chaîne de caractères en sous-chaînes séparées par des espaces.
# La compréhension de liste [int(x) for x in input().split()] transforme chaque sous-chaîne en entier.
A = [int(x) for x in input().split()]

# De manière similaire, on crée la liste B en lisant une autre ligne, en la divisant en mots, puis en convertissant chaque mot en entier.
B = [int(x) for x in input().split()]

# Initialisation de la variable ans à 0.
# Cette variable sera utilisée pour indiquer un résultat final (probablement un booléen au format entier).
ans = 0

# La méthode sort() trie la liste sur place, donc A est triée dans l'ordre décroissant grâce à reverse=True.
# Cela mettra les plus grands éléments de A en premier.
A.sort(reverse=True)

# Boucle pour chaque élément 'a' dans la liste A.
for a in A:
    # Pour chaque itération externe, on trie la liste B dans l'ordre décroissant.
    # Cela permet de s'assurer que les plus grands éléments de B sont au début.
    B.sort(reverse=True)

    # Une boucle qui s'exécute 'a' fois.
    for i in range(a):
        # On décrémente la valeur à l'index i dans la liste B de 1.
        # Autrement dit, on enlève 1 à chacun des 'a' premiers éléments de B.
        B[i] -= 1

    # On vérifie si la valeur minimale dans la liste B est inférieure à 0.
    # Si c'est le cas, cela signifie qu'au moins une valeur dans B est négative.
    if min(B) < 0:
        # On assigne 0 à ans.
        ans = 0
        # Et on interrompt la boucle principale, car la condition d'échec est atteinte.
        break

# Si la valeur maximale dans B est égale à 0,
# cela signifie que toutes les valeurs de B sont au plus égales à 0 et qu'aucune n'est positive.
if max(B) == 0:
    # On assigne 1 à ans pour indiquer un résultat positif/favorable.
    ans = 1

# Enfin, on affiche la valeur de ans.
print(ans)