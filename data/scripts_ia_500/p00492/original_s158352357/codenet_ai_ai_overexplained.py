import sys

# On importe le module sys qui permet d'interagir avec l'interpréteur Python, notamment pour modifier la limite de récursion.

# On modifie la limite maximale de profondeur d'appel récursif autorisée pour Python.
# La récursion est une technique où une fonction s'appelle elle-même.
# Par défaut, cette limite est souvent autour de 1000 pour éviter un dépassement de pile (stack overflow).
# Ici, on augmente cette limite à 1 000 000 pour permettre des appels récursifs très profonds dans la fonction search.
sys.setrecursionlimit(1000000)

# On définit une constante WALL valant 100.
# Cela va représenter les murs dans la grille. Utiliser une constante permet de changer cette valeur facilement partout dans le code.
WALL = 100

# On lit deux entiers depuis l'entrée standard (typiquement l'utilisateur ou un fichier).
# Ces entiers représentent respectivement la largeur (w) et la hauteur (h) d'une grille.
# La fonction input() récupère toute la ligne en tant que chaîne de caractères.
# La fonction split() coupe cette chaîne en éléments selon l'espace par défaut.
# map(int, ...) convertit chaque élément en entier.
w, h = map(int, input().split())

# On construit une liste à deux dimensions "lst" qui va représenter la grille.
# Chaque ligne est construite en entourant les données avec WALL pour créer une bordure.
# Pour chaque itération allant de 0 à h-1 (donc pour chaque ligne), on lit une ligne d'entrée (w valeurs) et on ajoute un WALL au début et un à la fin.
# Cela facilite la gestion des bords en évitant les erreurs d'indexation hors bornes lors des recherches.
lst = [[WALL] + list(map(int, input().split())) + [WALL] for i in range(h)]

# On ajoute une ligne de WALL complète au début de la grille : une ligne dont tous les éléments valent WALL.
# La taille de cette liste est w+2 car chaque ligne a été allongée de 2 par l'ajout de murs de chaque côté.
lst.insert(0, [WALL] * (w + 2))

# On ajoute aussi une ligne de WALL complète à la fin de la grille.
# Ainsi, la grille "lst" est entourée d'un couche de murs à gauche, à droite, en haut et en bas.
lst.append([WALL] * (w + 2))

# On crée une grille "visited" de la même taille que lst (h + 2 lignes et w + 2 colonnes).
# Cette grille aura des zéros initialement, ce qui indique que les cases ne sont pas encore visitées.
# visited sert à marquer pour chaque case si elle a été traitée et avec quel statut.
visited = [[0] * (w + 2) for _ in range(h + 2)]

# On crée une liste vide "hold" qui sera utilisée pour stocker temporairement des coordonnées (x,y) pendant la recherche.
hold = []

# On crée une variable "app" qui référence la méthode append de hold.
# Cela évite d'écrire "hold.append" plusieurs fois, légèrement plus rapide à exécuter.
app = hold.append

# Définition d'une fonction récursive "search" pour explorer la grille à partir d'un point (x, y).
def search(x, y):
  
  # Si la case visitée est un mur (valeur == WALL), on marque visited[x][y] avec 3, ce qui indique "mur", et on renvoie 3.
  if lst[x][y] == WALL:
    visited[x][y] = 3
    return 3
  
  # Si la case visitée contient la valeur 1, on la marque visited[x][y] à 2, ce qui correspond probablement à une zone/état spécifique, et on renvoie 2.
  if lst[x][y] == 1:
    visited[x][y] = 2
    return 2
  
  # Sinon, la case est vide ou 0, on la marque à 1 (visitée, sans mur ni valeur 1).
  visited[x][y] = 1
  
  # On ajoute la position actuelle à hold, pour garder trace des cases visitées lors de cet appel récursif.
  app((x, y))
  
  # Selon la parité de x (ligne), on définit les voisins du point (x,y) différemment.
  # Cela simule pour la grille une structure de voisinage hexagonal ou décalé.
  if not x % 2:  # si x est pair
    # On considère 6 points voisins autour de (x, y) : trois au dessus et trois en dessous.
    pairs = [(x - 1, y - 1), (x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y - 1), (x + 1, y)]
  else:  # si x est impair
    # Voisinage légèrement décalé à droite pour les lignes impaires.
    pairs = [(x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y + 1), (x + 1, y), (x + 1, y + 1)]
  
  # Variable permettant de garder la "valeur maximale" retournée par les recherches sur les voisins.
  ret = 0
  
  # On boucle sur tous les voisins calculés.
  for t in pairs:
    tx, ty = t[0], t[1]  # coordonnées du voisin
    v = visited[tx][ty]  # état du voisin dans visited
    a = 0  # variable temporaire pour stocker le résultat de la recherche
    
    # Si ce voisin n'a pas été visité (0), on lance récursivement search dessus.
    if not v:
      a = search(tx, ty)
    # Sinon, s'il a déjà été marqué comme mur (3), on récupère cette valeur.
    elif v == 3:
      a = 3
    # Ou s'il a été marqué 2 (cas valeur 1 rencontré) on récupère aussi 2.
    elif v == 2:
      a = 2
    
    # On garde la valeur maximale de a parmi tous les voisins explorés.
    # Cela permet de remonter un signal fort si on rencontre un mur ou un 1 à proximité.
    if a > ret:
      ret = a
  
  # On renvoie la valeur maximale détectée dans le voisinage récursif.
  return ret

# Fonction principale du programme.
def main():

  # On parcourt toutes les cases internes de lst, en ignorant la bordure de murs.
  for x in range(1, h + 1):
    for y in range(1, w + 1):
      # Si la case n'a pas été visitée et qu'elle est vide (valeur 0)
      if not visited[x][y] and not lst[x][y]:
        # On lance une recherche pour explorer un secteur connecté à cette case.
        stat = search(x, y)
        
        # Pour toutes les cases collectées dans hold pendant cette recherche,
        # on marque dans visited la statistique retournée par search.
        for point in hold:
          visited[point[0]][point[1]] = stat
        
        # On vide la liste hold pour la prochaine utilisation.
        hold.clear()
  
  # Variable qui comptera la réponse finale.
  ans = 0

  # On parcourt à nouveau toutes les cases internes.
  for x in range(1, h + 1):
    for y in range(1, w + 1):
      # Si la case est un mur ou une valeur (non nulle)
      if lst[x][y]:
        # On calcule à nouveau les voisins selon la parité de la ligne.
        if not x % 2:
          pairs = [(x - 1, y - 1), (x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y - 1), (x + 1, y)]
        else:
          pairs = [(x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y + 1), (x + 1, y), (x + 1, y + 1)]
        
        # Pour chaque voisin
        for t in pairs:
          tx, ty = t[0], t[1]
          # Si le voisin n'a pas été visité (0) ou est un mur (3) ET que la case du voisin est soit un mur (WALL) ou vide (0),
          # on incrémente le compteur ans.
          # Cela compte probablement les "bords" entre zones différentes ou les contours des murs.
          if (visited[tx][ty] in [0, 3]) and (lst[tx][ty] in [WALL, 0]):
            ans += 1
  
  # On affiche le résultat final calculé.
  print(ans)

# Appel de la fonction main pour exécuter le programme.
main()