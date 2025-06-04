def solve(n, A):
    # Définition d'une fonction interne pour identifier les cycles de permutations présents dans le tableau A.
    def cycles():
        # Création d'une liste de booléens de taille n pour savoir si un index a déjà été visité lors de la construction des cycles.
        V = [False] * n  # Au départ, aucun élément n'a été visité.

        # Création d'une copie triée du tableau original A. Ceci permet de connaître la position finale de chaque élément.
        B = sorted(A)

        # Création d'un dictionnaire pour mapper la valeur de chaque élément (de la liste triée) à son index dans B.
        # Cela permet de retrouver rapidement la destination correcte d'un élément en utilisant sa valeur.
        T = {B[i]: i for i in range(n)}

        # Initialisation d'une liste vide qui contiendra tous les cycles trouvés (chaque cycle est représenté par la liste de ses indices).
        C = []

        # On parcourt chaque index du tableau. Cela permet de débuter un nouveau cycle pour chaque élément non encore visité.
        for i in range(n):
            # Si l'index i a déjà été visité dans un cycle précédent, on le saute.
            if V[i]:
                continue
            # On commence un nouveau cycle à partir de l'index i.
            cur = i  # cur sera utilisé pour suivre la position courante dans le tableau lors de la constitution du cycle.
            cycle = []  # cycle va contenir les indexes du cycle actuellement construit.

            # Tant que l'index courant n'a pas encore été visité,
            # on continue de suivre les échanges nécessaires jusqu'à boucler sur le cycle.
            while not V[cur]:
                V[cur] = True  # On marque l'index courant comme visité pour ne pas le retraiter.
                cycle.append(cur)  # On ajoute l'index courant à la liste représentant le cycle.
                # On trouve la position correcte de la valeur A[cur] en regardant dans le dictionnaire T.
                # Cela indique où l'élément doit aller pour être trié.
                cur = T[A[cur]]

            # Le cycle complet est maintenant construit, on l'ajoute à la liste des cycles.
            C.append(cycle)

        # On retourne la liste de tous les cycles trouvés dans la permutation initiale.
        return C

    # Initialisation d'un accumulateur qui va contenir la réponse finale.
    ans = 0

    # On identifie la valeur minimale dans le tableau A.
    # Cette valeur sera potentiellement utile, car l'intégrer dans certains échanges peut être plus optimal.
    s = min(A)

    # Pour chaque cycle de permutation identifié, on va calculer le coût minimum nécessaire pour trier les éléments de ce cycle.
    for cycle in cycles():
        # On calcule la somme des valeurs des éléments présents dans le cycle.
        S = sum([A[i] for i in cycle])
        # On trouve la valeur minimale parmi les éléments du cycle.
        m = min([A[i] for i in cycle])
        # Le nombre d'éléments dans le cycle.
        an = len(cycle)

        # Deux méthodes sont envisagées pour trier un cycle :
        # - Méthode 1 (classique) : Pour trier un cycle de longueur an, il faut an - 1 échanges.
        #   Le coût est alors la somme S + (an - 2) * m, où m est la valeur la plus légère du cycle.
        # - Méthode 2 (optimale pour certains cas) : On utilise la valeur minimale globale s pour réaliser des échanges,
        #   ce qui peut réduire le coût total dans certains cas.
        #   Le coût est alors m + S + (an + 1) * s.
        # On prend la méthode la moins coûteuse entre les deux.
        ans += min(S + (an - 2) * m, m + S + (an + 1) * s)

    # On retourne le coût total minimal requis pour trier le tableau A.
    return ans

def main():
    # Lecture du nombre d'éléments du tableau à trier depuis l'entrée standard, converti en entier.
    n = int(input())
    # Lecture de la ligne d'entrée suivante, où sont listées les valeurs du tableau.
    # On divise la ligne selon les espaces, puis on convertit chaque objet en entier.
    A = [int(x) for x in input().split()]

    # On appelle la fonction solve avec les deux arguments et on affiche le résultat obtenu.
    print(solve(n, A))

# Exécution de la fonction principale, ce qui permet au script de fonctionner lors de son exécution directe.
main()