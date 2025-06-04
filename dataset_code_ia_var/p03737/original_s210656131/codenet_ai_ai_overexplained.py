# Demande à l'utilisateur d'entrer une ligne de texte au clavier
# La fonction 'input()' affiche une invite à l'utilisateur (il n'y a pas d'argument, donc rien n'est affiché)
# L'utilisateur tape une chaîne de caractères et appuie sur Entrée
# La méthode 'split()' sépare la chaîne obtenue en une liste de sous-chaînes, en utilisant les espaces comme séparateur par défaut
# Par exemple, si l'utilisateur tape 'bonjour le monde', S sera ['bonjour', 'le', 'monde']
S = input().split()

# On crée une liste vide appelée 'ans'
# Cette liste servira à stocker les premières lettres, mises en majuscule, de chaque mot de la liste S
ans = []

# On parcourt chaque élément 's' de la liste S
for s in S:
    # Pour chaque élément 's', on prend son premier caractère en utilisant 's[0]'
    # 's[0]' signifie "prends le caractère à l'indice 0", c'est-à-dire le premier caractère de la chaîne 's'
    # La méthode 'upper()' convertit ce caractère en majuscule, s'il ne l'est pas déjà
    # On ajoute ce caractère majuscule à la liste 'ans' grâce à la méthode 'append'
    ans.append(s[0].upper())

# La fonction 'join' permet de rassembler une liste de chaînes de caractères en une seule chaîne
# Ici, ''.join(ans) va créer une nouvelle chaîne en concaténant tous les éléments de la liste 'ans', sans séparateur entre eux (car la chaîne de départ est vide : '')
# La fonction 'print' affiche cette chaîne sur la sortie standard (en général à l'écran)
print(''.join(ans))