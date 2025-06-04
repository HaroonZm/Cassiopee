def main():
    # Importation du module sys pour récupérer l'entrée standard
    import sys
    # Importation des fonctions heappop et heappush pour manipuler la file de priorité (heap) efficacement
    from heapq import heappop, heappush

    # Définition d'une fonction d'input pour lire une ligne de l'entrée standard et enlever les retours à la ligne
    def input():
        # sys.stdin.readline() lit une ligne de l'entrée standard, rstrip() enlève les caractères de retour à la ligne
        return sys.stdin.readline().rstrip()

    # Définition de la fonction de Dijkstra pour calculer les plus courts chemins à partir d'un sommet donné
    def dijkstra(s):
        # Définition d'une grande valeur pour représenter "l'infini" (car le vrai infini ne peut pas être utilisé ici directement pour des comparaisons d'entiers)
        inf = 10**6  # 1 000 000
        # Création d'une liste de distances initialisées à "l'infini" pour chaque sommet (ici, il y a 10 sommets numérotés de 0 à 9)
        dist = [inf] * 10
        # Initialisation de la distance du sommet source 's' à 0, car la distance de soi à soi est 0
        dist[1] = 0  # Le sommet de départ est toujours 1
        # Création d'une file de priorité pour sélectionner le prochain sommet à visiter. Elle stocke des tuples (coût actuel, numéro du sommet)
        que = [(0, 1)]  # On commence avec le sommet 1 et un coût de 0
        # Tant qu'il y a des sommets à traiter dans la file de priorité
        while que:
            # Retire et retourne l'élément avec le plus petit coût dans la file de priorité
            cost, node = heappop(que)
            # Si le coût actuel est supérieur à la distance connue, ce chemin n'est pas optimal, on ignore
            if cost > dist[node]:
                continue
            # Examine tous les voisins possibles du sommet actuel (il y en a 10, numérotés de 0 à 9)
            for i in range(10):
                # On ne se connecte pas à soi-même, donc on ignore si c'est le même sommet
                if i == node:
                    continue
                # Si la distance pour aller au voisin i via le sommet current node est plus courte,
                # alors on met à jour la distance et on ajoute ce sommet dans la file de priorité
                if dist[i] > dist[node] + g[i][node]:
                    dist[i] = dist[node] + g[i][node]
                    # On ajoute dans la file de priorité pour traiter plus tard ce sommet avec sa nouvelle distance
                    heappush(que, (dist[i], i))
        # On retourne la liste finale des distances minimales du sommet 's' vers tous les autres
        return dist

    # Lecture de la première ligne de l'entrée standard, contenant deux entiers séparés par un espace (hauteur et largeur d'une grille)
    h, w = map(int, input().split())
    # Création d'une matrice de 10 lignes initialement vide pour stocker les coûts de conversion entre chiffres (g sera une liste de listes)
    g = [[] for _ in range(10)]
    # Pour chaque chiffre de 0 à 9, on lit la ligne correspondante et on convertit chaque valeur en entier
    for i in range(10):
        g[i] = list(map(int, input().split()))  # Chaque ligne contient 10 entiers, ce qui donne une matrice 10x10

    # Importation de 'defaultdict' de la bibliothèque collections pour compter facilement les occurrences
    from collections import defaultdict
    # Création d'un dictionnaire qui compte les occurrences de chaque type de cellule (clé = type de cellule; valeur = nombre d'occurrences)
    c_lis = defaultdict(int)
    # Lecture des h lignes suivantes, chacune décrivant une ligne de la grille
    for i in range(h):
        # On lit une ligne, on la découpe par espaces, et on parcourt chaque élément
        for j in input().split():
            # Conversion de la valeur lue (de type chaîne) en entier
            tmp = int(j)
            # Si la valeur absolue de tmp n'est pas égale à 1, on compte cette valeur
            # (On ignore les cellules qui valent 1 ou -1 selon l'énoncé implicite)
            if abs(tmp) != 1:
                c_lis[tmp] += 1  # Incrémente le compteur pour cette valeur

    # On applique Dijkstra pour trouver le chemin minimal pour transformer chaque chiffre en 1 (en partant de 1)
    dist = dijkstra(1)
    # Initialisation du total de la réponse à 0 (c'est le coût total minimal requis)
    ans = 0
    # Pour chaque type de cellule (clé) qui doit être changée en 1, on multiplie le nombre de fois où il apparaît par le coût minimal du changement
    for key in c_lis:
        # On accumule (ajoute) dans la variable ans la somme des conversions nécessaires pour chaque chiffre/key
        ans += c_lis[key] * dist[key]
    # On affiche le résultat final
    print(ans)

# Ceci est l'entrée principale du programme : ce bloc s'exécutera seulement si ce fichier est exécuté directement,
# et non s'il est importé comme module dans un autre fichier
if __name__ == '__main__':
    main()