# La variable ref est une chaîne de caractères représentant l'ordre des cartes du plus faible (2) au plus fort (A - As).
ref = "23456789TJQKA"

# Définition de la fonction judge qui sert à déterminer le gagnant d'un pli de bridge.
# hand : une liste contenant les 4 cartes du pli actuel (une par joueur).
# led : l'indice du joueur qui a conduit le pli (c'est-à-dire qui a posé en premier).
def judge(hand, led):
    # On récupère la couleur de la carte du joueur qui a conduit le pli.
    l = hand[led][1]
    # On initialise mx (max index avec la couleur demandée), tx (max index pour l'atout), et w (indice du gagnant) à -1.
    mx = tx = w = -1
    # On parcourt les 4 joueurs (0 à 3).
    for i in xrange(4):
        # num récupère la valeur de la carte (indice dans ref), s récupère la couleur de la carte.
        num, s = ref.index(hand[i][0]), hand[i][1]
        # Si la couleur est l'atout (t) et que l'indice de force bat tout atout précédent.
        if s == t and num > tx:
            # On mémorise la force de cet atout et l'indice du joueur.
            tx, w = num, i
        # Si aucun atout n'a encore été joué (tx == -1), on regarde les cartes de la couleur demandée.
        elif tx == -1 and s == l and num > mx:
            # On mémorise la force et l'indice du joueur pour la carte la plus forte dans la couleur demandée.
            mx, w = num, i
    # On retourne l'indice du joueur gagnant le pli.
    return w

# Boucle principale exécutée indéfiniment (while 1 signifie une boucle qui s'arrête seulement avec un break).
while 1:
    # On lit une ligne depuis l'entrée utilisateur, censée correspondre à la couleur d'atout ou à un indicateur d'arrêt.
    t = raw_input()
    # Si l'utilisateur entre "#" cela signifie que le programme doit s'arrêter.
    if t == "#":
        break
    # On lit ensuite 4 lignes correspondant aux mains respectives des 4 joueurs.
    # raw_input().split() découpe la ligne en une liste de mots (cartes), pour chaque main.
    hands = [raw_input().split() for i in xrange(4)]
    # zip(hands[0], hands[1], hands[2], hands[3]) permet de regrouper les cartes jouées dans l'ordre des plis :
    # par exemple, la 1ère liste contiendra la 1re carte de chaque joueur, la 2e liste la 2e carte, etc., simulant le déroulement des plis.
    hands = zip(hands[0], hands[1], hands[2], hands[3])
    # led garde trace du joueur qui commence le pli (au début, joueur 0).
    led = 0
    # win : tableau pour compter les plis gagnés par Nord-Sud (indice 0) et Est-Ouest (indice 1).
    win = [0] * 2
    # On parcourt tous les plis (il y a 13 plis car chaque joueur a 13 cartes au bridge).
    for hand in hands:
        # On détermine le gagnant du pli actuel. judge() retourne l'indice du joueur vainqueur du pli.
        led = judge(hand, led)
        # On incrémente le compteur du camp (Nord-Sud : joueurs 0 et 2 ; Est-Ouest : joueurs 1 et 3).
        win[led % 2] += 1
    # En fin de donne, si Nord-Sud a gagné plus de plis, on affiche leur nom suivi du nombre de plis gagnés au-dessus de la moyenne (6).
    if win[0] > win[1]:
        print "NS", win[0] - 6
    # Sinon, on affiche Est-Ouest et leur nombre de plis au-dessus de 6.
    else:
        print "EW", win[1] - 6