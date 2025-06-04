# Demander à l'utilisateur d'entrer un nombre entier, lu sous forme de chaîne, puis converti en entier
n = int(input())  # Par exemple, si l'utilisateur tape '5', n sera égal à 5

# Prendre la seconde ligne d'entrée utilisateur, supposée être des entiers séparés par des espaces.
# input() lit la chaîne, split() la sépare selon les espaces,
# map(int, ...) convertit chaque morceau en entier.
# On utilise "*A, =" pour dépaqueter les valeurs dans la liste A.
*A, = map(int, input().split())

# On trie la liste 'A' dans l'ordre décroissant :
# reverse=1 signifie qu'on souhaite un tri décroissant
# (car 1 est interprété comme True en Python)
A.sort(reverse=1)

# Initialiser la variable 'ans' qui va contenir la plus grande valeur trouvée.
# On part de 0 pour être certain que n'importe quel résultat positif sera pris.
ans = 0

# Première boucle pour choisir l'indice 'i' dans la liste A, de 0 à n-1 inclus
for i in range(n):
    # Deuxième boucle pour choisir l'indice 'j' dans la liste A, allant de i+1 à n-1 inclus.
    # On s'assure que j > i, donc i et j pointent toujours sur deux indices distincts.
    for j in range(i+1, n):
        # Initialiser les variables 'p' et 'q' à 0
        # 'p' et 'q' vont servir à pointer vers deux indices distincts de i et j
        p = 0
        q = 0
        
        # Trouver la première valeur de p qui n'est ni i ni j.
        # Tant que p est égal à i ou à j, on l'incrémente de 1.
        # Cela garantit que p est distinct de i et de j.
        while p in [i, j]:
            p += 1

        # Trouver la première valeur de q qui n'est ni i, ni j, ni p.
        # Tant que q est égal à i ou à j ou à p, on l'incrémente de 1.
        # Cela garantit que q est distinct de i, j, p.
        while q in [i, j, p]:
            q += 1

        # Calculer la somme des éléments de A aux indices p et q : (A[p] + A[q])
        # Calculer la différence entre les éléments de A aux indices i et j : (A[i] - A[j])
        # Prendre la valeur du quotient de ces deux résultats.
        val = (A[p] + A[q]) / (A[i] - A[j])
        
        # Mettre à jour la variable ans avec la valeur maximale entre ans et val obtenue.
        ans = max(ans, val)

# Afficher le résultat final 'ans' en format flottant avec 6 chiffres après la virgule.
# Le format '%.6f' permet d'afficher exactement 6 chiffres après la virgule.
print("%.6f" % ans)