# Création d'un dictionnaire vide appelé 'tp'
# Un dictionnaire est une structure de données qui stocke des paires clé-valeur
tp = {}

# Entrée dans une boucle infinie, qui ne s'arrêtera que lorsqu'une instruction break sera rencontrée
while 1:
    # Lecture d'une chaîne de caractères à partir de l'entrée standard (clavier) avec raw_input()
    # La fonction raw_input() lit toute la ligne de texte entrée jusqu'à l'appui sur la touche entrée (retour à la ligne)
    # La chaîne de caractères lue est ensuite divisée en deux parties en utilisant .split(",")
    # Cela signifie que la chaîne est coupée à chaque virgule rencontrée
    # Les deux éléments résultats sont convertis en entiers grâce à map(int, ...)
    t,p = map(int, raw_input().split(","))
    # On vérifie si t et p sont tous les deux égaux à 0
    # Cela sert de condition de sortie
    if t == p == 0:
        # Si t et p valent 0, on quitte la boucle grâce au break
        break
    # On ajoute une entrée dans le dictionnaire tp avec la clé t et la valeur p (tp[t] = p)
    # Cela associe l'équipe t au nombre de points p dans le dictionnaire
    tp[t] = p

# Création d'une liste des valeurs de points contenues dans tp
# [tp[key] for key in tp.keys()] crée une liste en prenant chaque clé (chaque équipe) de tp,
# puis récupère le nombre de points associé à cette équipe (valeur du dictionnaire)
# set(...) transforme cette liste en un ensemble, c'est-à-dire une collection non ordonnée et sans doublons,
# ce qui élimine les points en double
# list(...) retransforme l'ensemble en liste
# sorted(..., reverse=True) trie la liste des points du plus grand au plus petit (ordre décroissant)
plist = sorted(list(set([tp[key] for key in tp.keys()])), reverse=True)

# Entrée dans une nouvelle boucle infinie, pour traiter les requêtes de rang d'une équipe
while 1:
    try:
        # On essaie de lire une nouvelle ligne de l'utilisateur avec raw_input()
        # Cette ligne doit correspondre à un identifiant d'équipe (un int)
        team = int(raw_input())
    except:
        # Si une erreur se produit à la lecture ou à la conversion, cela signifie que l'entrée est terminée,
        # donc on quitte la boucle avec break
        break
    # On cherche la position de l'équipe dans la liste triée plist
    # tp[team] récupère le nombre de points pour l'équipe 'team' dans le dictionnaire tp
    # plist.index(tp[team]) donne l'indice du nombre de points de l'équipe dans la liste triee plist (cet indice commence à 0)
    # On ajoute 1 au résultat pour que les rangs commencent à 1 (et pas 0)
    print plist.index(tp[team])+1