from collections import defaultdict  # Importe la classe defaultdict du module collections. defaultdict fonctionne comme un dictionnaire, mais fournit une valeur par défaut pour les clés inexistantes.

N = int(input())  # Lit une ligne de l'entrée standard (utilisateur), convertit la chaîne saisie en entier, puis attribue ce nombre à la variable N. N représentera très souvent une taille ou un nombre d'éléments à traiter.
S = input()  # Lit encore une ligne au clavier, la conserve telle quelle (sous forme de chaîne de caractères), et stocke cette chaîne dans la variable S.

S1 = S[:N]  # Prend une sous-chaîne de S, allant du début (indice 0 inclus) jusqu'à l'indice N (exclu). Cela donne les N premiers caractères de S. On la stocke dans S1.
S2 = S[N:][::-1]  # Prend la sous-chaîne commencant à l'indice N jusqu'à la fin de S (cela représente la "seconde moitié" de S si S fait 2N caractères). Ensuite, [::-1] inverse cette sous-chaîne, donc S2 est la seconde moitié de S renversée.

D = defaultdict(int)  # Crée un nouveau dictionnaire dont les valeurs par défaut sont 0 (c'est le comportement de int()). On utilise D pour compter des occurrences avec des clés particulières qui vont être des tuples de chaînes, sans avoir à vérifier si la clé existe avant d'incrémenter.

ans = 0  # Initialise une variable nommée ans avec la valeur 0. Cette variable servira à accumuler, probablement le résultat final ou un comptage.

# Première boucle : On considère toutes les combinaisons possibles des caractères de S1, 0 ou 1 pour chaque position.
for i in range(2**N):  # Va boucler pour i allant de 0 à (2 puissance N) - 1 inclus, ce qui fait toutes les combinaisons binaires possibles sur N bits.
    # Convertit l'entier i en une chaîne binaire de N chiffres, en truquant : on ajoute 2**N (soit un "1" devant N zéros en binaire, ce qui permet de garantir que tous les bits soient présents même avec des zéros initiaux en binaire), puis on découpe la chaîne en sautant les trois premiers caractères ('0b1') pour n'avoir que N caractères.
    bit = bin(2**N+i)[3:]
    # Ici, on crée la chaîne red1 en parcourant simultanément S1 et bit lettre à lettre avec zip().
    # Pour chaque paire (d, s) où d vient de S1 et s du bit-string (chaîne de '0' et '1'), on sélectionne d si s vaut '1'.
    red1 = "".join([d for d, s in zip(S1, bit) if s == "1"])
    # De même, on crée blue1 en prenant d (caractère de S1) chaque fois que s (le caractère dans bit) est égal à '0'.
    blue1 = "".join([d for d, s in zip(S1, bit) if s == "0"])
    # On utilise le tuple (red1, blue1) comme clé dans le dictionnaire D. On ajoute 1 à la valeur associée à cette clé.
    # Si (red1, blue1) n'était pas encore présent dans D, il est créé automatiquement avec une valeur de 0 grâce à defaultdict.
    D[(red1, blue1)] += 1

# Deuxième boucle : cette fois, on itère à nouveau sur toutes les possibilités de combinaisons binaires sur N bits, mais en utilisant S2.
for i in range(2 ** N):  # Boucle de 0 à 2^N - 1 inclus.
    # Comme ci-dessus, prépare le bitstring correspondant (chaîne binaire de N caractères pour la combinaison courante).
    bit = bin(2 ** N + i)[3:]
    # On construit red2 en prenant les caractères de S2 pour lesquels le bit correspondant vaut '1'
    red2 = "".join([d for d, s in zip(S2, bit) if s == "1"])
    # blue2 prend les caractères de S2 pour lesquels le bit est '0'
    blue2 = "".join([d for d, s in zip(S2, bit) if s == "0"])
    # Pour chaque combinaison dans S2, on regarde si la paire (blue2, red2) existe dans le dictionnaire D et on additionne la valeur associée à ans.
    # Cela signifie qu'on recherche dans D le nombre d'occurrences où le red de la deuxième moitié correspond exactement au blue de la première, et inversement.
    ans += D[(blue2, red2)]

print(ans)  # Affiche (écrit sur la sortie standard) la valeur entière contenue dans ans, qui est la réponse finale calculée.