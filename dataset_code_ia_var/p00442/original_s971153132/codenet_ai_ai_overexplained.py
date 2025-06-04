import sys  # Importe le module sys, qui fournit des fonctions et des variables utilisées pour manipuler différentes parties de l'environnement d'exécution Python.

sys.setrecursionlimit(100000)  # Modifie la limite maximale de récursion. Cela évite une erreur lors de l'utilisation de la récursion profonde, en fixant la limite très haute.

def main():  # Définition de la fonction principale qui contient toute la logique du programme.
    V = int(input())  # Lit un entier à partir de l'entrée utilisateur, correspondant au nombre de sommets dans un graphe.
    E = int(input())  # Lit un autre entier de l'entrée utilisateur, représentant le nombre d'arêtes dans le graphe.
    
    L = []  # Crée une liste vide nommée L, qui va contenir l'ordre des sommets après un parcours particulier (ordre topologique).
    app = L.append  # Crée un raccourci vers la fonction d'ajout d'élément à la liste 'L' pour des appels plus rapides et du code plus compact.
    
    visited = [0 for i in range(V)]  # Crée une liste contenant V zéros, initialisant tous les sommets comme 'non visités' (0 : non visité, 1 : visité).
    edges = [[] for i in range(V)]  # Crée une liste contenant V sous-listes vides. Chaque sous-liste représentera la liste des voisins accessibles depuis ce sommet.
    
    def visit(x):  # Fonction récursive dédiée au parcours en profondeur (Depth-First Search, DFS) du graphe à partir du sommet d'indice 'x'.
        if not visited[x]:  # Vérifie si le sommet 'x' n'a pas encore été visité (si sa valeur dans 'visited' est 0).
            visited[x] = 1  # Indique que le sommet a maintenant été visité, en remplaçant 0 par 1 à l'indice 'x' dans la liste 'visited'.
            for e in edges[x]:  # Pour chaque voisin 'e' accessible directement depuis le sommet 'x' (pour chaque arête sortante).
                visit(e)  # Appelle récursivement la fonction de visite pour le voisin 'e', continuant ainsi l'exploration en profondeur.
            app(x)  # Ajoute le sommet 'x' à la fin de la liste 'L'. Cela se fait APRÈS avoir visité tous ses voisins (post-traitement).

    # Cette boucle traite la lecture et le stockage des arêtes du graphe.
    for i in range(E):  # Répète le processus E fois, une fois pour chaque arête à lire.
        s, t = map(int, input().split())  # Lit une ligne de l'entrée, la découpe en deux entiers 's' et 't'. Ceux-ci représentent une arête allant de 's' à 't'.
        edges[s - 1].append(t - 1)  # Convertit chaque sommet de base 1 à base 0 (indices Python) et ajoute le sommet 't-1' comme voisin sortant de 's-1'.
    
    # Cette boucle lance le parcours en profondeur pour chaque sommet.
    for i in range(V):  # Parcourt tous les indices de 0 à V-1, c'est-à-dire tous les sommets du graphe.
        if not visited[i]:  # Si le sommet i n'a pas encore été visité,
            visit(i)  # Appelle la fonction visit pour ce sommet, commençant ainsi son parcours en profondeur.
    
    L.reverse()  # Inverse la liste 'L' pour obtenir l'ordre topologique correct. (DFS post-ordre inversé == topologique)
    
    flag = 0  # Initialise une variable 'flag' à 0. Cette variable servira à indiquer si l'ordre topologique forme une chaîne d'arêtes ("path").
    
    # Cette boucle imprime l'ordre topologique et vérifie la "chaînage" de l'ordre.
    for i in range(V):  # Parcourt tous les indices de 0 à V-1 dans l'ordre topologique enregistré dans 'L'.
        print(L[i] + 1)  # Affiche l'indice du sommet augmenté de 1, pour rétablir le format d'origine (base 1) de l'entrée/sortie.
        # La condition suivante vérifie s'il existe un problème dans la succession des sommets dans l'ordre topologique.
        # Plus précisément, elle vérifie que, pour chaque sommet sauf le dernier, le sommet suivant dans l'ordre n'est pas accessible directement (n'est pas un voisin dans la liste des arêtes du sommet courant).
        if not flag and i < V - 1 and (L[i + 1] not in edges[L[i]]):  # Si 'flag' est encore à 0, si ce n'est pas le dernier sommet, et s'il n'existe pas d'arête directe du sommet courant au suivant,
            flag = 1  # On fixe 'flag' à 1 pour signaler que la chaîne peut "sauter" un lien direct, ce qui veut dire que ce n'est pas un chemin strict, mais juste un ordre topologique.

    print(flag)  # Affiche la valeur finale de 'flag', indiquant si l'ordre topologique est un chemin (0) ou non (1).
    
main()  # Appelle la fonction principale lorsque le script est exécuté, pour exécuter toute la logique du programme.