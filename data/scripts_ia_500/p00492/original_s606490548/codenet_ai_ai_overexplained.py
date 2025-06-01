import sys

# Définit la fonction principale de résolution qui prend en entrée la grille 'data' et ses dimensions 'w' (largeur) et 'h' (hauteur).
def solve(data, w, h):
    # Crée un ensemble pour stocker les coordonnées des zones invisibles (celles isolées entourées par des obstacles).
    invisible_area = set()
    # Crée un ensemble pour stocker les coordonnées des zones visibles (zones ouvertes connectées à l'extérieur).
    visible_area = set()
    # Crée un ensemble pour marquer les coordonnées déjà visitées afin d'éviter les traitements multiples.
    visited = set()
    
    # Double boucle sur tous les points de la grille :
    # 'y' est l'index des lignes (coordonnée verticale),
    # 'x' est l'index des colonnes (coordonnée horizontale).
    for y in range(h):
        for x in range(w):
            # On marque initialement chaque point comme visité afin de préparer la détection des régions.
            # (Ce point sera actualisé plus bas pour l'exploration des régions.)
            visited.add((x, y))
            # Si la case courante est un obstacle (valeur 1), on l'ajoute directement aux zones invisibles.
            if data[y][x] == 1:
                invisible_area.add((x, y))
            
            # Variable booléenne pour décider si la région explorée peut "voir" l'extérieur.
            is_visible = False
            
            # Si ce point est déjà classé comme invisible ou visible, on passe à la case suivante.
            if (x, y) in invisible_area or (x, y) in visible_area:
                continue

            # Initialise un ensemble 'area' avec la case actuelle pour stocker les coordonnées de la région connectée.
            area = {(x, y)}
            # Initialise une pile 'stack' pour effectuer une recherche en profondeur (DFS) depuis la case actuelle.
            stack = [(x, y)]

            # Tant que la pile contient des éléments, on continue la visite.
            while stack:
                # Retire et obtient le dernier élément ajouté de la pile pour traitement.
                cx, cy = stack.pop()
                # Marque ce point comme visité.
                visited.add((cx, cy))

                # Calcule les voisins selon la disposition hexagonale en double ligne décalée.
                # La structure hexagonale fait que les voisins dépendent de la parité de la ligne 'cy'.
                if cy % 2 == 0:
                    # Pour une ligne paire, voici les coordonnées des 6 voisins hexagonaux.
                    dxy = ((cx, cy-1), (cx+1, cy-1), (cx-1, cy), (cx+1, cy), (cx, cy+1), (cx+1, cy+1))
                else:
                    # Pour une ligne impaire, les voisins se décalent légèrement horizontalement.
                    dxy = ((cx-1, cy-1), (cx, cy-1), (cx-1, cy), (cx+1, cy), (cx-1, cy+1), (cx, cy+1))
                
                # Parcourt chacun des voisins calculés.
                for nx, ny in dxy:
                    # Si un voisin est en dehors de la grille, cela signifie que la région touche l'extérieur.
                    if not (0 <= nx < w) or not (0 <= ny < h):
                        is_visible = True
                    # Sinon si le voisin est dans la grille, n'est pas un obstacle (valeur 0), 
                    # et n'a pas encore été visité, on l'ajoute à la pile et à la région.
                    if 0 <= nx < w and 0 <= ny < h and data[ny][nx] == 0 and (nx, ny) not in visited:
                        stack.append((nx, ny))
                        area.add((nx, ny))
            
            # Après avoir exploré complètement la région connectée,
            # si la région touche l'extérieur, on la classe dans les zones visibles.
            if is_visible:
                visible_area |= area
            # Sinon, elle est entourée de murs et donc invisible.
            else:
                invisible_area |= area

    # Initialise le compteur final de la surface visible.
    ans = 0
    # Parcourt à nouveau chaque case de la grille.
    for cy in range(h):
        for cx in range(w):
            # Traite uniquement les cases qui sont des obstacles (valeur 1).
            if data[cy][cx] == 1:
                # Calcule à nouveau les voisins en fonction de la ligne paire ou impaire.
                if cy % 2 == 0:
                    dxy = ((cx, cy-1), (cx+1, cy-1), (cx-1, cy), (cx+1, cy), (cx, cy+1), (cx+1, cy+1))
                else:
                    dxy = ((cx-1, cy-1), (cx, cy-1), (cx-1, cy), (cx+1, cy), (cx-1, cy+1), (cx, cy+1))
                
                # Pour chaque obstacle, on compte combien de ses 6 côtés ne touchent pas une zone invisible.
                # Concrètement : pour chaque voisin, on vérifie s'il est dans 'invisible_area' (non visible).
                # Le nombre de côtés apparents est 6 moins le nombre de voisins cercelés d'invisible_area.
                ans += 6 - sum((nx, ny) in invisible_area for nx, ny in dxy)
    # Renvoie le résultat total calculé.
    return ans

# Définition de la fonction principale d'exécution quand le script est lancé.
def main(args):
    # Lit la largeur et la hauteur de la grille depuis l'entrée standard, on décompose la chaîne en deux entiers.
    w, h = map(int, input().split())
    # Lit la grille : 'h' lignes, chacune contenant une liste de 'w' entiers.
    # Chaque ligne est convertie en liste d'entiers via map(int, input().split()).
    data = [list(map(int, input().split())) for _ in range(h)]
    # Appelle la fonction de résolution avec les données et récupère la réponse.
    ans = solve(data, w, h)
    # Affiche la réponse sur la sortie standard.
    print(ans)

# Point d'entrée du script : s'assure que ce code s'exécute seulement si ce fichier est exécuté directement.
if __name__ == '__main__':
    # Appelle la fonction principale en passant les arguments de la ligne de commande sauf le nom du script.
    main(sys.argv[1:])