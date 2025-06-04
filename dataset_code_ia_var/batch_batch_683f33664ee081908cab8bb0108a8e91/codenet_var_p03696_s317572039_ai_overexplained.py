from functools import reduce  # Importe la fonction 'reduce' du module 'functools'

# Demande à l'utilisateur d'entrer une valeur entière via le clavier
N = int(input())  # Stocke la valeur entière entrée par l'utilisateur dans la variable N

# Demande à l'utilisateur d'entrer une chaîne de caractères
S = input()  # Stocke la chaîne entrée par l'utilisateur dans la variable S

# L'objectif est de créer une expression correcte de parenthèses à partir de S
# Pour cela, si S contient trop de parenthèses ouvrantes '(', il faut ajouter des ')' à la fin
# Si S contient trop de parenthèses fermantes ')', il faut ajouter des '(' au début
# Le code doit déterminer combien de chaque type sont nécessaires

# Utilisation de reduce pour parcourir tous les caractères de S
# La variable 'acc' est un tuple de deux entiers :
#   acc[0] : le nombre de parenthèses ouvrantes '(' non fermées rencontrées jusqu'à présent
#   acc[1] : le nombre minimal de parenthèses fermantes ')' excédentaires trouvées au début (donc le nombre de '(' à ajouter au début)
a, b = reduce(
    # Cette lambda prend l'accumulateur 'acc' et le caractère courant 's'
    lambda acc, s: (
        # Première valeur du tuple :
        # Si le caractère courant est '(', on incrémente le compteur de '(' non fermées
        # Si le caractère courant est ')', on décrémente (car une parenthèse est fermée)
        # On utilise max(..., 0) pour éviter que ce compteur ne devienne négatif
        acc[0] + 1 if s == '(' else max(0, acc[0] - 1),

        # Deuxième valeur du tuple :
        # Si on rencontre une ')' alors qu'il n'y a aucune '(' ouverte (acc[0] == 0),
        # on doit compter cette parenthèse excédentaire, donc on incrémente acc[1]
        # Sinon, on laisse acc[1] inchangé
        acc[1] + 1 if s == ')' and acc[0] == 0 else acc[1]
    ),
    S,        # On applique la fonction à chaque caractère de S
    (0, 0)    # L'accumulateur commence à (0, 0): aucune '(' non fermée, et aucune ')' en trop
)

# À la fin du reduce :
# a = nombre de '(' restées non fermées dans S (donc nombre de ')' à ajouter à la fin)
# b = nombre de ')' excédentaires rencontrées en début de chaîne (donc nombre de '(' à ajouter au début)

# Construction de la chaîne résultat :
# - Ajoute 'b' fois le caractère '(' au début
# - Puis la chaîne S elle-même
# - Puis 'a' fois le caractère ')' à la fin
ans = b * '(' + S + a * ')'

# Affiche la chaîne résultante qui est maintenant une expression bien parenthésée
print(ans)  # Affiche le résultat final à l'écran