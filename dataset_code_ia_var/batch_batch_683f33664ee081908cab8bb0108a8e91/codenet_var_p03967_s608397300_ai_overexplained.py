# Demander à l'utilisateur de saisir une chaîne de caractères.
# Cette chaîne sera stockée dans la variable S.
S = input()

# Calculer la longueur de la chaîne S, c'est-à-dire le nombre de caractères, et stocker cette valeur dans la variable N.
N = len(S)

# Initialiser la variable num à 0.
# Cette variable sera utilisée comme un compteur pour suivre le nombre courant d'états particuliers selon l'algorithme.
num = 0

# Initialiser la variable ans à 0.
# Cette variable sera utilisée pour calculer et stocker la réponse finale, c'est-à-dire le score calculé selon une logique spécifique.
ans = 0

# Démarrer une boucle qui va parcourir tous les entiers de 0 jusqu'à N-1, c'est-à-dire pour chaque caractère de la chaîne S.
for i in range(N):

    # Vérifier si le caractère à la position i est égal à la lettre 'g'.
    if S[i] == 'g':

        # Si oui, alors vérifier si la valeur de num est strictement supérieure à 0.
        if num > 0:
            # Si num > 0, diminuer num de 1 (équivalent à num = num - 1).
            num -= 1
            # Ensuite, augmenter ans de 1 (équivalent à ans = ans + 1).
            ans += 1
        else:
            # Sinon, c'est-à-dire si num est égal à 0, alors augmenter num de 1.
            num += 1

    # Si le caractère à la position i n'est pas 'g' (donc autre chose, sûrement 'p' dans ce problème),
    else:
        # Vérifier si num est strictement supérieur à 0.
        if num > 0:
            # Si num > 0, diminuer num de 1.
            num -= 1
        else:
            # Sinon, augmenter num de 1.
            num += 1
            # Ensuite, diminuer ans de 1 (équivalent à ans = ans - 1).
            ans -= 1

# Afficher la valeur de ans à l'utilisateur.
# Cela représente la réponse finale calculée selon la logique de l'algorithme.
print(ans)