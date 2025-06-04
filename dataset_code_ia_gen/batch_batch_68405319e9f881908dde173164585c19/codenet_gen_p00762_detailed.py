# Solution complète pour le problème Biased Dice

# Approche détaillée :
# 1. Chaque dé est un cube avec 6 faces numérotées de 1 à 6, avec une orientation donnée par le numéro sur le dessus (top) et à l'avant (front).
# 2. On modélise l'orientation du dé en stockant la numérotation de ses faces dans une structure pouvant être modifiée lors d'un roulis (roll).
# 3. Lorsqu'un dé est lâché, il tombe verticalement sur la "pile" à la position x=0 initialement,
#    puis il peut rouler selon certaines règles spécifiques liées au biais :
#    - Il ne peut rouler que dans les directions correspondant aux faces 4, 5 et 6.
#    - Il ne roule que si, après le roulage, il tombera (pas de support direct).
#    - S'il y a plusieurs possibilités, il roule vers la face la plus grande parmi celles possibles.
# 4. Le dé roule d'un pas (90°) dans la direction choisie puis tombe verticalement jusqu'à toucher la surface (plan ou autre dé).
# 5. Ce processus est répété jusqu'à ce que le dé ne puisse plus rouler.
# 6. On maintient une "surface d'altitudes" (hauteurs des empilements) indexée par la position horizontale (x).
# 7. Après avoir placé tous les dés, on calcule, pour chaque position x, quelle est la face visible du dé au sommet,
#    puis compte combien de chaque face (1 à 6) apparaissent visibles.
# 8. On répète pour chaque dataset jusqu'à ce que 0 soit donné.

# Détails de modélisation :
# - Chaque dé a 6 faces : T (top), F (front), R (right), L (left), B (back), U (under).
# - On déduit une orientation initiale à partir des valeurs de top et front données.
# - Les rotations modifient la position de ces faces.
# - On stocke la hauteur des piles par position x sous forme d'un dictionnaire (position->hauteur).

# Code complet avec commentaires :

import sys

# Classe Die pour gérer l'orientation du dé et les rotations
class Die:
    def __init__(self, top, front):
        # Initialisation de l'orientation à partir top et front
        # On définit les 6 faces selon leur labels standards
        # Orientation standard possible:
        # Faces: T, F, R, L, B, U
        # Initialement, on construit l'objet avec top et front donnés,
        # et on calcule toutes les faces.
        # Pour cela, on teste toutes les rotations possibles (il y a 24 orientations)
        # et on sélectionne celle où top et front correspondent aux entrées.
        self.faces = {}  # dict label->number

        # Position des faces dans la liste pour rotation
        # On stocke les "numbers" sur les faces
        # L'ordre des faces est une convention : T,F,R,L,B,U
        # On initialise avec une standard configuration :
        # standard die: top=1, front=2, right=3, left=4, back=5, under=6
        # mais ici on a un dé standard inversé selon l'énoncé (voir figure C-1)
        # Par convention: on utilise la table standard et on tourne pour correspondre.
        standard_config = {
            'T': 1,
            'F': 2,
            'R': 3,
            'L': 4,
            'B': 5,
            'U': 6
        }

        # Toutes les 24 orientations d'un cube comme (top, front, right, left, back, under)
        # on les génère et on sélectionne celle qui correspond à (top, front) donné

        # Fonction interne pour générer les faces après rotation selon la méthode
        # On manipule la liste des faces dans un ordre fixe
        # On applique des rotations : roll north, roll east, etc.

        # On part d'une liste: [top, front, right, left, back, under]
        base = [1,2,3,4,5,6]

        def roll_north(f):
            # rotation vers nord:
            # top->front, front->under, under->back, back->top
            return [f[1], f[5], f[2], f[3], f[0], f[4]]
        def roll_south(f):
            # rotation vers sud:
            # top->back, back->under, under->front, front->top
            return [f[4], f[0], f[2], f[3], f[5], f[1]]
        def roll_east(f):
            # rotation vers est:
            # top->left, left->under, under->right, right->top
            return [f[3], f[1], f[0], f[5], f[4], f[2]]
        def roll_west(f):
            # rotation vers ouest
            # top->right, right->under, under->left, left->top
            return [f[2], f[1], f[5], f[0], f[4], f[3]]
        def turn_right(f):
            # rotation autour de l'axe vertical (top-back) : front->left, left->back, back->right, right->front
            return [f[0], f[3], f[1], f[4], f[2], f[5]]
        # On génère toutes les orientations possibles
        orientations = []
        f = base[:]
        for cycle in range(6):
            for turn in range(4):
                orientations.append(f)
                f = turn_right(f)
            if cycle%2 ==0:
                f = roll_north(f)
            else:
                f = roll_east(f)

        # Recherche celle qui a top=top et front=front
        for o in orientations:
            if o[0]==top and o[1]==front:
                # trouvé
                self.faces = {'T':o[0],'F':o[1],'R':o[2],'L':o[3],'B':o[4],'U':o[5]}
                break

    # Méthodes de rotation : le dé roule dans une direction (N,E,S,W)
    # Ces rotations modifient la faces
    def roll(self, direction):
        f = self.faces
        if direction=='N':
            # top->front, front->under, under->back, back->top
            self.faces = {
                'T':f['F'],
                'F':f['U'],
                'R':f['R'],
                'L':f['L'],
                'B':f['T'],
                'U':f['B']
            }
        elif direction=='S':
            # top->back, back->under, under->front, front->top
            self.faces = {
                'T':f['B'],
                'F':f['T'],
                'R':f['R'],
                'L':f['L'],
                'B':f['U'],
                'U':f['F']
            }
        elif direction=='E':
            # top->left, left->under, under->right, right->top
            self.faces = {
                'T':f['L'],
                'F':f['F'],
                'R':f['T'],
                'L':f['U'],
                'B':f['B'],
                'U':f['R']
            }
        elif direction=='W':
            # top->right, right->under, under->left, left->top
            self.faces = {
                'T':f['R'],
                'F':f['F'],
                'R':f['U'],
                'L':f['T'],
                'B':f['B'],
                'U':f['L']
            }

    # Retourne numéros des faces visibles depuis "dessus" (top)
    def top_face(self):
        return self.faces['T']

    def front_face(self):
        return self.faces['F']

    def right_face(self):
        return self.faces['R']

    def left_face(self):
        return self.faces['L']

    def bottom_face(self):
        return self.faces['U']

    def back_face(self):
        return self.faces['B']

# Gestion de la pile des dés déposés:
# Pour chaque position x, on garde la hauteur de la pile

class Stack:
    def __init__(self):
        # position x -> hauteur (nombre de dés empilés)
        self.height = {}  # dict int -> int

    def get_height(self,x):
        return self.height.get(x,0)

    def set_height(self,x,h):
        self.height[x] = h

# Sens de rotation selon faces 4,5,6

# Le dé ne roule pas vers les faces 1,2,3
# On doit tester les directions possibles: N,S,E,W
# Chaque direction correspond à quel visage ? On doit pouvoir associer

# Correspondance directions et faces visibles sur le côté:
# Lors d'un roulis d'un pas dans une direction, le côté vers lequel il roule est celui du côté du dé qui sera la nouvelle face en bas.
# Par exemple, un roulis vers le nord fait que la face avant (F) devient la face du dessus, et la face du dessous devient la face arrière (B).
# Autrement dit, le côté vers lequel on roule correspond au nom et valeur d'une face.

# On fait la correspondance pour les faces 4,5,6:

# Selon les règles, le dé ne roule que vers les directions où la face latérale est 4, 5 ou 6 (faces des trois directions où le dé peut rouler).

# Pour chaque direction, la face latérale associée est :

# N : front face (F)
# S : back face (B)
# E : right face (R)
# W : left face (L)

# Seulement directions où face latérale est dans {4,5,6}

# La face latérale associée à la direction (N,S,E,W) est donc respectivement (F,B,R,L)

# Lorsqu'il y a plusieurs directions possibles, le dé roule vers celle avec la plus grande face

# Donc on doit pour chaque direction candidate :
# 1) vérifier si l'arête en direction est dans {4,5,6}
# 2) vérifier si le dé peut tomber après un roulis dans cette direction
# 3) sélectionner le max des faces candidate

# Le dé tombe si la hauteur du sol après roulis est strictement plus basse que la hauteur actuelle (la position sous le dé roule et peut être plus basse)

# Modèle de la chute sur la pile :
# Après le roulis, le dé se déplace d'une unité dans la direction
# puis tombe verticalement jusqu'à toucher la hauteur du sol à cette position

# On simule donc :
# - sa nouvelle position x (déplacement horizontal)
# - la hauteur au sol à cette position
# - la hauteur réelle: le sommet du dé sur la pile

# Le dé est posé sur le sol ou un autre dé, donc la hauteur est la hauteur du sol + 1

# On répète ce processus jusqu'à ce que le dé ne roule plus

# Positions sur la ligne: on prend x initial = 0, puis +1 à droite (E), -1 à gauche (W)

# N/S sont dans la verticale: pas de déplacement horizontal? On considère que le dé roule vers le nord ou sud déplace horizontalement ?
# Dans l’énoncé, la position horizontale évolue selon les directions, il est logique que N/S déplace aussi:

# On peut considérer que la position est un entier sur la ligne, et on associe N -> -1, S -> +1 par exemple.

# Le plan est une ligne horizontale. On choisit la direction des axes :

# On prend x = 0 initialement.

# Direction N = x -1

# Direction S = x +1

# Direction E = x +1

# Direction W = x -1

# L'énoncé ne précise pas si le dé roule sur une ligne ou un plan 2D.

# Dans le problème, le dé tombe sur une ligne horizontale (un axe 1D).

# Pour le problème, N,S,E,W représentent 4 directions de roulis possibles (sur une ligne ou plan)

# Ici, on prend un axe 1D et 4 directions possibles : N= -1, S= +1, E= +1, W= -1

# En fait d'après l'exemple, le dé roule sur une ligne horizontale x, donc on ne distingue pas N,S,E,W mais seulement gauche/droite.

# On peut s'en tenir à N/S associés à gauche/droite (N,W = x-1), (S,E = x+1)

# Or, pour ne pas confondre, on peut considérer que roulis possible sont seulement 3 directions : les faces 4,5,6 correspondent à 3 directions possibles (figure C-2).

# L’énoncé dit « le dé ne roule pas en direction des faces 1,2,3 »

# D'après la configuration standard, les faces latérales :

# F=2,L=4,R=3,B=5

# Donc faces 4,5,6 correspondent aux directions :

# 4 : gauche (L)

# 5 : arrière (B)

# 6 : sous le dé (U) ?

# Vu l'énoncé, il semble qu'on utilise les directions liées aux faces 4,5,6

# En fait, on utilise que 3 directions où il peut rouler : faces 4,5,6

# Selon la figure et l'explication, les directions de roulis possibles correspondent aux directions où la face latérale est 4,5 ou 6.

# Dans notre rotation, faces latérales sont F, B, R, L.

# Face 6 (U) n'est latérale, c'est la face en dessous.

# Donc faces latérales possibles sont 4,5 (L,B) et 6 (U) ?

# Mais 6 (under) correspond à la direction vers le bas, pas au roulis.

# Donc probablement les trois directions sont celles associées aux faces 4,5,6 mais positionnées sur le côté.

# => On considérera les directions de roulis possibles comme celles sur lesquelles la face latérale vaut 4, 5 ou 6.

# Or d'après notre convention :

# N : face F

# S : face B

# E : face R

# W : face L

# Les directions possibles sont celles où la face latérale vaut 4,5 ou 6.

# Donc on teste ces 4 directions et on garde uniquement celles dont la face latérale est dans {4,5,6}

# Puis, parmi ces directions, on teste si le dé peut tomber (à une hauteur plus basse)

# On choisit la direction de roulis où la face latérale est maximale (Règle (2))

# On roule d'un pas, on tombe verticalement, on recommence.

# Implémentons avec ça.

# Pour la hauteur, on stocke dans un dict hauteur_par_x

# Au début, tous les x = 0 ont hauteur 0

# Le dé initial est posé en x=0, hauteur = hauteur_par_x[0]

# Le dé est posé au sommet => hauteur = hauteur_sol +1

# Pour simuler si il peut rouler, on teste pour chaque direction admissible (face latérale est 4,5,6)

# la hauteur_sol après roulis: next_x = current_x + dx selon direction

# hauteur_sol_next = hauteur_par_x.get(next_x,0)

# Si hauteur_sol_next < hauteur_sol_courante alors il peut rouler sur next_x

# Note : Règle (2) dit : le dé peut rouler seulement quand il va tomber après roulis

# Ici "tomber" implique hauteur_sol_next +1 < hauteur_sol_courante +1

# Donc si hauteur_sol_next < hauteur_sol_courante

# Dé commence à une hauteur h = hauteur_par_x[x] + 1

# Après roulis, il se retrouve en position x+dx, et continue de tomber verticalement jusqu'à hauteur_par_x[x+dx]

# S'il y a une hauteur plus faible, il "tombe"

# Sinon pas de roulis.

# Reprenons la simulation complète.

# Code :

def main():
    input_lines = sys.stdin.read().strip().split('\n')
    idx = 0
    while True:
        if idx>=len(input_lines):
            break
        n = input_lines[idx].strip()
        idx+=1
        if n=='0':
            break
        n = int(n)
        dice = []
        for _ in range(n):
            t,f = map(int, input_lines[idx].split())
            idx+=1
            dice.append( (t,f) )

        # Initialisation de la hauteur de la pile
        height_map = {}  # position x : hauteur
        # On commence au sol : hauteur 0 partout

        # On pose chaque dé un par un
        # x initial = 0 pour le premier dé

        # On maintient aussi la position du dé courant
        # Car le dé peut se déplacer horizontalement lors du roulis

        # On simule pour chaque dé :
        # positions x (entier), hauteur position

        # x = 0 initialement pour le premier dé posé

        # Pour les suivants, on pose le dé au même point de départ x=0

        # En amas empilé, le dé peut rouler sur les voisins

        # On modélise la ligne des piles selon x (entier)

        # Donc chaque dé commence à x=0, z = hauteur_map[0]+1

        # Puis on simule les roulis et chutes jusqu'à stabilité

        DIRECTIONS = {
            'N': -1,
            'S': +1,
            'E': +1,
            'W': -1
        }

        # Pour choisir roll, on teste les directions N,S,E,W
        # On ne gardera que celles où la face latérale est dans {4,5,6}

        # Pour chaque direction testée, on aura :
        # 1) la face latérale associée
        # 2) la position horizontale après déplacement
        # 3) la hauteur du sol à cette position

        # Pour accéder à la face latérale correspondant à une direction

        # On définit mapping: direction -> face latérale

        dir_to_face = {
            'N':'F',
            'S':'B',
            'E':'R',
            'W':'L'
        }

        # Début simulation de chute et roulis pour chaque dé
        for top, front in dice:
            die = Die(top, front)
            x = 0
            # position x