from bisect import bisect_left as bl  # Importation de la fonction bisect_left depuis le module bisect, renommée en 'bl' pour plus de concision. Cette fonction permet de trouver la position d'insertion dans une liste triée.

def main():
    # Lecture d'une ligne d'entrée constituée de deux entiers séparés par un espace.
    # map applique la fonction int à chaque élément résultant du split, produisant deux entiers.
    n, c = map(int, input().split())  
    
    # Initialisation de la liste 'ranking' avec n éléments.
    # Chaque élément est un tuple (0, i) où 0 est un score initial et i l'identifiant de l'élément.
    ranking = [(0, i) for i in range(n)]  
    
    # Initialisation de la liste 'points' de taille n, remplie de zéros.
    # Elle garde en mémoire les points courants de chaque élément identifié par son index.
    points = [0 for _ in range(n)]  
    
    # Boucle sur le nombre total d'opérations ou commandes 'c'.
    for _ in range(c):
        # Lecture d'une ligne de commande, segmentation par espace pour obtenir une liste de chaînes.
        com = input().split()
        
        # Vérification du premier élément de la commande pour déterminer le type d'opération.
        if com[0] == "1":   # Si la commande commence par '1', il s'agit d'une requête d'affichage.
            # Conversion du second élément en entier moins un pour obtenir l'index 0-based.
            m = int(com[1]) - 1  
            # Affichage de deux valeurs séparées par un espace:
            # - ranking[m][-1] fait référence au second élément du tuple dans ranking à l'index m,
            #   qui correspond à l'identifiant i. On ajoute 1 pour revenir à une numérotation 1-based.
            # - -ranking[m][0] correspond au score inversé (initialement stocké négatif),
            #   on le multiplie par -1 pour afficher la valeur positive des points.
            print(ranking[m][-1] + 1, -ranking[m][0])
            
        else:
            # Pour les autres commandes (différentes de '1'), normalement '2' ici,
            # on récupère les deux entiers suivants t et p représentant un identifiant et un nombre de points.
            t, p = map(int, com[1:])
            
            # Passage à un index 0-based pour manipuler les listes.
            t -= 1  
            
            # Récupération du nombre de points actuel pour l'élément t.
            point = points[t]
            
            # Recherche dans la liste 'ranking' de la position d'insertion de (point, t).
            # Cette recherche est nécessaire pour localiser précisément où se trouve cet élément dans cette liste triée.
            index = bl(ranking, (point, t))  
            
            # Suppression de l'élément à l'index trouvé dans la liste 'ranking' car on va modifier ses points.
            ranking.pop(index)
            
            # Calcul du nouveau nombre de points après soustraction de p.
            new_point = point - p  
            
            # Recherche de la nouvelle position d'insertion dans la liste triée pour (new_point, t).
            new_index = bl(ranking, (new_point, t))  
            
            # Insertion du tuple mis à jour avec le nouveau score à la position correcte.
            ranking.insert(new_index, (new_point, t))  
            
            # Mise à jour de la liste 'points' pour refléter la modification.
            points[t] = new_point  

# Appel de la fonction principale pour lancer le programme.
main()