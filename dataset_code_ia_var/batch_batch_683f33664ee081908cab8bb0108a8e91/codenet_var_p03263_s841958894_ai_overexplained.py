def solve():
    # On commence par obtenir les dimensions du terrain, la hauteur (H) et la largeur (W)
    # input() prend la saisie utilisateur, split() sépare les éléments sur chaque espace, map(int, ...) convertit chaque élément en entier
    H, W = map(int, input().split())
    
    # On initialise le terrain (field), qui est une grille de H lignes et W colonnes 
    # Chaque ligne est saisie par l'utilisateur ; on convertit chaque nombre de la ligne en int par map(int, ...)
    # Pour chaque ligne de 0 à H-1 (total H lignes), on crée une sous-liste (donc une matrice)
    field = [list(map(int, input().split())) for _ in range(H)]

    # nh représente la position actuelle en ligne (indice de la ligne)
    # On démarre tout en haut à gauche, donc nh = 0
    nh = 0
    # nw représente la position actuelle en colonne (indice de la colonne)
    # On commence tout à gauche, donc nw = 0
    nw = 0
    # ans est la liste qui contiendra toutes les opérations menées, chaque opération sera une liste de positions [start_row, start_col, end_row, end_col]
    ans = []
    # haveCoin est une variable booléenne utilisée comme indicateur pour savoir si la case précédente avait un nombre impair
    haveCoin = False

    # On utilise une boucle éternelle (while True:) qui ne termine que manuellement par break 
    while True:

        # Si la valeur de la case actuelle est impaire (vérifié par le modulo 2, % 2 != 0)
        if field[nh][nw] % 2 != 0:
            # Si on avait déjà un "coin" du mouvement précédent, on l'enlève puisque deux impairs successifs s'annulent
            if haveCoin:
                haveCoin = False
            else:
                # Sinon, on doit transporter un "coin" à la case suivante
                haveCoin = True
        
        # frm représente la position de départ du mouvement (ou "from"), formatée en base 1 (lignes/colonnes commencent à 1), donc nh+1 et nw+1
        frm = [nh+1, nw+1]

        # Déplacement sur la grille en zigzag (ligne paire vers la droite, impaire vers la gauche)
        if nh % 2 == 0:
            # Si on est sur une ligne paire (comptée à partir de 0), on avance de colonne (nw += 1)
            nw += 1
            # Si on dépasse la dernière colonne (nw == W), on descend à la ligne suivante (nh += 1), 
            # et on place le pointeur à la dernière colonne à droite (nw = W-1)
            if nw == W:
                nh += 1
                nw = W-1
        else:
            # Si on est sur une ligne impaire, on recule de colonne (nw -= 1)
            nw -= 1
            # Si on va avant la première colonne (nw == -1), on descend à la ligne suivante (nh += 1)
            # et on remet le pointeur en début de ligne (nw = 0)
            if nw == -1:
                nh += 1
                nw = 0

        # to représente la position d'arrivée, toujours en base 1 (donc nh+1 et nw+1)
        to = [nh+1, nw+1]

        # Si nh atteint H, cela signifie qu'on a traité toutes les lignes, donc on termine la boucle
        if nh == H:
            break

        # Si haveCoin est True après le déplacement, cela signifie qu'on doit enregistrer l'action qui consiste à "transporter" à la case suivante
        # On enregistre alors le mouvement depuis frm vers to
        if haveCoin:
            ans.append(frm + to)
    
    # Après avoir fini tous les mouvements, on affiche le nombre total d'opérations effectuées (taille de ans)
    print(len(ans))
    # On affiche chaque opération sur une ligne, en déballant la liste pour séparer les éléments par des espaces
    for elem in ans:
        print(*elem)

# Ce bloc permet de s'assurer que la fonction solve() ne s'exécute que si le script est lancé directement,
# et pas lors d'un import dans un autre module Python
if __name__ == '__main__':
    solve()