from collections import defaultdict  # Importe le module collections et la classe defaultdict, utile pour créer des dictionnaires avec une valeur par défaut
import sys  # Importe le module sys pour accéder à certaines fonctions du système

sys.setrecursionlimit(10 ** 6)  # Définit la limite maximale de récursion pour éviter l'erreur de dépassement de la pile lors de récursions profondes

# Définition d'une fonction lambda appelée int1, qui prend un argument x, convertit x en entier et soustrait 1
# Cela est utile lorsque les indices dans les entrées sont en base 1, mais qu'on veut travailler en base 0
int1 = lambda x: int(x) - 1

# Définition d'une fonction lambda appelée p2D, utilisée pour afficher les éléments d'une liste (ou matrice) ligne par ligne
p2D = lambda x: print(*x, sep="\n")

def main():  # Début de la fonction principale du programme

    def k_fix_way(com_n, com_r):  # Fonction pour calculer la manière de fixer k éléments parmi n, utilisant des mémos pour optimiser
        # Vérifie si la valeur est déjà calculée et enregistrée dans le dictionnaire kmemo
        if (com_n, com_r) in kmemo:
            return kmemo[(com_n, com_r)]
        # Calcule le nombre de façons de fixer 'com_r' éléments parmi 'com_n'
        # Utilise les valeurs pré-calculées de factorielle et leur inverse modulaire
        # Utilise la formule de combinaison modulaire (les détails mathématiques sont dans la formule)
        res = kmemo[(com_n, com_r)] = fac[com_n] * inv[com_n - com_r] * fac[com_n] * inv[com_r] * inv[com_n - com_r] % md
        return res  # Retourne le résultat calculé (ou mému-misé)

    kmemo = {}  # Crée un dictionnaire vide nommé kmemo, qui servira à mémoriser les résultats de k_fix_way pour accélérer les calculs

    def centroid(u=0, pu=-1):  # Fonction récursive pour trouver le(s) centre(s) de gravité (centroïdes) de l'arbre
        res = []  # Liste qui servira à stocker les centroïdes trouvés
        is_centroid = True  # Booléen supposant par défaut que le noeud courant est un centroïde
        u_nodes = 1  # Nombre de noeuds dans le sous-arbre courant, initialisé à 1 pour le noeud courant
        for cu in to[u]:  # Parcourt tous les enfants/cu (child u) de u dans la liste d'adjacence to
            if cu == pu: continue  # Ignore le parent pour éviter de revenir en arrière
            res += centroid(cu, u)  # Récursion pour explorer les descendants, et ajoute les centroïdes trouvés
            cu_nodes = n_nodes[cu]  # Nombre de noeuds dans le sous-arbre de cu
            if cu_nodes > n / 2: is_centroid = False  # Si un sous-arbre est trop grand, alors u ne peut pas être centroïde
            u_nodes += cu_nodes  # Ajoute les noeuds du sous-arbre à u_nodes
        n_nodes[u] = u_nodes  # Stocke le nombre de noeuds du sous-arbre de u dans le tableau n_nodes
        if n - u_nodes > n / 2: is_centroid = False  # Si le reste de l'arbre (hors u) est trop grand, u n'est pas centroïde
        if is_centroid: res.append(u)  # Si u est centroïde, on l'ajoute à la liste résultat
        return res  # Retourne la liste des centroïdes trouvés dans ce parcours

    md = 10 ** 9 + 7  # Modulo souvent utilisé dans les problèmes de combinatoire pour éviter les dépassements (grand nombre premier)
    to = defaultdict(list)  # Crée un dictionnaire qui va servir de liste d'adjacence pour l'arbre, avec une liste par défaut pour chaque clé (noeud)
    n = int(input())  # Lit un entier depuis l'entrée standard ; il s'agit du nombre de noeuds de l'arbre
    for _ in range(n - 1):  # Pour chaque arête de l'arbre (il y a n-1 arêtes dans un arbre avec n noeuds)
        u, v = map(int, input().split())  # Lit deux entiers (les noeuds de l'arête)
        u, v = u - 1, v - 1  # Transforme les indices pour travailler en base 0, plus naturel en Python
        to[u].append(v)  # Ajoute v comme voisin de u dans la liste d'adjacence to
        to[v].append(u)  # Ajoute u comme voisin de v dans to (car l'arbre est non orienté, donc relation bilatérale)
    # Préparation d'un tableau pour stocker le nombre de noeuds dans chaque sous-arbre, initialisé à 0
    n_nodes = [0] * n
    cc = centroid()  # Appel de la fonction centroid pour déterminer le(s) centroïde(s) de l'arbre, retourne une liste de noeuds centroïdes
    # Calcul des factorielles et de leurs inverses modulo md, afin de pouvoir calculer rapidement les combinaisons
    n_max = n  # Le nombre maximal pour lequel on aura besoin de calculer une factorielle
    fac = [1]  # Initialisation de la liste des factorielles; fac[0] = 1
    inv = [1] * (n_max + 1)  # Initialisation de la liste des inverses modulaires ; taille n_max+1, initialisée à 1 partout
    k_fac_inv = 1  # Variable pour stocker la factorielle courante sous forme d'inverse
    for i in range(1, n_max + 1):  # Pour tous les entiers de 1 à n inclus
        k_fac_inv = k_fac_inv * i % md  # Calcule la factorielle i modulo md chaque fois
        fac.append(k_fac_inv)  # Ajoute la valeur calculée à la liste fac
    k_fac_inv = pow(k_fac_inv, md - 2, md)  # Calcule l'inverse modulaire de la dernière factorielle (grâce au théorème de Fermat : a^(p-2) mod p pour p premier)
    for i in range(n_max, 1, -1):  # Remplit la liste inv à l'envers (de n à 2)
        inv[i] = k_fac_inv  # Associe à chaque case la valeur de l'inverse courant
        k_fac_inv = k_fac_inv * i % md  # Met à jour l'inverse pour le tour suivant (multiplication cumulative)
    # Si le centroïde se trouve être deux noeuds (cas où l'arbre est parfaitement équilibré et "coupé" en deux)
    if len(cc) == 2:
        print(pow(fac[n // 2], 2, md))  # Alors le résultat est juste le carré de la factorielle de n//2 modulo md (explication mathématique liée à la combinatoire de découpe équilibrée)
        exit()  # On termine immédiatement le programme
    # S'il n'y a qu'un centroïde (cas le plus courant)
    # On va alors s'intéresser à la taille des sous-arbres du centroïde
    subtree_node_n = []  # Liste pour stocker la taille de chaque sous-arbre du centroïde
    c = cc[0]  # Il n'y a qu'un centroïde: on le prend (premier élément)
    for u in to[c]:  # On regarde tous les voisins du centroïde
        u_nodes = n_nodes[u]  # On prend le nombre de noeuds dans le sous-arbre de ce voisin
        if u_nodes > n / 2: continue  # Si le sous-arbre est trop grand ce n'est pas un "vrai" sous-arbre du centroïde; on saute
        subtree_node_n.append(u_nodes)  # Sinon on ajoute cette taille à la liste des sous-arbres
    if c != 0: subtree_node_n.append(n - n_nodes[c])  # Si le centroïde n'est pas la racine, on ajoute le complément (noeuds non visités du reste)
    # dp[i][j] décrira, en termes combinatoires, le nombre de façons de fixer j éléments parmi les i premiers sous-arbres examinés
    dp = [0] * n  # Tableau dp de taille n, initialisé à 0 partout
    dp[0] = 1  # Il y a toujours une seule manière de ne rien choisir (cas de base)
    for i, node_n in enumerate(subtree_node_n):  # On parcourt chaque sous-arbre avec son nombre de noeuds
        for j in range(n - 1, -1, -1):  # Pour chaque nombre possible de noeuds déjà fixés (à rebours pour éviter d'écraser des valeurs)
            pre = dp[j]  # On garde temporairement la valeur de dp[j]
            if pre == 0: continue  # Si aucune façon pour ce nombre, on continue
            for k in range(node_n, 0, -1):  # Pour chaque nombre k de nouveaux noeuds qu'on peut fixer dans ce sous-arbre
                dp[j + k] = (dp[j + k] + pre * k_fix_way(node_n, k)) % md  # Mise à jour du dp pour j+k, ajoutant le nombre de façons d'en choisir k dans le sous-arbre, modulo md
    # Calcul final utilisant le principe d'inclusion-exclusion (alternance de signes)
    ans = 0  # Initialisation du résultat total à 0
    coff = 1  # Variable qui va alterner entre +1 et -1 pour réaliser le principe d'inclusion-exclusion
    for j in range(n):  # Pour chaque nombre possible de noeuds fixés
        ans = (ans + coff * dp[j] * fac[n - j]) % md  # Ajoute/retire la contribution des arrangements possibles selon le principe d'inclusion-exclusion
        coff *= -1  # Change le signe (pour alterner + et -)
    print(ans)  # Affiche la réponse finale

main()  # Exécute la fonction principale