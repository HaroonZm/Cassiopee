# Demande à l'utilisateur d'entrer deux entiers séparés par un espace.
# input() lit la ligne saisie par l'utilisateur sous forme de chaîne de caractères.
# split() sépare la chaîne sur les espaces pour donner une liste de deux éléments.
# map(int, ...) convertit ces deux éléments en entiers.
# On assigne le premier entier à la variable n, et le second à la variable k.
n, k = map(int, input().split())

# Initialise la variable 'count' à 0.
# Cette variable servira à accumuler le résultat final qui sera affiché à la fin.
count = 0

# On utilise une boucle for pour faire varier la variable b de 'k+1' jusqu'à 'n+1' (exclu),
# car la fonction range(a, b) produit a, a+1, ..., b-1.
for b in range(k + 1, n + 1):

    # Calcule le nombre d'entiers dans la plage de 1 à n qui,
    # lorsqu'on divise leur valeur entière par 'b' (division entière),
    # sont complètement dans des blocs de taille 'b'.
    # 'n // b' donne le nombre de blocs complets de taille b dans n.
    # '(b - k)' donne le décalage spécifique qui intéresse l'algorithme pour chaque bloc.
    candidate = (n // b) * (b - k)

    # 'n % b' donne le reste de la division de n par b.
    # C'est-à-dire, combien il reste après avoir extrait le maximum de blocs de taille b.
    mod = n % b

    # On vérifie si ce reste est supérieur ou égal à k.
    if mod >= k:
        # On calcule combien il y a d'entiers supplémentaires
        # dans le dernier groupe partiel qui répondent à la condition,
        # ceux dont l'indice dépasse k dans le groupe mod.
        add = mod - k + 1

        # Si k vaut 0, il faut soustraire 1 car l’indice 0 serait compté deux fois.
        if k == 0:
            add -= 1

        # On ajoute ce nombre aux candidats pour ce b.
        candidate += add

    # Mise à jour du compteur global avec les candidats calculés pour ce b.
    count += candidate

# Affiche le résultat final, le nombre total calculé.
print(count)