# La clé du problème est de modéliser le déroulement du jeu comme une série d'attaques alternées entre les deux équipes,
# où chaque membre de l'équipe en attaque inflige exactement une réduction d'1 point de santé à un membre de l'équipe adverse.
# Chaque membre a initialement 2 points de vie.
#
# Le jeu se déroule en tours alternés:
# - Tour UKU : Chaque membre de l'équipe UKU attaque une fois.
# - Tour Ushi: Chaque membre de l'équipe Ushi attaque une fois.
#
# À l'issue de chaque tour, si l'équipe attaquée n'a plus de membres (vie 0), le jeu s'arrête.
# Sinon, on incrémente le score commun de 1 et on passe au tour suivant.
#
# Notre objectif est de trouver le score final minimal possible.
#
# Analyse :
# - Un joueur peut être attaqué plusieurs fois dans un tour.
# - Pour faire sortir au minimum des joueurs, il faut "concentrer" les attaques,
#   car chaque joueur a 2 PV, donc il faut 2 attaques pour le mettre hors-jeu.
#
# Le jeu peut être vu comme une alternance de soustraction de multiples de N et de M.
# On peut définir récursivement la fonction f(N, M) = nombre minimal de tours supplémentaires
# (à partir de l'état initial où chaque joueur a 2 PV) avant que l'un des deux groupes soit éliminé.
#
# Si N > M: UKU attaque d'abord, et par "nagé", on pourra attaquer M joueurs de Ushi 1 fois pour réduire leurs PV,
# sachant que chaque joueur est retiré dès 2 attaques reçues.
# En pratique, ce processus correspond à l'algorithme d'Euclide modifié:
# Le nombre minimal de tours correspond à la somme des quotients de la division euclidienne N // M, adjoints de manière récursive.
#
# D'où la solution:
# On calcule le quotient q = N // M,
# Le reste r = N % M,
# Le score minimal = q + f(M, r), avec f(0) = 0.

def uu_game_score(N: int, M: int) -> int:
    # Fonction récursive pour calculer le score minimal,
    # inspirée de l'algorithme d'Euclide tout en additionnant les quotients
    # Chaque quotient représente le nombre de "cycles" complets effectués avant de passer à l'autre équipe
    if M == 0:
        # Si une équipe est vide, le jeu s'arrête, score 0
        return 0
    q = N // M
    r = N % M
    # On échappe de q tours "complètes" + récursion sur (M, r)
    return q + uu_game_score(M, r)

def main():
    N, M = map(int, input().split())
    # Le score minimal est calculé en partant du plus grand vers le plus petit
    # car le jeu commence avec UKU attaquant/ushi defenseur.
    # On calcule toujours avec le plus grand en premier argument:
    if N < M:
        N, M = M, N
    # Le score obtenu ici correspond au nombre total de "tours - 1"
    # Comme le problème demande le score final, on en soustrait 1 car la première étape
    # ne fait pas augmenter le score.
    score = uu_game_score(N, M) - 1
    # score minimal >= 0 car la soustraction peut sortir -1 si N==M==1
    if score < 0:
        score = 0
    print(score)

if __name__ == "__main__":
    main()