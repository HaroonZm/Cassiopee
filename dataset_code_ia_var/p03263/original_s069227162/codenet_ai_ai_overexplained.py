# Lire deux entiers à partir d'une seule ligne d'entrée, séparés par un espace
# map applique la fonction int à chaque élément de l'entrée découpée en morceaux (split())
# H représente la hauteur (nombre de lignes), W la largeur (nombre de colonnes) de la grille
H, W = map(int, input().split())

# Initialiser une liste vide appelée 'a' pour stocker la grille/les matrices de nombres
a = []

# Répéter H fois (pour chaque ligne de la grille)
for _ in range(H):
    # Lire la ligne courante, découper selon les espaces et convertir chaque élément en entier
    A = list(map(int, input().split()))
    # Ajouter la liste convertie de cette ligne à la grille 'a'
    a.append(A)

# Initialiser la variable i à 0 (non utilisée plus loin, c'était probablement pour une ancienne version du code)
i = 0
# Initialiser la variable j à 0 (également non utilisée)
j = 0
# Initialiser un compteur 'cnt' à 0 ; il comptera le nombre total de mouvements effectués
cnt = 0
# Initialiser une liste vide 'ans' pour enregistrer chaque mouvement effectué sous forme de liste [h1, w1, h2, w2]
ans = []

# Boucle externe sur chaque ligne de la grille; h commence à 0 et va jusqu'à H-1
for h in range(H):
    # Boucle interne sur chaque colonne de la ligne courante; w commence à 0 et va jusqu'à W-1
    for w in range(W):
        # Vérifier si le nombre courant, a[h][w], est impair (le reste de la division par 2 est non nul)
        if a[h][w] % 2 == 1:
            # Vérifier si ce n'est PAS la dernière colonne de la ligne (w n'est pas égal à l'indice maximal W-1)
            if w != W-1:
                # Incrémenter le compteur de mouvements car on va effectuer une opération
                cnt += 1
                # Enregistrer ce mouvement : on déplace 1 de la case (h, w) à la case (h, w+1)
                # Utilisation de h+1 et w+1 car l'énoncé (ou la sortie) exige des indices commençant à 1
                ans.append([h+1, w+1, h+1, w+2])
                # Décrémenter de 1 la case courante car on donne un à la voisine
                a[h][w] -= 1
                # Incrémenter de 1 la case juste à droite (h, w+1)
                a[h][w+1] += 1
            else:
                # Si on est sur la dernière colonne (droite), mais PAS sur la dernière ligne
                if h != H-1:
                    # Incrémenter le compteur de mouvements car on va déplacer vers la ligne du dessous
                    cnt += 1
                    # Enregistrer ce mouvement : on déplace 1 de la case (h, w) à la case (h+1, w)
                    ans.append([h+1, w+1, h+2, w+1])
                    # Décrémenter la case courante car on donne un à celle du dessous
                    a[h][w] -= 1
                    # Incrémenter la case directement en dessous (h+1, w)
                    a[h+1][w] += 1

# Afficher sur une ligne le nombre total de mouvements effectués
print(cnt)

# Parcourir tous les mouvements enregistrés dans la liste ans
for i in range(len(ans)):
    # Imprimer chaque mouvement sous forme de 4 nombres séparés par des espaces
    # *ans[i] permet de "dépaqueter" la liste ans[i] en paramètres séparés pour print
    print(*ans[i])