from heapq import heappush, heappop  # Importation des fonctions heappush et heappop du module heapq permettant de gérer une file de priorité (tas).

# Définition d'une liste de positions cibles (comp) sous forme de tuples (x, y).
comp = [(1, 1), (2, 1), (3, 1),
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
        (1, 3), (2, 3), (3, 3)]
# Création d'un objet range représentant une séquence de nombres entiers de 0 à 10 inclus.
numbers = range(11)
# Définition d'un tuple contenant les indices des "cases vides" dans l'état: ici 11 et 12.
zeros = (11, 12)

# Définition d'une fonction nommée manhattan prenant en paramètres deux tuples v1 et v2 représentant des coordonnées (x, y).
def manhattan(v1, v2):
  x1, y1 = v1  # Décomposition du premier tuple autour des variables x1 et y1 pour récupérer les coordonnées du premier point.
  x2, y2 = v2  # Décomposition du second tuple autour des variables x2 et y2 pour récupérer les coordonnées du second point.
  # Calcul et retour de la distance de Manhattan entre les deux points, à savoir la somme des distances absolues de leurs composantes x puis y.
  return abs(x2 - x1) + abs(y2 - y1)

# Définition d'une fonction heuristic prenant en paramètre un état (state), c'est-à-dire une liste ou un tuple de positions.
def heuristic(state):
  # Calcule la somme des distances de Manhattan entre chaque position d'état et la position cible correspondante dans comp.
  # La fonction sum additionne les valeurs obtenues dans la liste créée par la compréhension.
  return sum([manhattan(state[i], comp[i]) for i in numbers])

# Définition d'une fonction swaped prenant en paramètres un état et deux indices n1 et n2.
def swaped(state, n1, n2):
  # Création d'une copie de l'état, ici sous forme d'une liste, pour ne pas modifier l'original directement.
  new_state = [i for i in state]
  # Échange des éléments aux indices n1 et n2 dans la copie de l'état.
  new_state[n1], new_state[n2] = new_state[n2], new_state[n1]
  # Retourne la nouvelle configuration comme un tuple, car les états sont manipulés sous forme immuable nécessaire au dictionnaire.
  return tuple(new_state)

# Définition de la fonction principale du programme.
def main():
  while True:  # Boucle infinie, jusqu'à une condition d'arrêt explicite.
    p1 = int(input())  # Lecture d'un entier depuis l'entrée standard. Usage d'int pour convertir la chaîne en nombre.
    if p1 == -1:  # Condition d'arrêt de la boucle si l'entier reçu est égal à -1.
      break

    # Initialisation d'une grille 5x5 avec des valeurs -1 représentant des cases non utilisables.
    # Puis insertion de la valeur p1 lue dans la rangée 1 au milieu (index 2).
    l1 = [-1, -1, p1, -1, -1]
    # Lecture d'une ligne depuis l'entrée, convertie en entiers, et ajout des bornes -1 à gauche et à droite.
    l2 = [-1] + list(map(int, input().split())) + [-1]
    l3 = list(map(int, input().split()))  # Lecture d'une ligne entière sans ajout de bornes.
    l4 = [-1] + list(map(int, input().split())) + [-1]  # Lecture avec bornes comme pour l2.
    l5 = [-1, -1, int(input()), -1, -1]  # Lecture d'un entier isolé pour la rangée 5 au milieu également.

    # Création de la matrice mp représentant la grille complète avec ses bornes.
    mp = [l1, l2, l3, l4, l5]

    # Initialisation d'une liste de taille 13 remplie de None, qui va contenir les positions des numéros et des zéros.
    init_state = [None] * 13

    # Double boucle parcourant chaque coordonnée (y pour ligne, x pour colonne) de la grille 5x5.
    for y in range(5):
      for x in range(5):
        if mp[y][x] != -1:  # On ignore les cases marquées -1 qui ne contiennent rien d'intéressant.
          if mp[y][x] == 0:  # Si la case contient un 0, on doit stocker sa position dans init_state aux indices 11 ou 12.
            # Si la position 11 est vide, on y stocke la première position rencontrée.
            if not init_state[11]:
              init_state[11] = (x, y)
            else:
              # Sinon la position va dans celle d'index 12.
              init_state[12] = (x, y)
          else:
            # Pour un numéro non nul, on stocke la position (x, y) à l'indice correspondant au numéro - 1.
            init_state[mp[y][x] - 1] = (x, y)

    # Conversion de la liste init_state en tuple afin qu'elle soit immuable et donc utilisable en tant que clé de dictionnaire.
    init_state = tuple(init_state)

    dic = {}  # Initialisation d'un dictionnaire vide qui contiendra les états déjà visités.
    dic[init_state] = True  # Marquage de l'état initial comme visité.

    que = []  # Initialisation d'une liste pour contenir la file de priorité (tas) des états à explorer.
    # Ajout du premier élément dans la file: un tuple contenant le coût total (heuristique + 0), le nombre de déplacements effectués (0), et l'état initial.
    heappush(que, (heuristic(init_state) + 0, 0, init_state))

    # Boucle principale de recherche tant qu'il y a des états à traiter dans la file de priorité.
    while que:
      # Extraction de l'état ayant le plus petit score (priorité la plus haute) de la file.
      score, count, state = heappop(que)
      # Condition de réussite: si le score correspond au nombre de déplacements effectués, on a atteint la solution idéale (heuristique nulle).
      if score == count:
        print(count)  # Affiche le nombre minimum de déplacements effectués pour résoudre le puzzle.
        break  # Sort de la boucle car la solution est trouvée.

      # Sinon, pour chaque indice correspondant aux cases "vides" (indices 11 et 12).
      for z in zeros:
        # Pour chaque numéro de pièce (indices 0 à 10).
        for i in numbers:
          # Vérifie si la distance de Manhattan entre la case vide z et la pièce i est égale à 1, c'est-à-dire adjacente.
          if manhattan(state[z], state[i]) == 1:
            # Si oui, créer un nouvel état où les positions de la pièce et de la case vide sont échangées.
            new_state = swaped(state, i, z)
            # Si ce nouvel état n'a pas encore été visité.
            if new_state not in dic:
              dic[new_state] = True  # Marque le nouvel état comme visité.
              # Calcule un nouveau score en sommant l'heuristique du nouvel état et les déplacements effectués +1.
              new_score = heuristic(new_state) + count + 1
              # On ne retient que les états dont le score est inférieur ou égal à 20, limitant la profondeur de la recherche.
              if new_score <= 20:
                # Ajoute ce nouvel état dans la file de priorité avec son score et son nombre de déplacements.
                heappush(que, (new_score, count + 1, new_state))
    else:
      # Si la boucle while se termine sans jamais rencontrer un break, cela signifie qu'aucune solution n'a été trouvée.
      print("NA")

# Appel de la fonction principale pour lancer l'exécution du programme.
main()