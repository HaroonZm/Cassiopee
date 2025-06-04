# Demander à l'utilisateur de saisir un entier depuis l'entrée standard, puis convertir cette entrée en entier
n = int(input())

# Créer une liste 'ss' composée de chaînes de caractères saisies par l'utilisateur.
# Il y a (n + 1) chaînes, donc on fait une boucle 'for' pour collecter chacune d'elles.
ss = [input() for _ in range(n + 1)]

# Créer une nouvelle liste 'sp', qui va contenir une transformation de chaque chaîne de 'ss'.
# Pour chaque chaîne 's' dans 'ss', on crée une liste contenant uniquement le premier caractère de 's'.
# On encapsule chaque premier caractère dans une liste pour un traitement futur.
sp = [[s[0]] for s in ss]

# Boucler sur toutes les chaînes 's' de 'ss', en ayant également leur indice 'i' pour parcourir les listes en parallèle.
for i, s in enumerate(ss):
    # Parcourir chaque caractère de la chaîne 's', mais en partant du deuxième caractère (indice 1)
    for j in range(1, len(s)):
        # Vérifier si le caractère précédent (position j-1) et le caractère courant (position j)
        # sont de types différents (l'un est un chiffre, l'autre ne l'est pas)
        if s[j - 1].isdigit() != s[j].isdigit():
            # Si on passe d'un chiffre à une lettre ou inversement, ajouter une nouvelle chaîne vide à la liste sp[i]
            sp[i].append('')
        # Ajouter le caractère courant (à l'indice j dans 's') à la dernière section de sp[i] (donc concaténer)
        sp[i][-1] += s[j]

# La première chaîne transformée (après découpage) est stockée dans 's0'
s0 = sp[0]

# Parcourir toutes les chaînes transformées à partir de la deuxième (donc à partir de l'indice 1)
for s in sp[1:]:
    # Initialiser 'p', un compteur pour comparer caractère par caractère les chaînes s0 et s
    p = 0
    # 'm' est la longueur minimale entre s0 et s, pour ne pas dépasser la longueur des listes lors de la comparaison
    m = min(len(s0), len(s))
    # Tant que 'p' est à l'intérieur de la taille minimale et que les sections associées sont égales,
    # on incrémente 'p' pour continuer la comparaison
    while p < m and s0[p] == s[p]:
        p += 1
    # Si on a comparé tous les éléments (p == m), cela signifie que l'une des listes se termine ici ou les deux
    if p == m:
        # On affiche '+' si s0 est plus court ou égal à s, sinon '-'
        # L'indexation de la chaîne "-+" par l'expression booléenne ('len(s0) <= len(s)') choisit le bon caractère
        print('-+'[len(s0) <= len(s)])
        # On passe à la prochaine comparaison
        continue
    # Déterminer si les sections qui diffèrent sont toutes les deux composées de chiffres
    a = s0[p].isdigit()
    b = s[p].isdigit()
    if a and b:
        # Si les deux sont des chiffres,
        # on compare numériquement la valeur convertie en int de chaque section pour choisir '-' ou '+'
        print('-+'[int(s0[p]) <= int(s[p])])
    elif a or b:
        # Si l'une ou l'autre est composée de chiffres (mais pas les deux)
        # on affiche '+' si celle de s0 est un chiffre (a == True), sinon '-'
        print('-+'[a])
    else:
        # Si aucune des deux sections n'est un chiffre (donc deux chaînes de lettres)
        # alors on compare les chaînes en lexicographique pour choisir '-' ou '+'
        print('-+'[s0[p] <= s[p]])