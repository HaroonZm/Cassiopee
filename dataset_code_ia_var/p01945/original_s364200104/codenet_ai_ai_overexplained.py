# Demande à l'utilisateur de saisir une chaîne de caractères et stocke la valeur dans la variable 's'
s = input()

# Commence une boucle while qui continuera tant que la sous-chaîne '()' existe dans 's'
while '()' in s:
    # La méthode 'replace' recherche toutes les occurrences de la chaîne '()' dans 's'
    # Elle les remplace par une chaîne vide '', c'est-à-dire qu'elle les supprime
    # Cette nouvelle chaîne, purgée de toutes les occurrences de '()', est à nouveau affectée à 's'
    s = s.replace('()', '')

# Le bloc 'else' associé à la boucle while s'exécute seulement lorsque la boucle se termine "naturellement"
# c'est-à-dire que la condition '()' in s devient fausse (aucune parenthèse vide n'est trouvée)
else:
    # La méthode 'count' compte le nombre de fois que le caractère '(' apparaît dans la chaîne 's'
    # On affiche ce nombre avec la fonction print, ce qui affiche à l'utilisateur le nombre de parenthèses ouvrantes restantes
    print(s.count('('))