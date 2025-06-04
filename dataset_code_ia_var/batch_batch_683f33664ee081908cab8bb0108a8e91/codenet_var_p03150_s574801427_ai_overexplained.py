import sys  # Importe le module sys pour permettre l'utilisation de sys.exit(), qui termine le programme immédiatement

S = input()  # Demande à l'utilisateur de saisir une chaîne de caractères et l'assigne à la variable S

num = len(S)  # Calcule la longueur de la chaîne S en utilisant la fonction len(), et l'assigne à la variable num

# Démarre une boucle for qui itère sur les valeurs de i allant de 0 jusqu'à num-1 inclus (range(num) génère une séquence de nombres de 0 à num-1)
for i in range(num):

    # À chaque itération, crée une nouvelle chaîne en prenant la sous-chaîne du début jusqu'à la position i (exclue), c'est-à-dire S[:i],
    # puis en la concaténant avec la sous-chaîne allant de l'index (num - 7 + i) jusqu'à la fin de la chaîne S (S[num-7+i:]).
    # Cette opération simule la suppression d'une partie centrale de la chaîne S, dont la longueur varie à chaque tour de la boucle.
    # Ensuite, compare le résultat de cette concaténation avec la chaîne de caractères littérale 'keyence' à l'aide de l'opérateur ==.
    if S[:i] + S[num-7+i:] == 'keyence':
        # Si la condition précédente est vraie, cela signifie qu'en supprimant la partie centrale ainsi définie de S,
        # il est possible d'obtenir 'keyence'. Dans ce cas, affiche la chaîne 'YES' à l'aide de la fonction print().
        print('YES')
        sys.exit()  # Termine immédiatement l'exécution du programme pour ne pas continuer inutilement la boucle ou exécuter la suite du code.

# Si la boucle termine sans qu'aucune des tentatives n'ait réussi à obtenir 'keyence',
# cela signifie que S ne peut pas être transformée en 'keyence' via cette opération. Affiche alors 'NO'.
print('NO')