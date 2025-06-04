# Commence par lire un entier de l'entrée standard qui représente le nombre de requêtes à traiter.
q = int(input())  # 'q' est le nombre de requêtes ou d'opérations qui vont suivre

# Initialise une liste vide qui sera utilisée pour stocker toutes les opérations brutes lues depuis l'entrée.
s = []

# Initialise une autre liste qui sera utilisée pour collecter toutes les clés et intervalles mentionnés.
# Cette liste sert à préparer la discrétisation (mapping d'éléments arbitraires à des indices consécutifs).
rs = []  # Pour la discrétisation des clés

# Parcours de toutes les requêtes, une par une, en fonction du nombre spécifié (q)
for i in range(q):
    # Lecture d'une ligne de saisie, puis séparation en liste de chaînes (chaque élément de la requête)
    s.append(input().split())
    # Si le type d'opération est '3' (opération impliquant un intervalle de clés)
    if s[i][0] == '3':
        # On ajoute à 'rs' la clé de début (s[i][1]) et la clé de fin (s[i][2]) de l'intervalle
        rs.append(s[i][1])
        rs.append(s[i][2])
    else:
        # Pour toute autre opération, on ajoute simplement la clé unique utilisée (s[i][1]) à 'rs'
        rs.append(s[i][1])

# On retire les doublons avec 'set', on transforme à nouveau en liste,
# puis on trie toutes les clés et intervalles pour obtenir un ordre cohérent et fixer les indices.
rs = sorted(list(set(rs)))

# Crée un dictionnaire de discrétisation permettant d'accéder rapidement à l'indice de chaque clé
# Chaque clé distincte de rs se voit attribuer un entier unique, consécutif, de 0 à len(rs)-1
index = {rs[i]: i for i in range(len(rs))}

# Initialise une liste de listes vides pour stocker les données associées à chaque clé discrétisée.
# Il y a autant de sous-listes que de clés distinctes (c-à-d, len(rs))
d = [[] for i in range(len(rs))]

# Parcours à nouveau la liste des requêtes enregistrées afin de traiter chaque opération selon son type
for i in range(q):
    # Extrait l'opération (type de requête, en entier) et la clé (sous forme de chaîne)
    op, key = int(s[i][0]), s[i][1]
    # Récupère l'indice discrétisé correspondant à cette clé à l'aide du dictionnaire 'index'
    idx = index[key]
    # Si l'opération est de type 0 (insertion d'une valeur pour cette clé)
    if op == 0:
        # Ajoute la valeur (s[i][2]) à la liste associée à cette clé discrétisée
        d[idx].append(s[i][2])
    # Si l'opération est de type 1 (affichage de toutes les valeurs associées à cette clé)
    elif op == 1:
        # Parcourt chaque élément stocké pour cette clé et l'affiche
        for item in d[idx]:
            print(item)
    # Si l'opération est de type 2 (effacement de toutes les valeurs associées à cette clé)
    elif op == 2:
        # Vide la liste de données associée à cette clé
        d[idx].clear()
    # Si l'opération est de type 3 (affichage pour un intervalle de clés)
    else:
        # Détermine les indices délimiteurs de l'intervalle dans l'ordre trié
        l = idx  # indice de début (pour la clé de gauche)
        r = index[s[i][2]]  # indice de fin (pour la clé de droite, incluse)
        # Pour chaque clé comprise dans cet intervalle (bornes incluses)
        for j in range(l, r + 1):
            # Parcourt toutes les valeurs associées à cette clé et les affiche
            for item in d[j]:
                # Affiche à la fois la clé représentée (chaîne) et la valeur associée
                print(rs[j], item)