# Solution complète pour le problème "Product Sale Lines"
# 
# Approche :
# - On modélise la file en forme de "コの字" (forme en U inversé) avec deux colonnes verticales (interne and externe) de hauteur H et une ligne horizontale (en haut) de largeur W.
# - Chaque personne est identifiée par sa position dans la file.
# - Initialement, les deux personnes (Uniclo Uzuki et Meguro Rin) sont placées côte à côte à l'arrière des deux colonnes verticales (donc dernière position dans chaque colonne).
# - On simule les départs selon la liste p (0 = extérieur sort, 1 = intérieur sort).
# - À chaque opération, ceux qui restent avancent d’une place.
# - Après chaque départ, on vérifie si les deux personnes sont "adjacentes" (sauf quand tous les deux sont aux coins noirs).
# 
# Détails importants :
# - Ne compte pas la position initiale même si adjacentes.
# - "Coin noir" correspond aux deux coins du "コの字" où ils ne sont pas considérés voisins.
# - Adjacent signifie positions voisines dans la structure du "コの字" (horizontalement ou verticalement adjacentes).
# 
# Implémentation :
# - On construit une représentation linéaire de la file en suivant la description.
# - On garde la position des deux amis dans cette structure.
# - On met à jour leurs positions à chaque départ.
# - On compte le nombre de fois où les deux friends sont adjacents selon la règle.
# 

def main():
    W, H = map(int, input().split())
    N = int(input())
    p = list(map(int, input().split()))

    # La "コの字" consiste en (du point de vue hauteur):
    # - Colonne extérieure (externe) dans la colonne de gauche, H personnes empilées verticalement.
    # - Colonne intérieure (interne) dans la colonne de droite, H personnes empilées verticalement.
    # - Ligne horizontale en haut, connectant ces 2 colonnes, de longueur W.
    #
    # Indexation des positions des personnes :
    # On numérote les positions selon le parcours suivant du "コの字" :
    #     (externe colonne) de bas en haut (0 à H-1)
    #     ensuite la ligne horizontale de gauche à droite (H à H+W-1)
    #     ensuite la colonne interne de haut en bas (H+W à H+W+H-1)
    #
    # La longueur totale est : H + W + H = 2H + W
    
    length = 2 * H + W
    
    # On représente la "ファイル" par une liste "line", chaque élément étant une personne ou None.
    # Initialement, chaque position est occupée par une personne identifiée par un numéro.
    # Les deux joueurs se trouvent à la queue des deux colonnes verticales (externes et internes).
    
    # Positions des deux amis :
    # - Uzuki (U) dans colonne extérieure (externe) à l'arrière => position 0 (le bas de la colonne externe)
    # - Rin (R) dans colonne intérieure (interne) à l'arrière => position H+W+H-1 (le bas de la colonne interne)
    
    # Pour suivre la position des joueurs, on stocke leur indices dans la file.
    # Tout le monde avance vers la tête (qui est à la position au sommet de la colonne extérieure)
    
    # Construction initiale liste des personnes:
    # On attribue un id unique à chaque personne dans l'ordre:
    # col_externe (bas vers haut): positions 0..H-1 => individus H-1 down to 0 (le dernier à la queue = 0)
    # ligne du haut: positions H..H+W-1 => individus 2H .. 2H+W-1
    # col_interne (haut vers bas): positions H+W..H+W+H-1 => individus 2H+W..2H+W+H-1
    #
    # Plus simple: initialisation par une liste d'indices de 0 à length-1
    # avec deux joueurs positionnés respectivelement :
    # - Uzuki = id "U" position 0 (col externe bas)
    # - Rin = id "R" position length-1 (col interne bas)
    
    line = ["P" + str(i) for i in range(length)]
    # Identifier les 2 joueurs par "U" et "R"
    uzuki_pos = 0
    rin_pos = length - 1
    line[uzuki_pos] = "U"
    line[rin_pos] = "R"
    
    # Fonction qui retourne les voisins directs (adjacents) d'une position dans le "コの字"
    def neighbors(pos):
        res = []
        # On traite les 3 parties distinctement
        
        if pos < H:
            # Colonne extérieure verticale (bas à haut)
            # voisins : position +1 (vers le haut) si pos +1 < H
            # et si pos == H-1, voisin à la ligne horizontale en position H
            if pos + 1 < H:
                res.append(pos + 1)
            else:  # pos == H-1 (plus haut dans colonne extérieure)
                res.append(H)  # début de la ligne horizontale
        elif H <= pos < H + W:
            # Ligne horizontale (gauche à droite)
            # voisins : pos -1 (si pos > H), pos +1 (si pos < H+W-1)
            # plus voisin colonne extérieure si pos == H (le début)
            # plus voisin colonne intérieure si pos == H+W-1 (la fin)
            if pos - 1 >= H:
                res.append(pos - 1)
            elif pos == H:
                res.append(H -1)  # sommet de colonne extérieure (pos == H-1)
            if pos + 1 < H + W:
                res.append(pos + 1)
            elif pos == H + W -1:
                res.append(H + W)  # sommet colonne interne (pos == H + W)
        else:
            # Colonne intérieure verticale (haut à bas)
            # voisins : pos +1 (vers le bas) si pos +1 < length
            # et si pos == H+W (le plus haut du côté interne), voisin pos == H + W -1 (fin ligne horizontale)
            if pos + 1 < length:
                res.append(pos + 1)
            else:  # pos == length-1 (bas du côté interne)
                res.append(H + W + H - 2)
            if pos == H + W:
                res.append(H + W - 1)
            if pos -1 >= H + W and pos -1 < length:
                res.append(pos -1)
            
            # En fait la colonne interne est haute->bas donc adjacents sont pos-1 (haut) et pos+1 (bas) si dans borne.
            # Corrige ci-dessus :
            # pos-1 si pos > H+W
            # pos+1 si pos < length-1
            res = []
            if pos -1 >= H + W:
                res.append(pos -1)
            if pos +1 < length:
                res.append(pos +1)
            if pos == H + W:
                # sommet interne a voisin à ligne horizontale fin
                res.append(H + W -1)
        
        return res

    # Ajustement des voisins pour colonne intérieure (car précédemment confus) :
    # Colonne intérieure (pos from H+W to H+W+H-1), rangée de haut en bas
    # voisins: pos-1 (haut) si pos > H+W
    #         pos+1 (bas) si pos < H+W+H-1
    #         si pos ==H+W (haut), voisin ligne horizontale pos H+W -1 (fin ligne horizontale)
    # Corrige voisins pour tous pos:
    def neighbors(pos):
        res = []
        if pos < H:
            # colonne extérieure
            if pos +1 < H:
                res.append(pos +1)
            else:
                # sommet colonne extérieure lien avec ligne horizontale pos H
                res.append(H)
            if pos -1 >= 0:
                res.append(pos -1)
        elif H <= pos < H+W:
            # ligne horizontale
            if pos -1 >= H:
                res.append(pos -1)
            elif pos == H:
                res.append(H -1)
            if pos +1 < H+W:
                res.append(pos +1)
            elif pos == H + W -1:
                res.append(H + W)
        else:
            # colonne intérieure
            if pos -1 >= H + W:
                res.append(pos -1)
            else:
                # sommet colonne intérieure lien avec ligne horizontale (fin)
                res.append(H + W -1)
            if pos +1 < length:
                res.append(pos +1)
        
        return res

    # On définit la fonction qui retourne True si les 2 amis sont adjacents selon les règles du problème
    def are_adjacent(u_pos, r_pos):
        # Ne pas compter quand les deux sont dans les coins noirs:
        # coins noirs = sommet (pos H-1 colonne extérieure) et sommet (pos H+W colonne intérieure)
        # si u_pos == H-1 and r_pos == H+W => ne compte pas
        if (u_pos == H -1 and r_pos == H + W) or (r_pos == H -1 and u_pos == H + W):
            return False
        # Sinon sont adjacents si positions voisins
        if r_pos in neighbors(u_pos):
            return True
        if u_pos in neighbors(r_pos):
            return True
        return False

    # Fonction qui fait avancer la file quand un départ a lieu:
    # p_i == 0 => la personne en colonne extérieure sort
    # p_i == 1 => la personne en colonne intérieure sort
    # La personne sort du head (position la plus haute) dans sa colonne respective, et ceux derrière avancent d'une position
    # Les deux amis ne sortent jamais (ne sont jamais en position de tête à sortir)

    # On simule avec une liste "line" et le fait de retirer la personne en tête dans la colonne correspondante,
    # et en décalant les autres

    def remove_front(line, col):
        # col == 0 => colonne extérieure
        # col == 1 => colonne intérieure
        # Trouver la personne à la tête dans la colonne
        # Positions de tête:
        # colonne extérieure : position H -1
        # colonne intérieure : position H + W
        if col == 0:
            head_pos = H -1
            # la position à retirer dans "line" est head_pos
            # on décale tous vers le bas dans cette colonne (de H-2 down to 0), chacun avance d'une position (pos+1)
            # la ligne horizontale et colonne intérieure ne changent pas
            # on enlève l'individu à head_pos : la personne à head_pos sort
            # On fait un décalage vers le haut de toute la colonne extérieure (pos 0..H-2 moves to pos 1..H-1)
            # head_pos est la tête, personne sort
            # Positions:
            # On remplace la position 0 par None (nouvelle place vide à la queue)
            # On shift en remontant

            # Vérification si Uzuki ou Rin sont au head, si oui ils ne sortent pas
            if line[head_pos] in ("U","R"):
                # ils ne sortent pas donc on ne retire personne
                return line, False
            
            # On retire line[head_pos], on décale de 1 vers le haut la colonne extérieure
            # Construction nouvelle colonne extérieure :
            col_ext = [line[i] for i in range(H)]
            # retirer head_pos = H-1
            removed = col_ext.pop()  # dernier élément
            # insérer None en position 0 (queue)
            col_ext.insert(0,None)
            # Met à jour line
            new_line = line[:]
            for i in range(H):
                new_line[i] = col_ext[i]
            return new_line, True

        else:
            # col == 1 colonne intérieure
            head_pos = H + W  # sommet colonne intérieure (la tête)
            # La colonne intérieure positions H+W .. H+W+H-1
            if line[head_pos] in ("U","R"):
                return line, False
            col_int = [line[i] for i in range(H + W, length)]
            removed = col_int.pop(0)  # retirer le premier élément (tête)
            col_int.append(None)      # nouvelle place vide à la queue
            new_line = line[:]
            for idx, val in enumerate(col_int):
                new_line[H + W + idx] = val
            return new_line, True


    count = 0
    counted_positions = set()
    # On ne compte pas la position initiale même si adjacents --> on ignore l'état avant la première sortie

    for i in range(N):
        col_to_remove = p[i]
        line, changed = remove_front(line, col_to_remove)

        # Mettre à jour position des 2 joueurs (U et R)
        # On cherche leurs positions dans line:
        new_uzuki_pos = None
        new_rin_pos = None
        for idx, val in enumerate(line):
            if val == "U":
                new_uzuki_pos = idx
            elif val == "R":
                new_rin_pos = idx

        if new_uzuki_pos is None or new_rin_pos is None:
            # Ce cas ne devrait pas arriver, car joueurs ne sortent pas
            break

        # Vérifier si adjacents selon la règle:
        # On compte une fois par événement où ils deviennent adjacents, donc on vérifie transitions.

        # Ne compte pas la situation initiale (avant premier départ)
        # On ne compte que si ils sont adjacents et que cette situation est une nouvelle rencontre (pas déjà comptée)
        if are_adjacent(new_uzuki_pos, new_rin_pos):
            # Ne pas compter les coins noirs déjà exclu dans are_adjacent
            # Pour ne pas compter plusieurs fois la même position
            # On utilise l'ensemble counted_positions pour stocker les tuples (pos_u, pos_r) atteints à comptabiliser
            key = (new_uzuki_pos, new_rin_pos)
            # On tient à ne compter que les nouvelles positions adjacentes apparues
            if key not in counted_positions and i > 0:
                count += 1
                counted_positions.add(key)
        else:
            # Si ils ne sont pas adjacents, on ne compte rien et on peut nettoyer l'ensemble des positions adjacentes connues
            # pour pouvoir recompter quand ils redeviendront adjacents
            counted_positions.clear()

        # Mettre à jour positions pour la suite
        uzuki_pos = new_uzuki_pos
        rin_pos = new_rin_pos

    print(count)

if __name__ == "__main__":
    main()