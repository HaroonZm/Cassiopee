import sys  # Permet d'accéder aux fonctionnalités liées au système, comme l'entrée standard
from collections import defaultdict  # Importe un type de dictionnaire qui retourne une valeur par défaut pour les clés manquantes

def main():
    # Redéfinit input pour lire rapidement les lignes depuis l'entrée standard
    input = sys.stdin.readline
    # Lit la première ligne, la découpe en éléments, les convertit en entiers, puis les attribue à n, m, et k
    n, m, k = map(int, input().split())  # n = nombre total d'éléments, m = taille du tableau d, k = nombre de lignes dans A
    
    # Lit la ligne suivante, découpe en entiers et crée la liste d
    d = list(map(int, input().split()))  # d contient m entiers
    
    # Crée une liste l de taille n, remplie de -1. l sera utilisé pour enregistrer les indices où les éléments d[i] apparaissent
    l = [-1] * n
    for i in range(m):  # On parcourt chaque index de 0 à m-1
        # d[i] - 1 : conversion à partir d'un indice basé sur 1 vers un indice basé sur 0
        # l[d[i] - 1] = i : enregistre l'indice i pour la valeur d[i] dans l
        l[d[i]-1] = i
    
    # Crée une liste 2D A de taille n x k, chaque ligne étant lue de l'entrée standard et convertie en entiers
    A = [list(map(int, input().split())) for _ in range(n)]  # A est une matrice à n lignes
    
    # Crée la liste "a", où chaque élément correspond à une liste calculée pour chaque j parmi k
    # Structure doublement imbriquée : sur chaque j (0,...,k-1), pour chaque valeur i de d
    # Chaque élément a[j][d_index] vaut l'indice associé à la valeur dans l, ou None si elle vaut -1
    a = [
        [l[A[i-1][j] - 1] if l[A[i-1][j] - 1] != -1 else None for i in d]
        for j in range(k)
    ]
    
    # Initialise la liste c qui va contenir des scores, de taille 2 puissance m (tous les masques binaires possibles sur m bits)
    # Tous les éléments sont initialisés à -1, indiquant que ce masque n'a pas encore été atteint/traité
    c = [-1] * (1 << m)  # (1 << m) signifie 2 puissance m
    
    # Attribue la valeur 0 au dernier élément de c, c’est-à-dire pour le masque complet (tous les bits à 1)
    c[(1 << m) - 1] = 0
    
    # Construit une liste D où D[i] est 2 puissance i, c'est-à-dire un masque de bit avec juste le ième bit à 1
    # D[0] = 1 (0001), D[1] = 2 (0010), etc. Le dernier élément (m+1 -ème) n'est pas utilisé
    D = [1 << i for i in range(m+1)]
    
    # Initialise la liste x. Ici on lui met une taille m et on la remplit avec -1. Elle sera plus tard utilisée comme liste temporaire
    x = [-1] * m
    
    # q est un dictionnaire spécial (defaultdict) qui retourne 0 pour toute clé non encore créée
    q = defaultdict(int)
    
    # Range est utilisé comme un alias pour la séquence d’indices de 0 à m-1 (à réutiliser pour plus de clarté)
    Range = range(m)
    
    # K fait office d’index de lecture dans la "queue" q, tandis que R servira d’index d’écriture/incrément
    K = 0
    # On établit une première entrée q[0] = -1. Dans la suite, q sera utilisé pour stocker les masques atteints à chaque étape
    q[0] = -1
    R = 1  # C’est le compteur pour la prochaine position libre dans q
    
    # On démarre une boucle sans condition de sortie initiale : elle ne s’arrête qu’avec un return explicite
    while 1:
        # Récupère le masque courant à l’indice K dans q. C’est l’état à traiter
        mask = q[K]
        K += 1  # Incrémente K pour traiter les prochains masques à la prochaine itération
        
        # Calcul du score pour ce masque : on ajoute 1 au score associé au masque courant
        # (Le +1 reflète le passage à une nouvelle "étape"/niveau dans cette recherche)
        score = c[mask] + 1
        
        # x devient la liste des indices i (dans Range donc 0..m-1) tels que le bit i de mask est activé (c’est-à-dire mask & D[i] != 0)
        x = [i for i in Range if mask & D[i]]
        
        # Parcourt chaque ai dans la liste a (pour chaque "ligne" k)
        for ai in a:
            tmp = 0  # Commence avec aucun bit activé, c.-à-d. masque nul
            for j in x:  # Pour chaque indice où le bit dans mask est à 1
                aji = ai[j]  # aji est la valeur en position j dans ai
                # Vérifie si aji n'est pas None (il y a donc un indice valable à activer dans le masque)
                if aji != None:
                    # Active le bit d’indice aji dans tmp en utilisant le OU binaire
                    tmp |= D[aji]
            # Maintenant, tmp est un nouveau masque formé à partir d’ai et de x (les positions actives)
            # Si ce masque n’a pas encore de score associé (c[tmp] == -1), il est découvert pour la première fois
            if c[tmp] == -1:
                c[tmp] = score  # Associe le score à ce masque
                q[R] = tmp      # Place tmp dans la file q, position R
                R += 1          # Avance à la prochaine position
                # Si tmp == 0, alors ce masque ne contient aucun bit activé (tous désactivés), c’est le but final
                if tmp == 0:
                    print(score)  # Affiche le score minimum atteint jusqu’ici, puis
                    return        # Arrête immédiatement le programme

# Exécute la fonction main uniquement si ce script est exécuté directement (et pas importé comme module)
if __name__ == "__main__":
    main()