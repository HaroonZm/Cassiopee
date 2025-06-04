from bisect import bisect_left as bl  # Importe la fonction bisect_left du module bisect et la renomme en 'bl' pour simplifier son utilisation dans le code

def main():
    # Lit la première ligne de l'entrée, la divise (split) en deux parties, puis les convertit en entiers avec map(int, ...)
    # Cette ligne permet d'obtenir le nombre de joueurs 'n' et le nombre de commandes 'c'
    n, c = map(int, input().split())
    
    # Initialise une liste appelée 'ranking'. 
    # Chaque élément dans cette liste est un tuple de deux éléments :
    # (score_du_joueur, indice_du_joueur)
    # Ici, tous les scores sont initialisés à 0, et l'indice varie de 0 à n-1
    # Cela permet de garder une trace de la position de chaque joueur et de leur score (pour trier/ranger).
    ranking = [(0, i) for i in range(n)]
    
    # Crée une liste 'points' qui contient le score actuel de chaque joueur. 
    # Tous les scores des joueurs sont initialement à 0.
    # L'indice dans la liste 'points' correspond à l'indice du joueur.
    points = [0 for _ in range(n)]
    
    # Boucle qui va traiter chaque commande. Il y a exactement 'c' commandes à lire, donc '_ in range(c)'
    for _ in range(c):
        # Lit la commande saisie par l'utilisateur. La commande est une chaîne de caractères comprenant soit :
        # - "1 X" pour demander la position actuelle du joueur X
        # - "2 T P" pour diminuer le score du joueur T de P points 
        # La ligne est divisée selon les espaces, chaque partie de la commande sera un élément de la liste 'com'
        com = input().split()
        
        # Si la première partie de la commande (com[0]) est "1", il s'agit d'une requête de type 1
        if com[0] == "1":
            # Récupère l'indice du joueur demandé (X), en le convertissant de chaîne en entier puis en utilisant une indexation de base 0
            m = int(com[1]) - 1  # On soustrait 1 car la numérotation des joueurs commence à 1 dans l'entrée utilisateur, 
                                 # mais les indices en Python commencent à 0
            # Affiche la position du joueur m dans la liste 'ranking'
            # ranking[m][-1] récupère le dernier élément du tuple à la position m de la liste (c'est-à-dire l'indice du joueur)
            # On ajoute 1 pour correspondre à l'indexation utilisateur (débutant à 1)
            # -ranking[m][0] donne l'opposé du score (puisque les scores sont stockés négativement pour tri croissant)
            print(ranking[m][-1] + 1, -ranking[m][0])
        else:
            # S'il ne s'agit pas de la commande "1", il s'agit forcément de la commande "2"
            # Extrait les valeurs de t (indice joueur à modifier) et p (nombre de points à enlever),
            # Après avoir converti chaque élément de la liste à partir de com[1:](= 2e et 3e éléments) en entiers 
            t, p = map(int, com[1:])
            t -= 1  # Convertit 't' de la base utilisateur (débutant à 1) à la base Python (débutant à 0)
            
            # Récupère le score courant du joueur 't'
            point = points[t]
            
            # Trouve l'indice dans la liste 'ranking' où se trouve le joueur 't' avec son score actuel 
            # Utilise la recherche dichotomique via 'bl', ce qui est plus rapide qu'une recherche linéaire
            # L'ordre de rangement dépend du tuple (point, t) : le score, puis l'indice du joueur
            index = bl(ranking, (point, t))
            
            # Retire l'élément correspondant à (point, t) de la liste 'ranking' parce que le score va changer
            ranking.pop(index)
            
            # Calcule le nouveau score du joueur 't' après avoir soustrait 'p'
            new_point = point - p
            
            # Trouve le nouvel emplacement où insérer le tuple mis à jour dans la liste 'ranking'
            # Ceci garde la liste 'ranking' triée, ce qui facilitera et accélérera les futures recherches et insertions
            new_index = bl(ranking, (new_point, t))
            
            # Insère le nouveau tuple (new_point, t) à la bonne position dans la liste 'ranking'
            ranking.insert(new_index, (new_point, t))
            
            # Met à jour aussi la liste 'points' pour refléter le nouveau score du joueur 't'
            points[t] = new_point

# Appelle la fonction principale pour démarrer le programme
main()