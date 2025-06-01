from collections import deque  # Importation de deque depuis la bibliothèque collections, qui est une file doublement terminée permettant d'ajouter ou retirer des éléments efficacement à gauche et à droite.

# Définition de la classe Car représentant une voiture avec deux attributs : rem (temps restant de stationnement) et ind (identifiant de la voiture)
class Car:
  def __init__(self, rem, ind):
    # L'attribut ind stocke l'identifiant unique de la voiture
    self.ind = ind
    # L'attribut rem stocke le temps restant pendant lequel la voiture doit rester garée
    self.rem = rem

# Définition de la classe Part représentant une place de parking pouvant contenir jusqu'à deux voitures (une au-dessus de l'autre)
class Part:
  def __init__(self, i):
    # L'indice i identifie cette place de parking parmi toutes
    self.ind = i
    # Référence vers la voiture positionnée en haut sur cette place (None si aucune)
    self.top = None
    # Référence vers la voiture positionnée en dessous sur cette place (None si aucune)
    self.und = None
    # État de la place: 0 = libre, 1 = une voiture dessus, 2 = deux voitures dessus
    self.sta = 0
    # Temps restant minimal parmi les voitures sur cette place (utile pour savoir quand la place sera libérée)
    self.rem = -1
  
  # Méthode pour faire progresser le temps sur cette place et réduire le temps restant des voitures
  def prog(self, time):
    # Si une voiture est en haut, on réduit son temps restant
    if self.top != None:
      self.top.rem -= time
    # Si une voiture est en dessous, on réduit aussi son temps restant
    if self.und != None:
      self.und.rem -= time
    # Si la place est partiellement occupée (sta différent de 0), on met à jour le temps restant associé à la place
    if self.sta != 0:
      self.rem -= time

  # Méthode qui gère la sortie des voitures dont le temps de parking est écoulé et met à jour l'état de la place
  def out(self):
    # Si la place est occupée par deux voitures
    if self.sta == 2:
      # Si les deux voitures ont fini leur temps de parking (rem <=0), on les fait sortir toutes les deux
      if self.und.rem <= 0 and self.top.rem <= 0:
        # On récupère les identifiants des deux voitures avant de les retirer
        outs = [self.und.ind, self.top.ind]
        # On libère la place en mettant à None les références aux voitures dessus
        self.und = None
        self.top = None
        # L'état redevient libre
        self.sta = 0
        # Le temps restant utilisé pour la place est remis à -1 (indiquant aucune voiture)
        self.rem = -1
        # On retourne la liste des voitures sorties
        return outs
      # Sinon si seulement la voiture du dessous a fini son temps
      if self.und.rem <= 0:
        # On prépare la sortie de cette voiture
        outs =  [self.und.ind]
        # On la retire de la place, laissant seulement la voiture du dessus
        self.und = None
        # L'état devient une seule voiture présente (la top)
        self.sta = 1
        # On met à jour le temps restant pour la place au temps de la voiture du dessus
        self.rem = self.top.rem
        # On retourne la liste contenant la voiture sortie
        return outs
    
    # Si la place ne contient qu'une seule voiture (sta == 1)
    if self.sta == 1:
      # Si cette voiture a fini son temps de parking
      if self.top.rem <= 0:
        # On sort cette voiture
        outs = [self.top.ind]
        # On libère la place
        self.top = None
        self.sta = 0
        self.rem = -1
        # On retourne la liste avec la voiture sortie
        return outs
    # Si aucune condition de sortie n'est remplie, on retourne une liste vide
    return []

  # Méthode pour placer une voiture sur la place avec un temps de parking rem et un identifiant ind
  def into(self, rem, ind):
    # Si la place est libre
    if self.sta == 0:
      # On place la voiture en haut (top)
      self.top = Car(rem, ind)
      # L'état devient une voiture présente
      self.sta = 1
      # Le temps restant pour la place est mis à celui de la voiture
      self.rem = rem
    # Si une voiture est déjà présente
    elif self.sta == 1:
      # On place la deuxième voiture dessous (und)
      self.und = Car(rem, ind)
      # L'état devient deux voitures présentes
      self.sta = 2
      # Le temps restant devient celui de la voiture du dessous (rem)
      self.rem = rem

# Classe représentant le parking complet contenant plusieurs places
class Parking:
  def __init__(self, length):
    # Le nombre total de places dans le parking
    self.length = length
    # La capacité maximale du parking est deux fois le nombre de places (car chaque place peut contenir 2 voitures)
    self.max_space = length * 2
    # L'espace disponible initial est la capacité maximale (parking vide)
    self.space = length * 2
    # Une liste contenant toutes les places du parking, chaque place est un objet Part avec un indice unique
    self.body = [Part(i) for i in range(length)]

  # Méthode qui fait avancer le temps pour toutes les places du parking
  def prog(self, time):
    # On appelle la méthode prog sur chaque place pour réduire temps des voitures
    for part in self.body:
      part.prog(time)

  # Méthode qui gère les sorties des voitures après progression du temps, et rend les places libres
  def out(self):
    outs = []  # Liste temporaire pour collecter les sorties des voitures car chaque out() retourne une liste
    for part in self.body:
      # On vérifie si la place contient au moins une voiture et si le temps est écoulé pour libérer la ou les voitures
      if part.sta >= 1 and part.rem <= 0:
        outs.append(part.out())  # On ajoute les identifiants des voitures sorties
    ret = []  # Liste regroupant toutes les voitures sorties dans le parking
    for out in outs:
      # On fusionne toutes les listes pour avoir une liste plate
      ret += out
    # On augmente l'espace disponible du parking par le nombre de voitures sorties
    self.space += len(ret)
    # On retourne la liste finale des voitures sorties
    return ret

  # Méthode permettant d'ajouter une voiture dans le parking avec un temps de stationnement rem et un identifiant ind
  def into(self, rem, ind):
    # Dès qu'une voiture entre, on diminue l'espace disponible
    self.space -= 1
    # On essaye d'abord de trouver une place complètement vide pour placer la voiture en top
    for part in self.body:
      if part.sta == 0:
        part.into(rem, ind)
        return
    # Si pas de place complètement vide, on regarde les places avec une seule voiture pour potentiellement placer la deuxième
    rem_lst = []
    for part in self.body:
      if part.sta == 1:
        # On récupère un tuple du temps restant et de l'indice de la place pour trier ensuite
        rem_lst.append((part.rem, part.ind))
    # On trie la liste par temps restant croissant pour tenter de placer la voiture sur une place dont la voiture restante reste le temps le plus faible possible >= rem
    rem_lst.sort()
    
    # On cherche la première place avec un temps restant >= rem pour placer la voiture dessous
    for r, i in rem_lst:
      if r >= rem:
        self.body[i].into(rem, ind)
        return
    
    # Si aucune place ne convient (temps restant plus petit), on choisit la place ayant le temps restant maximal
    max_r = r  # r n'est plus modifié depuis la dernière boucle, donc contient le plus grand temps restant de rem_lst triée
    for r, i in rem_lst:
      if r == max_r:
        self.body[i].into(rem, ind)
        return

# Boucle principale de l'application qui s'exécute tant qu'on n'a pas une condition d'arrêt
while True:
  # Lecture de deux entiers m (nombre de places) et n (nombre de groupes ou intervalle de lecture)
  m, n = map(int, input().split())
  # Si m est égal à 0, on arrête le programme (condition de terminaison)
  if m == 0:
    break
  # Création d'un parking avec m places
  parking = Parking(m)
  # Création d'une file d'attente pour stocker les voitures en attente d'entrée
  que = deque()
  # Liste pour stocker les identifiants des voitures sorties dans l'ordre
  ans = []
  # On boucle sur un intervalle de temps maximal, calculé selon n pour gérer plusieurs rounds
  for t in range(n * 120 - 1):
    # On fait avancer le temps dans le parking d'une unité (temps=1)
    parking.prog(1)
    # On récupère la liste des voitures sorties après progression du temps et on les ajoute à ans
    ans += parking.out()
    # À chaque multiple de 10 unités de temps (sans dépasser (n-1)*10), on lit un nouvel arrivant
    if t <= (n - 1) * 10 and t % 10 == 0:
      r = int(input())  # Lit le temps de stationnement demandé par un nouveau véhicule entrant
      # On ajoute ce nouveau véhicule dans la file d'attente sous forme d'un tuple (temps restant, identifiant numéroté selon t)
      que.append((r, t // 10 + 1))

    # On place autant de véhicules dans le parking que possible parmi ceux en attente, sans dépasser la capacité restante
    for i in range(min(parking.space, len(que))):
      # Retire le premier véhicule de la file d'attente
      rem, ind = que.popleft()
      # On insère la voiture dans le parking
      parking.into(rem, ind)
  # On affiche tous les identifiants des voitures sorties durant la simulation, séparés par des espaces
  print(*ans)