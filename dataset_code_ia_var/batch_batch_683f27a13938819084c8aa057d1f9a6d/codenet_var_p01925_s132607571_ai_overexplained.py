#!/usr/bin/env python3
# AOJ C - Programme principal avec commentaires extrêmement détaillés

# Cette boucle while tourne indéfiniment jusqu'à ce qu'on rencontre une condition d'arrêt explicite (break).
while 1:  # 1 représente la valeur True en Python, cette boucle ne s'arrêtera pas tant que le 'break' n'est pas exécuté.
    # On lit une ligne de l'entrée standard (typiquement le clavier) et on la sépare en deux valeurs
    # grâce à la méthode .split(), générant une liste de chaînes.
    # On utilise map(int, ...) pour convertir chaque chaîne en entier.
    N, M = map(int, input().split())  # N = nombre de joueurs, M = nombre d'événements (par exemple)

    # Condition d'arrêt de la boucle : si N==0 et M==0, le programme quitte la boucle grâce à 'break'.
    if N == 0 and M == 0:
        break  # Sortie de la boucle while, donc fin du programme

    # Création d'une liste I, contenant M sous-listes. Chaque sous-liste est générée par
    # la capture d'une ligne d'entrée, divisée avec .split(), convertie en entiers.
    # On utilise la compréhension de liste pour effectuer cette opération M fois (pour chaque événement).
    I = [list(map(int, input().split())) for _ in range(M)]  # I contiendra tous les événements

    # Création d'une liste P de taille N, initialisée avec des zéros.
    # P[i] représentera le score total du joueur numéro i.
    P = [0 for _ in range(N)]

    # Création d'une liste mP de taille N, également initialisée à 0.
    # mP[i] utilisera une logique particulière dans le code suivant.
    mP = [0 for _ in range(N)]

    # Parcours de chacun des M événements (on numérote les événements de 0 à M-1)
    for i in range(M):
        # k représente le nombre d'éléments concernés par cet événement (à partir de la deuxième valeur de la ligne)
        k = I[i][1]

        # Si k == 1, l'événement ne concerne qu'un seul joueur
        if k == 1:
            # On incrémente la valeur mP de ce joueur (l'indice du joueur est donné par I[i][2]-1)
            mP[I[i][2]-1] += I[i][0]  # I[i][0] est la valeur associée à l'événement (peut être un score ou une quantité)

        # Boucle à travers tous les joueurs concernés par cet événement
        for j in range(k):
            # On met à jour la liste P pour chacun des k joueurs impliqués (P[joueur] += valeur)
            # L'indice du joueur est I[i][2+j]-1 car la liste I[i] est structurée comme [valeur, k, joueur1, joueur2, ...]
            P[I[i][2+j]-1] += I[i][0]

    # Initialisation de la variable maxp qui contiendra la valeur maximale de score trouvée dans P
    maxp = 0  # Commence à 0 car les scores peuvent être positifs seulement

    # Initialisation de minp à l'infini, ainsi tout score rencontré sera plus petit
    minp = float("inf")  # float("inf") représente l'infini positif

    # On souhaite trouver l'indice du joueur qui a le score maximum (on le stocke dans 'index')
    for i in range(N):
        if maxp < P[i]:
            maxp = P[i]  # On met à jour maxp avec le nouveau score maximum
            index = i    # On retient l'indice correspondant à ce score maximum

    # Ensuite, on cherche, parmi les autres joueurs (sauf celui d'indice 'index'),
    # la valeur minimale de mP.
    for i in range(N):
        if i != index:  # On ignore le joueur d'indice 'index'
            if minp > mP[i]:
                minp = mP[i]  # On met à jour la valeur minimale rencontrée

    # Variable de flag 'f', initialisée à 0 (ceci représente False dans ce cas)
    f = 0

    # On vérifie si, parmi les autres joueurs (sauf 'index'), il existe un joueur pour lequel mP vaut 0
    for i in range(N):
        if i != index:
            if mP[i] == 0:
                f = 1  # Si tel joueur existe, on met le flag à 1 (représente True)

    # Si le flag f a été mis à 1, cela signifie qu'au moins un joueur (autre que le score max) n'a jamais eu un ajout mP.
    if f:
        # On affiche la valeur maximale des scores de P + 1.
        print(max(P)+1)  # max(P) retourne le score maximum trouvé dans P
    else:
        # Sinon, on affiche max(P) + 1 - minp, c'est-à-dire le score max augmenté de 1,
        # auquel on soustrait la valeur minimale trouvée dans mP parmi les autres joueurs.
        print(max(P)+1-minp)