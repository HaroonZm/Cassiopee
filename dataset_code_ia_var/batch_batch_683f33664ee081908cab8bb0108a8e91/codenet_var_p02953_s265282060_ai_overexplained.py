import sys  # Le module sys permet d'interagir directement avec certaines variables et fonctions propres à l'interpréteur Python

sys.setrecursionlimit(10 ** 7)  # Cette ligne augmente la limite de récursion de l'interpréteur Python. 
# Par défaut, Python arrête un programme lorsqu'il dépasse environ 1000 appels récursifs pour éviter les débordements de pile (stack overflow).
# Ici, on élève cette limite à 10 millions (10^7), ce qui permet des appels récursifs très profonds. 
# C'est utile pour certains algorithmes nécessitant beaucoup de récursion, comme ceux traitant de grands arbres ou graphes.

# from collections import deque  # Cette ligne est commentée et donc inutilisée. deque est une structure de données "double-ended queue" très utile pour ajouter/retirer des éléments aux deux extrémités de façon efficace.
from collections import deque  # Ici, on importe explicitement deque pour une utilisation ultérieure. Mais dans ce code, deque n'est finalement pas utilisé.

# import bisect  # Le module bisect permet des opérations efficaces d'insertion/positionnement dans des listes triées, mais ici il est commenté.
# import numpy as np  # Numpy est un module utilisé pour le calcul scientifique sur des tableaux, mais il est commenté donc non utilisé ici.
# from collections import deque  # Commenté, doublon avec la ligne plus haut.
# map(int, sys.stdin.read().split())  # Cette ligne seule ne fait rien, elle illustre peut-être une manière commune de lire des entiers depuis l'entrée standard.

import itertools  # Le module itertools contient divers outils pour manipuler des itérateurs (permutations, produits cartésiens, etc.), mais il n'est pas utilisé dans ce script.
import heapq  # heapq donne accès à la structure de données "tas binaire" (heap) pour créer des files de priorité efficaces, mais ici aussi il n'est pas utilisé.

def input():
    """
    Fonction personnalisée remplaçant la fonction input() standard de Python.
    Elle lit une ligne depuis l'entrée standard (typiquement l'utilisateur ou un fichier),
    supprime le caractère de fin de ligne (retour chariot), puis renvoie la ligne.
    Ceci est particulièrement utile pour éviter d'avoir des retours à la ligne superflus qui viennent souvent de sys.stdin.readline().
    """
    return sys.stdin.readline().rstrip()  # readline() lit une ligne, rstrip() supprime les espaces en fin de chaîne (notamment '\n').

def main():
    """
    Fonction principale du programme. Elle exécute la logique principale, souvent appelée point d'entrée du script.
    """

    N = int(input())  # Lecture d'un entier N qui représente généralement le nombre d'éléments ou la taille d'une séquence.
    # On utilise la fonction input() définie précédemment pour obtenir la ligne de l'entrée, puis int() pour convertir la chaîne en entier.

    H = list(map(int, input().split()))  
    # Lecture d'une seconde ligne de l'entrée, censée contenir N nombres entiers séparés par des espaces.
    # On appelle input() pour la lire, .split() pour séparer la ligne sur les espaces, 
    # map(int, ...) pour convertir chaque élément (qui est à ce stade une chaîne) en entier, 
    # et enfin list() pour obtenir une liste d'entiers.
    
    off = 0  # Initialisation d'une variable appelée 'off' à 0. 
    # Cette variable agit ici comme une sorte de drapeau ou d'état, elle sera utilisée pour ajuster certains calculs dans la boucle suivante.
    
    flag = 1  # Initialisation d'une seconde variable appelée 'flag' à 1.
    # Cependant, cette variable n'est jamais utilisée dans la suite du code et peut donc être supprimée sans changer le comportement du programme.

    for i in range(N-1, 0, -1):
        # Boucle for qui démarre à l'indice N-1 (dernier indice valide de la liste H) et décrémente jusqu'à 1 (puisque la borne inférieure 0 n'est pas incluse).
        # À chaque itération, i représente l'indice courant dans la liste H. On traite donc la liste du dernier élément vers le premier.
        
        if H[i] - off >= H[i-1]:
            # Teste si la hauteur du bloc actuel (H[i]) diminuée de la valeur de off (correction éventuelle) est supérieure ou égale à la hauteur du bloc précédent (H[i-1]).
            # Si oui, on peut "descendre" un bloc sans problème ou sans nécessiter de modification. On réinitialise alors off à 0.
            off = 0  # On remet la modification/correction à 0 pour la prochaine itération.
            continue  # continue fait passer à la prochaine itération de la boucle, évitant d'exécuter le reste du code dans cette boucle.

        elif H[i] - off + 1 == H[i-1]:
            # Ici, on vérifie si, en augmentant d'une unité la hauteur actuelle (avec la correction 'off'),
            # on pourrait égaler la hauteur du bloc précédent. Cela signifie qu'on est autorisé à abaisser une fois la hauteur du bloc précédent de 1.
            off = 1  # On indique qu'une modification/correction a été faite pour la prochaine itération.

        else:
            # Si aucune des deux conditions précédentes n'est remplie, alors la séquence ne respecte pas la contrainte exigée.
            # Dans le contexte de ce problème, ça signifie que la transformation des hauteurs n'est pas possible.
            print("No")  # On affiche 'No' pour indiquer l'impossibilité.
            exit()      # On arrête le programme immédiatement.

    # Si la boucle n'a jamais rencontré le cas d'échec, c'est que la transformation est réalisable.
    print("Yes")  # On affiche 'Yes' pour indiquer le succès.

if __name__ == "__main__":  # Cette condition spéciale permet de vérifier si le script est exécuté directement (pas importé comme module).
    main()  # Si c'est le cas, on exécute la fonction principale main().