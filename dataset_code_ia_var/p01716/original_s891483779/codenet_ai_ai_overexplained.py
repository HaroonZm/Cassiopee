# Importation du module itertools, qui fournit des fonctions permettant de travailler avec des itérateurs de manière efficace.
from itertools import product

# Importation du module sys, qui nous permet de manipuler les flux d'entrée/sortie standards (stdin et stdout).
import sys

# Liaison rapide de la fonction readline à sys.stdin.readline, pour une lecture optimisée de l'entrée standard (plus rapide que input()).
readline = sys.stdin.readline
# Liaison rapide de la fonction write à sys.stdout.write, pour écrire rapidement sur la sortie standard.
write = sys.stdout.write

# Définition de la fonction principale qui encapsule tout le traitement du problème.
def solve():
    # Définition d'une constante MOD valant 10^9 + 7, un nombre premier utilisé pour prendre les résultats modulo ce nombre
    MOD = 10**9 + 7

    # Lecture de deux entiers séparés par un espace depuis l'entrée standard, puis conversion en entiers via map et unpacking.
    N, M = map(int, readline().split())

    # Lecture d'une chaîne depuis l'entrée standard, suppression des retours à la ligne inutiles en début et fin (strip()).
    S = readline().strip()

    # Création d'une liste de zéros de taille M, pour contenir ultérieurement certaines valeurs (ici U).
    U = [0]*M
    # Idem ci-dessus pour L.
    L = [0]*M

    # Création d'un dictionnaire 'mp', qui va servir à associer à chaque caractère/digit une valeur numérique unique.
    mp = {}

    # Boucle pour remplir le dictionnaire 'mp' avec les caractères-chiffres '0'-'9' associés à leur valeur entière.
    for i in range(10):
        mp[str(i)] = i

    # Boucle sur M lignes d'entrée, chacune définissant une substitution de lettres à des nombres.
    for i in range(M):
        # Lecture d'une ligne, séparation en deux parties. v est la lettre, u la chaîne numérique associée.
        v, u = readline().split()
        # Associe à la lettre v une valeur numérique unique dans mp (i+10 évite tout chevauchement avec les chiffres 0-9).
        mp[v] = i+10
        # Stocke la longueur de u dans L[i].
        L[i] = len(u)
        # Convertit u en entier et le stocke dans U[i].
        U[i] = int(u)

    # Définition d'une fonction locale 'root' pour trouver la racine d'un élément x dans une structure d'ensemble disjoint (union-find).
    def root(x):
        # Si la racine de x est x lui-même, c'est la racine.
        if prt[x] == x:
            return x
        # Sinon, compression de chemin : on remonte récursivement et on mémorise la racine.
        prt[x] = y = root(prt[x])
        return y

    # Définition d'une fonction locale 'unite' pour fusionner deux ensembles dans la structure union-find.
    def unite(x, y):
        # On récupère la racine de x (px) et de y (py).
        px = root(x)
        py = root(y)
        # On fait pointer le plus grand vers le plus petit pour garantir une profondeur minimale.
        if px < py:
            prt[py] = px
        else:
            prt[px] = py

    # Pour chaque caractère de la chaîne S, on le mappe via mp à son identifiant numérique, puis déballage sous forme de liste T.
    *T, = map(mp.__getitem__, S)

    # Initialisation de la variable qui va accumuler la réponse finale.
    ans = 0

    # Création d'un tuple t10 contenant dix valeurs 1. (Pas utile ici mais correspond sans doute à un pattern standard).
    t10 = (1,)*10

    # Boucle sur toutes les configurations de tailles possibles des substitutions, product([1,2], repeat=M) génère toutes les possibilités.
    for P in product([1, 2], repeat=M):
        # Variable booléenne pour vérifier la validité d'une configuration.
        ok = 1
        # Vérifie que la taille de chaque substitut n'excède pas sa longueur maximale autorisée
        for i in range(M):
            if P[i] > L[i]:
                ok = 0
                break
        # Si ce n'est pas valide, on saute cette configuration.
        if not ok:
            continue

        # Initialise la structure union-find : chaque élément pointe sur lui-même (pour 10 chiffres et 2*M supplémentaires pour les lettres).
        *prt, = range(10+M*2)

        # Initialisation de variables de boucle pour former des paires symétriques entre les extrémités gauche (l, p) et droite (r, q) de la chaîne.
        l = 0
        p = P[T[l]-10]-1 if T[l] >= 10 else 0 # Si T[l] est une lettre substituée, on regarde le nombre de chiffres restants pour cette lettre
        r = N-1
        q = 0 # Nombre de chiffres consommés depuis la droite

        # Boucle qui va parcourir la chaîne S en formant des couples symétriques gauche-droite.
        while l < r or (l == r and q < p):
            # Si l'élément de gauche à l'indice l est une lettre substituée (>=10 dans notre convention)
            if T[l] >= 10:
                # Calcule l'identifiant "virtuel" exact sur la plage allouée pour chaque chiffre d'une lettre
                a = T[l]*2-10+p
                # Si tous les chiffres de la lettre sont consommés, on passe à la lettre suivante à gauche
                if p-1 == -1:
                    l += 1
                    # Met à jour p selon si l'élément suivant est une lettre ou un chiffre
                    p = P[T[l]-10]-1 if T[l] >= 10 else 0
                else:
                    # Sinon, on consomme un chiffre de la lettre
                    p -= 1
            else:
                # Si l'élément de gauche est un chiffre, a est simplement ce chiffre
                a = T[l]
                l += 1
                p = P[T[l]-10]-1 if T[l] >= 10 else 0

            # Même raisonnement pour la droite
            if T[r] >= 10:
                b = T[r]*2-10+q
                # Si tous les chiffres pour cette lettre sont consommés côté droit
                if q+1 == P[T[r]-10]:
                    r -= 1
                    q = 0
                else:
                    # Sinon, on consomme un chiffre de la lettre
                    q += 1
            else:
                # Si c'est un chiffre, on avance simplement le curseur droit
                b = T[r]
                r -= 1
                q = 0
            # On impose qu'à ces deux positions symétriques correspondent le même chiffre, on fusionne donc leurs ensembles.
            unite(a, b)

        # Après la boucle précédente, on vérifie si chaque chiffre de 0 à 9 n'a pas été fusionné à un autre (autrement dit, si le système est cohérent)
        for i in range(10):
            if root(i) != i:
                ok = 0
                break
        # Si ce n'est pas vérifié, on passe à la configuration suivante.
        if not ok:
            continue

        # Initialisation des bornes minimales et maximales autorisées pour chaque composante (pour la gestion des contraintes sur les substituts).
        mi0 = [0]*(10+M*2)
        ma0 = [9]*(10+M*2)

        # Copie de ces bornes, à chaque branche de configuration
        mi = [0]*(10+M*2)
        ma = [9]*(10+M*2)

        # Copie du tableau des parents de la structure union-find, pour pouvoir revenir à l'état initial à chaque itération.
        prt1 = prt[:]

        # Pour chaque configuration possible sur le choix Q (restrictions additionnelles sur les substituts)
        for Q in product([0, 1], repeat = M):
            # On remet à zéro les bornes
            mi[:] = mi0
            ma[:] = ma0
            ok = 1
            # On vérifie pour chaque substitut que si on utilise le nombre maximum de chiffres, Q[i] ne force pas à une contradiction
            for i in range(M):
                if P[i] < L[i] and Q[i] == 1:
                    ok = 0
                    break
            if not ok:
                continue

            # On restaure l'état d'origine de la structure union-find.
            prt[:] = prt1

            # Pour tous les chiffres de 0 à 9 on impose que leur valeur est figée
            for i in range(10):
                mi[i] = ma[i] = i

            # Pour chaque substitut, on applique les contraintes de borne selon la longueur désirée et le cas (Q[i])
            for i in range(M):
                if L[i] == 1: # Si la substitution correspond à un seul chiffre
                    v = U[i]
                    e0 = 2*i+10 # Index unique pour la "case" prise par la valeur de ce substitut
                    if Q[i]: # Si le second cas, on lie la variable à la valeur v
                        unite(v, e0)
                    else: # Sinon, la borne supérieure doit être inférieure à v
                        ma[e0] = v-1
                else: # Si la substitution correspond à deux chiffres
                    v1, v0 = divmod(U[i], 10) # On décompose en dizaines (v1) et unités (v0)
                    e0 = 2*i+10
                    e1 = 2*i+11
                    if Q[i]:
                        unite(v1, e1) # On lie la dizaine à la composante e1
                        ma[e0] = v0 # La composante e0 est bornée supérieurement
                    else:
                        ma[e0] = 9 # Aucun borne stricte sur e0
                        if P[i] == 2:
                            ma[e1] = v1-1 # La dizaine doit être strictement inférieure à v1 si la longueur vaut 2, min à 1
                            mi[e1] = 1

            # Mise à jour globale des bornes après unions : maximum des minimums et minimum des maximums sur chaque racine d'ensemble fusionné.
            for i in range(10+2*M):
                a = root(i)
                mi[a] = max(mi[a], mi[i])
                ma[a] = min(ma[a], ma[i])
            # On vérifie que pour chaque chiffre, il n'a pas été fusionné avec autre chose et que ses bornes sont bien fixées à sa valeur
            for i in range(10):
                if root(i) != i or not mi[i] == i == ma[i]:
                    ok = 0
                    break
            if not ok:
                continue

            # Ici calcule le nombre de combinaisons valides pour la configuration courante.
            res = 1
            for i in range(M):
                e0 = 2*i+10
                e1 = 2*i+11
                if P[i] == 2: # Si la substitution se fait avec deux chiffres
                    if root(e1) == e1: # Si l'ensemble de e1 n'a pas été fusionné à un chiffre déjà fixé
                        # Si la plage de valeurs autorisées est invalide (min>max), c'est impossible
                        if not mi[e1] <= ma[e1]:
                            res = 0
                            break
                        # Multiplication du nombre de valeurs possibles sur ce chiffre
                        res = res * (ma[e1] - mi[e1] + 1) % MOD
                # Même raisonnement pour e0, qui correspond à l'autre chiffre de la substitution
                if root(e0) == e0:
                    if not mi[e0] <= ma[e0]:
                        res = 0
                        break
                    res = res * (ma[e0] - mi[e0] + 1) % MOD
            # Ajout du résultat valide à la réponse globale
            ans += res
    # On ramène la réponse finale à MOD par sécurité
    ans %= MOD
    # On affiche la réponse finale, suivie d'un retour à la ligne
    write("%d\n" % ans)

# Exécution de la fonction principale à l'appel du script
solve()