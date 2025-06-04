import sys  # Importation du module système qui fournit l'accès à certaines variables ou fonctions utilisées par Python.
readline = sys.stdin.buffer.readline  # Création d'un alias pour la méthode de lecture d'une ligne depuis l'entrée standard (stdin) en mode binaire, ce qui la rend plus rapide pour la lecture de gros volumes de données, généralement utilisée pour les compétitions.

# Lecture des entiers n et k à partir de l'entrée standard.
n, k = map(int, readline().split())  # 'map' applique la fonction int à chaque élément du résultat de 'readline().split()', ce qui transforme chaque sous-chaîne (séparée par des espaces) en un int.

# Lecture d'une séquence d'entiers et stockage dans la liste 'vs'.
vs = list(map(int, readline().split()))  # Lecture d'une ligne, séparation par espace, conversion en entier, puis création d'une liste.

L = 18  # Définition de la constante L, qui sera utilisée comme le nombre maximal de niveaux pour le saut binaire (généralement pour garantir que 2^L > n pour tout n raisonnable).

# Création et initialisation de tableaux pour la structure de saut binaire.
# 'xid' et 'xsum' sont utilisés pour les sauts vers la droite (indices supérieurs), tandis que 'yid' et 'ysum' sont pour les sauts vers la gauche (indices inférieurs).
# Chaque tableau est initialisé avec des zéros et a une taille de n*L pour permettre l'accès à plusieurs niveaux pour chaque indice.
xid = [0] * (n * L)   # Table pour les indices de destination après chaque saut de niveau lv à partir de i vers la droite.
xsum = [0] * (n * L)  # Table pour la somme (ou compteur) associée aux sauts vers la droite.
yid = [0] * (n * L)   # Table pour les indices de destination après chaque saut de niveau lv à partir de i vers la gauche.
ysum = [0] * (n * L)  # Table pour la somme (ou compteur) associée aux sauts vers la gauche.

# Partie de pré-calcul pour les sauts vers la droite (x-table).
j = n  # Initialisation de j à la fin de la liste (juste après le dernier élément).
for i in reversed(range(n)):  # On commence de n-1 à 0 (ordre décroissant).
    # On cherche le plus petit j >= i tel que vs[j-1] > vs[i] + k.
    while i < j and vs[i] + k <= vs[j - 1]:
        j -= 1  # On décrémente j jusqu'à ce que la condition soit fausse.
    xid[i * L + 0] = j    # Premier niveau (direct) de saut: destination immédiate depuis i au niveau 0.
    xsum[i * L + 0] = j   # Pour le niveau 0 de i, on stocke aussi j comme 'somme' (interprétation dépend du problème).
    # Remplissage des niveaux supérieurs pour le saut binaire (doublons successifs).
    for lv in range(1, L):  # lv: niveau de profondeur pour le saut binaire.
        a = xid[i * L + lv - 1]  # a est la destination si on fait un saut de 2^{lv-1} à partir de i.
        if a == n:  # Si la destination sort du tableau, tous les niveaux suivants iront aussi en dehors.
            xid[i * L + lv] = n
        else:
            # Sinon, la nouvelle destination est atteinte en faisant deux fois le saut de taille 2^{lv-1}.
            xid[i * L + lv] = xid[a * L + lv - 1]
            # Addition des 'sums' pour accumuler le coût/compteur cumulé en deux sauts de niveau inférieur.
            xsum[i * L + lv] = xsum[i * L + lv - 1] + xsum[a * L + lv - 1]

# Partie de pré-calcul pour les sauts vers la gauche (y-table).
j = -1  # On initialise j avant le début de la liste.
for i in range(n):  # On parcourt de gauche à droite (de 0 à n-1).
    # On cherche le plus grand j < i tel que vs[j+1] + k <= vs[i].
    while j < i and vs[j + 1] + k <= vs[i]:
        j += 1  # On incrémente j jusqu'à ce que la condition soit fausse.
    yid[i * L + 0] = j    # Premier niveau (direct) de saut de i vers la gauche.
    ysum[i * L + 0] = j   # Comme pour xsum, on stocke aussi j (interprétation dépend du problème).
    # Remplissage des niveaux supérieurs pour le saut binaire (doublons successifs).
    for lv in range(1, L):  # Pour chaque niveau de profondeur.
        a = yid[i * L + lv - 1]  # Destination après un saut 2^{lv-1} à partir de i.
        if a == -1:  # Si la destination est hors du tableau (avant 0), tous les sauts suivants sont -1.
            yid[i * L + lv] = -1
        else:
            # Sinon, composition de saut binaire.
            yid[i * L + lv] = yid[a * L + lv - 1]
            ysum[i * L + lv] = ysum[i * L + lv - 1] + ysum[a * L + lv - 1]

# Traitement des requêtes.
q = int(readline())  # Lecture du nombre de requêtes à traiter.

for tmp in range(q):  # Boucle sur chaque requête.
    l, r = map(int, readline().split())  # Lecture des bornes l et r pour chaque requête.
    l -= 1  # Décrémentation pour passer en indexation de base 0 (Python indexe les listes à partir de 0, alors que les entrées sont souvent à partir de 1).
    r -= 1

    ans = 0  # Initialisation de la variable 'ans' qui va contenir le résultat final pour cette requête.

    # =========== Calcul depuis l'extrémité gauche (l vers r) ===========
    i = l  # On commence à l'indice l.
    ans -= i  # On retire i au début. Cela dépend du problème, mais ici c'est la logique décrite dans le code original.
    # On effectue des sauts binaires aussi grands que possible tant que la destination reste <= r.
    for lv in reversed(range(L)):  # On commence des grands sauts (niveau élevé) vers les petits sauts (niveau faible).
        if xid[i * L + lv] <= r:  # Si un saut du niveau lv ne dépasse pas la borne droite r.
            ans -= xsum[i * L + lv]  # On ajoute la somme/compteur ('coût') associé à ce saut.
            i = xid[i * L + lv]      # On déplace i à la nouvelle position (après le saut).

    # =========== Calcul depuis l'extrémité droite (r vers l) ===========
    i = r  # On recommence à l'indice r.
    ans += i + 1  # On ajoute i + 1 (là encore, dépend de la logique du problème original)
    # On effectue des sauts binaires vers la gauche aussi grands que possible tant qu'on ne passe pas avant l.
    for lv in reversed(range(L)):
        if yid[i * L + lv] >= l:  # On vérifie que le saut du niveau lv ne dépasse pas la borne gauche l.
            ans += ysum[i * L + lv] + (1 << lv)  # Ajoute la 'somme/cost' associée et 2^lv (nombre de pas couverts par ce saut).
            i = yid[i * L + lv]  # Mise à jour de la position courante de i.

    print(ans)  # Affichage du résultat pour cette requête.