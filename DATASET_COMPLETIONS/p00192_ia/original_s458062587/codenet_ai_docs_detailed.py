from collections import deque

class Car:
    """
    Classe représentant une voiture, caractérisée par son temps restant de stationnement
    et son identifiant.
    """
    def __init__(self, rem, ind):
        """
        Initialisation d'une voiture.

        Args:
            rem (int): temps restant que la voiture doit rester dans le parking.
            ind (int): identifiant unique de la voiture.
        """
        self.ind = ind  # Identifiant de la voiture
        self.rem = rem  # Temps restant dans le parking


class Part:
    """
    Classe représentant une place (ou partie) dans le parking pouvant contenir jusqu'à deux voitures
    (une "top" et une "und", probablement pour modéliser deux places superposées).
    """
    def __init__(self, i):
        """
        Initialisation d'une place du parking.

        Args:
            i (int): indice ou identifiant unique de cette place.
        """
        self.ind = i      # Indice de la place
        self.top = None   # Voiture au niveau supérieur (None si vide)
        self.und = None   # Voiture au niveau inférieur (None si vide)
        self.sta = 0      # Statut de la place : 0 vide, 1 une voiture, 2 deux voitures
        self.rem = -1     # Temps restant minimum des voitures présentes

    def prog(self, time):
        """
        Progresser le temps de stationnement pour les voitures présentes dans la place.

        Args:
            time (int): quantité de temps à déduire du temps restant des voitures.
        """
        # Décrémente le temps restant des voitures présentes
        if self.top is not None:
            self.top.rem -= time
        if self.und is not None:
            self.und.rem -= time
        # Met à jour le temps restant global de la place si elle est occupée
        if self.sta != 0:
            self.rem -= time

    def out(self):
        """
        Gérer le départ des voitures dont le temps est écoulé.

        Returns:
            list[int]: liste des identifiants des voitures sorties.
        """
        # Si la place a deux voitures
        if self.sta == 2:
            # Si les deux voitures ont dépassé leur temps, les libérer
            if self.und.rem <= 0 and self.top.rem <= 0:
                outs = [self.und.ind, self.top.ind]
                self.und = None
                self.top = None
                self.sta = 0
                self.rem = -1
                return outs
            # Si seule la voiture "und" a dépassé son temps, la libérer et mettre à jour la place
            if self.und.rem <= 0:
                outs = [self.und.ind]
                self.und = None
                self.sta = 1
                self.rem = self.top.rem
                return outs

        # Si la place a une seule voiture (top)
        if self.sta == 1:
            # Si la voiture a dépassé son temps, la libérer
            if self.top.rem <= 0:
                outs = [self.top.ind]
                self.top = None
                self.sta = 0
                self.rem = -1
                return outs

        # Aucune voiture n'est sortie
        return []

    def into(self, rem, ind):
        """
        Ajouter une voiture à cette place.

        Args:
            rem (int): temps de stationnement demandé pour la voiture.
            ind (int): identifiant de la voiture.
        """
        # Si la place est vide, placer la voiture au niveau supérieur (top)
        if self.sta == 0:
            self.top = Car(rem, ind)
            self.sta = 1
            self.rem = rem
        # Si la place a une voiture, ajouter la voiture au niveau inférieur (und)
        elif self.sta == 1:
            self.und = Car(rem, ind)
            self.sta = 2
            self.rem = rem


class Parking:
    """
    Classe modélisant un parking constitué d'une liste de places (Part).
    Chaque place peut contenir jusqu'à deux voitures.
    """
    def __init__(self, length):
        """
        Initialisation du parking.

        Args:
            length (int): nombre de places dans le parking.
        """
        self.length = length                # Nombre total de places
        self.max_space = length * 2        # Capacité maximale du parking (2 voitures par place)
        self.space = length * 2            # Espace disponible actuel
        self.body = [Part(i) for i in range(length)]  # Liste des places du parking

    def prog(self, time):
        """
        Faire progresser le stationnement de toutes les voitures du parking.

        Args:
            time (int): temps à déduire de toutes les voitures présentes.
        """
        # Pour chaque place du parking, décompter le temps restant des voitures
        for part in self.body:
            part.prog(time)

    def out(self):
        """
        Gérer les sorties des voitures dont le temps de stationnement est écoulé.

        Returns:
            list[int]: liste des identifiants des voitures sorties.
        """
        outs = []
        # Vérifier toutes les places pour détecter les voitures terminant leur stationnement
        for part in self.body:
            # Si la place est occupée et que le temps est écoulé, tenter de libérer la place
            if part.sta >= 1 and part.rem <= 0:
                outs.append(part.out())

        # Aplatir la liste des sorties (liste de listes) en une liste simple
        ret = []
        for out in outs:
            ret += out

        # Mettre à jour l'espace libre avec les voitures sorties
        self.space += len(ret)
        return ret

    def into(self, rem, ind):
        """
        Insérer une voiture dans le parking.

        Args:
            rem (int): temps de stationnement demandé.
            ind (int): identifiant de la voiture.
        """
        # Réduire l'espace libre car on va ajouter une voiture
        self.space -= 1

        # Chercher une place vide (sta == 0) pour placer la voiture
        for part in self.body:
            if part.sta == 0:
                part.into(rem, ind)
                return

        # Si aucune place vide, chercher les places avec une voiture (sta == 1)
        # et trier celles-ci par leur temps restant (pour optimiser le placement)
        rem_lst = []
        for part in self.body:
            if part.sta == 1:
                rem_lst.append((part.rem, part.ind))
        rem_lst.sort()

        # Chercher une place dont la voiture a un temps restant plus grand ou égal au temps demandé
        for r, i in rem_lst:
            if r >= rem:
                self.body[i].into(rem, ind)
                return

        # Sinon, prendre la place avec le max temps restant (la dernière dans la liste triée)
        max_r = r
        for r, i in rem_lst:
            if r == max_r:
                self.body[i].into(rem, ind)
                return


# Boucle principale d'exécution : traiter plusieurs cas de parking et voitures
while True:
    # Lecture du nombre de places (m) et du nombre d'intervalles n
    m, n = map(int, input().split())
    if m == 0:
        # Fin du programme lorsque m=0
        break

    # Initialisation d'un parking avec m places
    parking = Parking(m)
    que = deque()  # File d'attente des voitures en attente d'entrée
    ans = []       # Liste des identifiants des voitures sorties

    # Parcours du temps total (chaque unité de temps vaut 1, pour n*120 unités environ)
    for t in range(n * 120 - 1):
        parking.prog(1)          # Faire progresser le temps d'une unité
        ans += parking.out()     # Gérer et collecter les voitures sorties

        # Toutes les 10 unités de temps (pour t ≤ (n-1)*10), lire une nouvelle voiture avec son temps demandé
        if t <= (n - 1) * 10 and t % 10 == 0:
            r = int(input())               # Temps de stationnement demandé pour la nouvelle voiture
            que.append((r, t // 10 + 1))  # Ajouter la voiture dans la file d'attente avec son indice

        # Tenter d'insérer dans le parking le nombre possible de voitures selon l'espace disponible
        for i in range(min(parking.space, len(que))):
            rem, ind = que.popleft()
            parking.into(rem, ind)

    # Affichage du résultat : identifiants des voitures sorties dans l'ordre
    print(*ans)