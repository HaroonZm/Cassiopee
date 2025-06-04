class RangeMaximumQuery:
    def __init__(self, n):
        # Initialisation d'une instance de la classe RangeMaximumQuery pour un segment [0, n)
        # 'n' est la taille du tableau original, peut-être ajusté à une puissance de 2 pour simplifier
        self.size = n  # On stocke la taille. self.size sera la taille effective de la base de l'arbre
        # Le tableau 'dat' va contenir les valeurs maximales pour chaque segment de l'arbre segmentaire
        # L'arbre segmentaire complet a 2 * n - 1 noeuds internes si on l'implémente ainsi
        self.dat = [0] * (2 * n - 1)  # On initialise toutes les valeurs à 0

    def update(self, i, x):
        # Met à jour la valeur de l'élément à l'index 'i' du tableau original à la valeur 'x'
        # et met à jour les parents de cet élément dans l'arbre segmentaire
        # On appelle cela une "mise à jour ponctuelle"

        # Les feuilles de l'arbre sont stockées à partir de l'indice self.size - 1 dans 'self.dat'
        i += self.size - 1  # On convertit l'index du tableau original à l'index dans 'dat'
        self.dat[i] = x      # Mise à jour directe de la feuille avec la nouvelle valeur

        # On met à jour tous les ancêtres de ce noeud pour que chaque noeud stocke la valeur max de ses deux enfants
        while i > 0:  # Tant qu'on n'est pas à la racine (l'indice 0)
            i = (i - 1) // 2  # On passe à l'index du parent
            d1 = self.dat[i * 2 + 1]  # Valeur max du fils gauche
            d2 = self.dat[i * 2 + 2]  # Valeur max du fils droit
            # On stocke le maximum des deux dans le parent
            if d1 > d2:
                self.dat[i] = d1
            else:
                self.dat[i] = d2

    def getmax(self, a, b, k, l, r):
        # Recherche le maximum dans la plage [a, b) sur le segment [l, r) représenté par le noeud k.
        # Arguments :
        # a, b : bornes de la requête (demande utilisateur)
        # k : index du noeud dans self.dat (démarre toujours par 0)
        # l, r : intervalle du noeud courant (au début l=0, r=self.size)

        # Cas 1 : pas d'intersection entre le segment recherché et le segment actuel, on retourne 0
        if r <= a or b <= l:
            return 0  # On ne prend que des valeurs positives, donc 0 est neutre pour max

        # Cas 2 : le segment courant [l, r) est complètement inclus dans [a, b)
        elif a <= l and r <= b:
            return self.dat[k]  # On retourne la valeur stockée ici qui correspond à ce segment

        # Cas 3 : les segments se recoupent partiellement, on descend dans les deux fils
        else:
            # On découpe [l, r) en deux : [l, mid) (fils gauche), [mid, r) (fils droit)
            mid = (l + r) // 2  # Calcul du point milieu
            vl = self.getmax(a, b, k * 2 + 1, l, mid)  # Recherche max dans le sous-segment gauche
            vr = self.getmax(a, b, k * 2 + 2, mid, r)  # Recherche max dans le sous-segment droit
            # On retourne le maximum des deux côtés
            if vl > vr:
                return vl
            else:
                return vr

def solve():
    from math import ceil, log  # On importe des fonctions mathématiques depuis le module math

    # Lecture d'un entier depuis l'entrée standard (input) représentant la taille du tableau
    n = int(input())  # n, c'est la taille de la séquence d'entiers à traiter

    # Lecture de la séquence d'entiers depuis l'entrée, convertie en int.
    # input() lit une ligne, split() sépare, map(int, ...) applique int à chaque élément
    A = map(int, input().split())

    # Calcul du plus petit entier s qui soit une puissance de 2 supérieure ou égale à n.
    # C'est utile pour simplifier l'arbre segmentaire (implémentation complète/binaire)
    s = 2 ** ceil(log(n, 2))  # On utilise log pour calculer combien il faut élever 2 pour dépasser n

    # Création d'une instance de RangeMaximumQuery pour gérer les mises à jour et requêtes
    W = RangeMaximumQuery(s)

    # Boucle sur chaque élément a_i de la séquence A
    for a_i in A:  # Pour chaque entier de la séquence...
        # On recherche, pour chaque a_i, le coût optimal associé à une certaine politique dynamique
        # W.getmax(0, a_i - 1, 0, 0, s) : Recherche du maximum parmi les indices de 0 à a_i-2
        # On ajoute a_i à ce maximum pour former "cost"
        cost = W.getmax(0, a_i - 1, 0, 0, s) + a_i

        # On met à jour l'arbre segmentaire à la position a_i-1 avec la nouvelle valeur 'cost' calculée
        W.update(a_i - 1, cost)

    # Calcul du résultat final :
    # La formule n * (n + 1) // 2 donne la somme des entiers de 1 à n (somme arithmétique)
    # On soustrait la valeur maximale obtenue via la DP stockée dans l'arbre pour le segment [0, n)
    ans = n * (n + 1) // 2 - W.getmax(0, n, 0, 0, s)

    # On affiche la réponse à la sortie standard (console)
    print(ans)

# Appel de la fonction solve, car c'est le point de départ du programme
solve()