# Initialisation de la variable 'a' à zéro. 
# Cette variable servira à accumuler la somme des valeurs traitées.
a = 0

# Début d'une boucle 'for' qui va s'exécuter 5 fois. 
# La fonction range(5) génère une séquence de 5 entiers, de 0 à 4 inclus.
for i in range(5):

    # Lecture d'une entrée utilisateur via la fonction input().
    # input() retourne une chaîne de caractères (string) qui est convertie en entier avec int().
    b = int(input())

    # Condition 'if' pour vérifier si la valeur entrée 'b' est inférieure à 40.
    if b < 40:
        # Si 'b' est inférieure à 40, on affecte directement la valeur 40 à 'b'.
        # Cela garantit que la valeur minimale prise en compte est 40.
        b = 40

    # Ajout de la valeur (modifiée ou non) 'b' à la variable 'a'.
    # L'opérateur '+=' incrémente la valeur de 'a' par 'b' dans la même instruction.
    a += b

# Une fois la boucle terminée (après avoir traité 5 valeurs),
# on effectue une division entière de la somme 'a' par 5 pour calculer la moyenne arrondie vers le bas.
# L'opérateur '//' réalise une division entière, supprimant toute partie décimale.
print(a // 5)