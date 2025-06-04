import copy  # Le module 'copy' permet de faire des copies superficielles ou profondes d’objets en Python
import sys  # Le module 'sys' donne accès à certaines variables et fonctions qui interagissent fortement avec l’interpréteur Python

# On redéfinit 'input' pour utiliser la fonction 'readline' du flux standard d'entrée, ce qui est plus rapide dans certains contextes
input = sys.stdin.readline

# Cette ligne modifie la limite maximale de récursion autorisée par l’interpréteur Python.
# sys.setrecursionlimit permet d’augmenter la profondeur de récursion dans les appels de fonctions récursives.
# Ici, la valeur utilisée est très élevée pour supporter de très grandes profondeurs récursives.
sys.setrecursionlimit(11451419)

# On importe 'deque' depuis le module 'collections'.
# 'deque' est une structure de données qui permet de faire des opérations d'ajout/suppression à gauche/droite de manière efficace (complexité temps constant).
from collections import deque

# Lecture d'un entier depuis l'entrée standard. Ce sera le nombre de sommets du graphe.
n = int(input())

# On construit la matrice d'adjacence du graphe.
# G est une liste de n listes vides, chacune représentant la liste des sommets adjacents à un sommet donné.
G = [[] for i in range(n)]

# On lit les arêtes du graphe.
for i in range(n):
    a, b = map(int, input().split())  # Lecture de deux entiers 'a' et 'b' représentant une arête entre les sommets a et b
    # Les sommets sont supposés être numérotés à partir de 1 dans l'entrée, donc on soustrait 1 pour utiliser des indices à partir de 0
    G[a-1].append(b-1)  # Ajoute b-1 comme voisin de a-1
    G[b-1].append(a-1)  # Ajoute a-1 comme voisin de b-1 (car le graphe est non orienté)

# 'seen' est une liste utilisée pour garder trace des sommets déjà visités lors du parcours en profondeur (DFS).
# Elle contient n éléments, initialisés à 0 (faux), ce qui signifie qu’aucun sommet n’a été visité au départ.
seen = [0 for i in range(n)]

# On initialise une deque (file doublement chaînée) pour stocker l'historique du parcours des sommets lors de la DFS.
# Cette structure servira à retrouver le cycle identifié éventuellement.
hist = deque([])  # Historique de visite des sommets

# La variable 'pos' indique la position d'un sommet à la racine d’un cycle détecté.
# On la fixe à -1 (valeur spéciale signifiant qu’aucun cycle n’a été identifié jusqu’à présent).
pos = -1  # Identifiant du sommet d'entrée dans le cycle, -1 si aucun cycle n'a été trouvé

# Définition de la fonction récursive de parcours en profondeur (DFS).
# 'x' : sommet courant
# 'p' : parent du sommet courant (on ne doit pas revenir vers lui dans la DFS)
def dfs(x, p):
    # On utilise 'global' pour indiquer qu’on souhaite modifier la variable globale 'pos'.
    global pos

    # On marque le sommet 'x' comme visité.
    seen[x] = 1

    # On ajoute 'x' à l’historique de la visite.
    hist.append(x)

    # Parcours de tous les voisins directs du sommet 'x'
    for to in G[x]:
        # Si le voisin est le parent d'où l'on vient, on ignore pour éviter de revenir en arrière.
        if to == p:
            continue  # On saute cette itération et passe au voisin suivant

        # Si le voisin a déjà été visité, cela signifie qu'un cycle est détecté.
        if seen[to] == 1:
            pos = to  # On enregistre ce sommet comme point d'entrée du cycle
            return    # On arrête la recherche dès qu'un cycle est trouvé

        # Pour les voisins qui n’ont pas encore été visités, on continue le DFS récursivement.
        dfs(to, x)
        # Si 'pos' a été modifié (donc, un cycle a été découvert quelque part plus bas dans la récursion), on arrête la recherche.
        if pos != -1:
            return  # On quitte aussitôt que le cycle est détecté

    # Si on termine la boucle sans détecter de cycle, on retire le sommet courant de l’historique de visite.
    hist.pop()
    # La suppression du sommet marque le retour en arrière dans la pile d'appels.

    # On explicite le retour de la fonction, mais ce return est optionnel.
    return

# Lancement du parcours en profondeur (DFS) à partir du sommet 0 (premier sommet), dont le parent est mis à -1 (aucun parent).
dfs(0, -1)

# À ce stade, la variable 'hist' contient l’historique du parcours de DFS,
# qui peut contenir des branches secondaires suivies avant d’entrer dans le cycle.
# Notre objectif est maintenant d’extraire précisément les sommets composant le cycle.

# Utilisation d’un ensemble (set) pour enregistrer les sommets appartenant au cycle détecté.
cycle = set([])  # Ensemble de sommets formant le cycle

# On va dépiler les sommets depuis la fin de 'hist' (pile), jusqu'à trouver le sommet de départ du cycle 'pos'.
while hist:
    qwe = hist.pop()  # On retire le sommet le plus récent de l’historique
    cycle.add(qwe)    # On l’ajoute à l’ensemble représentant le cycle
    # Dès que l’on atteint le sommet d'entrée du cycle (pos), c’est que tout le cycle a été récupéré
    if qwe == pos:
        break
    # L'utilisation de 'break' permet de se stopper immédiatement une fois tout le cycle extrait

# Lecture du nombre de requêtes à traiter.
m = int(input())

# Pour chaque requête, qui consiste en deux sommets, on veut savoir s’ils appartiennent tous deux au cycle ou non.
for i in range(m):
    a, b = map(int, input().split())  # Lecture des deux sommets impliqués (indices 1-based dans l'entrée)
    # On vérifie si les deux sommets appartiennent tous les deux au cycle détecté.
    if (a-1) in cycle and (b-1) in cycle:
        print(2)  # Tous deux sont dans le cycle, réponse "2"
    else:
        print(1)  # Au moins l’un n'est pas dans le cycle, réponse "1"