import string

# Définition d'une classe appelée 'SuffixArray' qui va permettre de manipuler et de travailler avec le suffix array d'une chaîne de caractères.
class SuffixArray:
    # Le constructeur (méthode d'initialisation) s'exécute automatiquement à chaque fois qu'une nouvelle instance de la classe est créée.
    # Il prend en paramètre la chaîne S dont on veut construire le suffix array.
    def __init__(self, S):
        # Stocke la longueur de la chaîne S dans l'attribut d'instance self.N
        self.N = len(S)
        # Stocke la chaîne de caractères S elle-même pour une utilisation ultérieure.
        self.S = S
        # Crée un dictionnaire qui associe chaque caractère imprimable à un entier unique (son indice dans string.printable).
        # Cela sert à convertir rapidement un caractère en un entier (utile pour le tri et la comparaison).
        self.atoi = {x: i for i, x in enumerate(string.printable)}
        # Construire le suffix array pour la chaîne S. Le résultat est stocké dans self.sa.
        self.sa = self.__make_sa()

    # Méthode pour afficher (par impression standard) l'ensemble du suffix array avec détails pour chaque suffixe.
    def show(self):
        # On parcourt le suffix array et, pour chaque suffixe, affiche son indice dans le SA, la position d'origine, et le texte du suffixe correspondant.
        for i, s in enumerate(self.sa):
            print(i, s, self.S[s:])

    # Méthode privée (notez le double underscore) qui construit le suffix array selon un algorithme de complexité O(N (logN)^2).
    def __make_sa(self):
        """Renvoie le suffix array pour la chaîne S. Complexité en temps : O(N (logN)^2)."""
        N = self.N  # Longueur de la chaîne d'origine.
        # Initialise la liste SA avec des indices de 0 à N inclus (N inclus pour prendre en compte le suffixe vide).
        SA = list(range(N + 1))
        # La liste 'rank' stocke les rangs (nombres entiers) associés à chaque suffixe de S (basé d'abord sur le premier caractère).
        # On met tous les rangs à -1 par défaut.
        rank = [-1] * (N + 1)
        # 'tmp' est une liste temporaire utilisée lors du processus de mise à jour des rangs au cours du tri.
        tmp = [0] * (N + 1)
        # La variable k contrôle la longueur des préfixes sur lesquels on classera les suffixes à chaque itération (d'abord 1, puis 2, 4, 8, ...).
        k = 1

        # On initialise les rangs pour chaque position de la chaîne : le rang de i correspond au code associé au caractère S[i].
        for i, s in enumerate(self.S):
            rank[i] = self.atoi[s]  # Conversion du caractère en entier pour pouvoir le comparer facilement.

        # Définition d'une fonction auxiliaire 'key' qui, pour l'indice i courant, retourne le tuple de rangs
        # (rank courant, rank du suffixe commencé après k lettres), pour permettre de comparer des paires de préfixes.
        def key(i):
            # Si le suffixe qui commence en i+k existe, on peut obtenir un couple de rangs.
            if i + k <= N:
                return (rank[i], rank[i + k])
            # Sinon, si on déborde de la chaîne, on met -1 pour le second rang pour marquer la fin de la chaîne.
            return (rank[i], -1)

        # Fonction auxiliaire qui permet de faire une comparaison (i < j selon leurs clés de tri).
        def cmp(i, j):
            # On utilise la définition de comparaison naturelle sur les tuples Python.
            return key(i) < key(j)

        # Tant que la taille du préfixe considéré (k) n'a pas dépassé la taille de la chaîne :
        while k <= N:
            # On trie la liste SA selon la clé 'key' définie plus haut: trie les indices selon les paires de rangs.
            # Cela trie les suffixes en fonction des 2k premiers caractères.
            SA.sort(key=key)
            # On réinitialise le rang du premier suffixe à 0.
            tmp[SA[0]] = 0
            # On parcourt les suffixes triés et on attribue un rang incrémenté si la clé (i.e. leur préfixe de longueur 2k) a changé.
            for i in range(1, N + 1):
                tmp[SA[i]] = tmp[SA[i - 1]] + cmp(SA[i - 1], SA[i])
            # On met à jour la liste des rangs avec les nouveaux rangs calculés.
            for i in range(N + 1):
                rank[i] = tmp[i]
            # On double la longueur du préfixe à chaque itération (c'est le cœur de l'algorithme : on classe sur k, puis 2k, etc).
            k *= 2

        # On retourne enfin le suffix array construit.
        return SA

    # Méthode qui permet de vérifier si une sous-chaîne T est incluse dans S, en utilisant la structure du suffix array.
    # Effectue une recherche binaire pour savoir si T apparaît dans S et retourne l'indice dans le suffix array si trouvé, sinon -1.
    def contain(self, T, side="left"):
        """
        Recherche si la chaîne T apparaît dans S.
        Paramètres :
           T   : chaîne ou tableau de caractères à rechercher.
           side: 'left' pour obtenir le plus petit indice i tel que S[sa[i]:sa[i]+len(T)] == T,
                 'right' pour obtenir le plus grand indice i tel que S[sa[i]:sa[i]+len(T)] == T.
        Retourne :
           Index dans le suffix array si T est trouvée, sinon -1.
        """
        NT = len(T)  # Longueur de la chaîne à rechercher.
        # Si la chaîne T à rechercher est plus longue que S, il est impossible de la trouver.
        if NT > self.N:
            return -1
        # On initialise les bornes pour la recherche binaire.
        L = 0
        R = self.N
        if side == "left":
            # Recherche binaire pour trouver le plus petit indice où T est trouvé.
            while R - L > 1:
                # Calcul du point milieu.
                m = (L + R) // 2
                # i est la position de départ du suffixe correspondant dans S.
                i = self.sa[m]
                # On compare le préfixe de longueur NT du suffixe courant à T.
                if self.S[i:i + NT] < T:
                    L = m  # Si le préfixe est plus petit, on doit aller à droite.
                else:
                    R = m  # Sinon on resserre à gauche.
            # À la fin de la boucle, on vérifie si T correspond bien au préfixe du suffixe à l'indice R.
            i = self.sa[R]
            if self.S[i:i + NT] == T:
                return R
        else:
            # Pour chercher la borne supérieure, on met R à N+1.
            R += 1
            # Recherche binaire pour la plus grande position où un préfixe de suffixe <= T.
            while R - L > 1:
                m = (L + R) // 2
                i = self.sa[m]
                if self.S[i:i + NT] <= T:
                    L = m
                else:
                    R = m
            i = self.sa[L]
            if self.S[i:i + NT] == T:
                return L
        # Si on n'a rien trouvé, renvoie -1.
        return -1

    # Méthode pour obtenir la liste des positions originales dans S où la sous-chaîne T apparaît.
    def get_indices(self, T):
        """
        Cherche toutes les occurrences (positions de départ) de la chaîne T dans S à l'aide du suffix array.
        Retourne : une liste des indices (positions dans S) où T commence.
        """
        # Cherche la plus petite position du SA où T apparaît.
        L = self.contain(T, side="left")
        # Si pas trouvée, retourne une liste vide.
        if L == -1:
            return []
        # Cherche la plus grande position du SA où T apparaît.
        R = self.contain(T, side="right")
        # Récupère tous les indices du SA entre L et R inclus (positions de début dans S où T apparaît).
        return [self.sa[i] for i in range(L, R+1)]

# Construction de l'objet SuffixArray à partir d'une chaîne entrée par l'utilisateur.
SA = SuffixArray(input())
# On lit une seconde chaîne (la sous-chaîne à chercher), puis on récupère dans 'res' la liste de toutes les occurrences (indices).
res = SA.get_indices(input())
# Si la sous-chaîne a été trouvée (c’est-à-dire si la liste n'est pas vide) :
if res:
    # On trie les résultats par ordre croissant (par position d'apparition dans S).
    res.sort()
    # On affiche chaque indice (position) où la sous-chaîne apparaît, séparé par des sauts de ligne.
    print(*res, sep="\n")