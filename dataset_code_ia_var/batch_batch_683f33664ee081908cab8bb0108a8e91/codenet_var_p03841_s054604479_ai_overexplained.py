# Demander à l'utilisateur d'entrer un entier n via l'entrée standard
n = int(input())  # n représente la taille ou le nombre d'éléments à traiter

# Demander à l'utilisateur une ligne contenant n entiers séparés par des espaces
# input().split() produit une liste de chaînes correspondant aux entiers saisis
# enumerate() parcourt cette liste et retourne à chaque fois un couple (indice, valeur)
# Ici, la variable i contient l'indice (que l'on ignore), x la valeur (une chaîne)
# [int(x) for i, x in enumerate(...)] convertit chaque valeur de chaîne en entier
x = [int(x) for i, x in enumerate(input().split())]

# range(1, n+1) génère une séquence d'entiers du 1 à n inclus
# zip(x, range(1, n+1)) associe chaque élément de x à son indice (commençant à 1)
# sorted(...) trie la liste résultante selon les valeurs de x par ordre croissant (par défaut)
x = sorted(zip(x, range(1, n+1)))

# Initialiser une liste vide appelée stack
stack = []

# Boucle sur les couples (valeur, indice) de la liste x à l'envers
# x[::-1] renverse l'ordre de x pour traiter les plus grandes valeurs en premier
for v, i in x[::-1]:
    # Répéter l'opération (i-1) fois. Pour chaque répétition :
    for _ in range(i-1):
        # Ajouter i à la fin de la liste stack
        stack.append(i)

# Initialiser cur à 1 ; il représente la valeur courante cible pour le traitement
cur = 1

# Initialiser la liste ans qui contiendra la solution (la séquence finale construite)
ans = []

# Initialiser la liste temporaire res qui servira pour des valeurs mises en réserve
res = []

# Initialiser le compteur cnt, une liste de n+1 zéros
# cnt[k] va compter combien de fois l'entier k a été ajouté à ans (ou à une certaine étape)
cnt = [0]*(n+1)

# Parcourir i de 0 à n-1 (chaque position dans x)
for i in range(n):
    # Pour chaque différence entre la valeur x[i][0] (la i-ème valeur de x, premier champ du tuple)
    # et la valeur courante cur, répéter autant de fois :
    for _ in range(x[i][0]-cur):
        # Si stack n'est pas vide
        if stack:
            # stack.pop() enlève et récupère le dernier élément de stack
            nxt = stack.pop()
        # Sinon, si res n'est pas vide
        elif res:
            # res.pop() enlève et récupère le dernier élément de res
            nxt = res.pop()
        # Sinon, il n'y a plus de valeurs possibles à utiliser
        else:
            # Affiche 'No' (impossible de construire une séquence valide)
            print('No')
            # Arrête immédiatement l'exécution du script
            exit()
        # Ajouter nxt à ans (la solution en construction)
        ans.append(nxt)
        # Incrémenter le compteur correspondant à nxt
        cnt[nxt] += 1
    # Après avoir ajouté les valeurs intermédiaires,
    # On vérifie que le nombre d'occurrences du i-ème indice est correct
    if cnt[x[i][1]] != x[i][1]-1:
        # Si ce n'est pas le cas, la solution n'est pas valide, afficher 'No'
        print('No')
        # Arrêter le programme
        exit()
    # Ajouter l'indice (x[i][1]) à la solution
    ans.append(x[i][1])
    # Pour n-x[i][1] fois, ajouter x[i][1] à la liste res (mise en réserve)
    for _ in range(n-x[i][1]):
        res.append(x[i][1])
    # Mettre à jour cur à la valeur suivante à traiter : x[i][0]+1
    cur = x[i][0]+1

# Après avoir traité tous les éléments, ajouter toutes les valeurs en réserve à ans
ans += res

# Afficher 'Yes' pour indiquer qu'une solution a été trouvée
print('Yes')
# Afficher les éléments de la liste ans séparés par un espace
print(*ans)