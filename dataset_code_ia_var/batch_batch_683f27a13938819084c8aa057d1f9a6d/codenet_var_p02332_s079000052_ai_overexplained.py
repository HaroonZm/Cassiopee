from collections import defaultdict

class Combinatorics:
    def __init__(self, N, mod):
        '''
        Initialise la classe Combinatorics.
        Cette initialisation pré-calcule toutes les valeurs nécessaires pour calculer rapidement les coefficients binomiaux (combinaisons) et d’autres objets combinatoires modulo "mod".
        Entrées :
            N (int) : la plus grande valeur de n dont on aura besoin (bornes des précalculs)
            mod (int) : nombre premier, module pour effectuer les calculs dans le corps fini Z/(mod)Z
        '''
        self.mod = mod  # Stocke la valeur du modulo comme attribut d’instance
        # Création de dictionnaires pour stocker les valeurs précalculées
        # self.fact contiendra les factorielles jusqu'à N : fact[n] = n!
        self.fact = {i: None for i in range(N+1)}         
        # self.inverse contiendra l’inverse de chaque entier de 1 à N modulo mod
        self.inverse = {i: None for i in range(1, N+1)}   
        # self.fact_inverse contiendra l’inverse de la factorielle de chaque entier de 0 à N
        self.fact_inverse = {i: None for i in range(N+1)} 
        
        # Prétraitement des valeurs
        # La factorielle de 0 (par définition) est 1
        self.fact[0] = 1
        # La factorielle de 1 est aussi 1
        self.fact[1] = 1
        # L’inverse de la factorielle de 0 est 1
        self.fact_inverse[0] = 1
        # L’inverse de la factorielle de 1 est aussi 1
        self.fact_inverse[1] = 1
        # L’inverse de 1 modulo mod est 1 car 1*1 = 1 pour tout mod
        self.inverse[1] = 1

        # Boucle pour pré-calculer toutes les valeurs de fact, inverse et fact_inverse jusqu’à N
        for i in range(2, N+1):
            # Calcule de la factorielle de i modulo mod, c'est-à-dire self.fact[i] = (i * self.fact[i-1]) % mod
            self.fact[i] = i * self.fact[i-1] % self.mod

            # Calcul de l’inverse de i dans le corps Z/(mod)Z
            # Utilisation d’une relation de récurrence basée sur le fait que mod est un nombre premier
            # L’inverse de i modulo mod peut se calculer par : inv[i] = - (mod // i) * inv[mod % i] % mod
            q, r = divmod(self.mod, i)
            self.inverse[i] = (- (q % self.mod) * self.inverse[r]) % self.mod 

            # L’inverse de la factorielle de i est le produit de l’inverse de i et de l’inverse de la factorielle précédente, modulo mod
            self.fact_inverse[i] = self.inverse[i] * self.fact_inverse[i-1] % self.mod

    def perm(self, n, r):
        '''
        Calcule le nombre de permutations (k arrangements) : nPr = n! / (n-r)!
        C’est à dire, le nombre de façons d’ordonner r objets parmi n différents.
        La valeur retournée est calculée modulo self.mod.
        Si n < r (on pioche plus d’objets qu’on en possède), ou si n ou r est négatif, on considère qu’il n’y a aucune façon, donc on retourne 0.
        '''
        if n < r or n < 0 or r < 0:
            return 0  # Cas non valide : on ne peut pas choisir plus d’éléments qu’il n’y en a, ou valeurs négatives
        else:
            # Formule : nPr = n! / (n-r)!. On utilise les inverses précalculés pour éviter la division.
            # (a / b) % mod équivaut à (a * inverse(b)) % mod sur un corps fini
            return (self.fact[n] * self.fact_inverse[n-r]) % self.mod

    def binom(self, n, r):
        '''
        Calcule le coefficient binomial, c’est-à-dire le nombre de combinaisons de n objets pris r à la fois : nCr = n! / (r! * (n-r)!)
        Le résultat est renvoyé modulo self.mod.
        Si n < r, ou si n ou r est négatif, cela n’a pas de sens, donc la fonction retourne 0.
        '''
        if n < r or n < 0 or r < 0:
            return 0  # Cas impossible ou non défini
        else:
            # Formule de combinaison : nCr = n! / (r! * (n-r)!)
            # On multiplie les inverses de r! et de (n-r)! précalculés.
            return self.fact[n] * (self.fact_inverse[r] * self.fact_inverse[n-r] % self.mod) % self.mod

    def hom(self, n, r):
        '''
        Calcule le nombre de multisets ou combinaisons avec répétitions (nHr, aussi noté "hom" pour multinomiale de rang r sur n types).
        La formule est : nHr = C(n+r-1, r), c’est-à-dire le coefficient binomial (n+r-1)Cr.
        Ceci correspond à la répartition de r objets identiques dans n cases, les cases pouvant rester vides.
        Quelques exemples de partitions d’objets :
            o o o | o o | | | o | | | o o | | o
        '''
        # Cas (bord) : aucune classe, mais au moins un objet à placer → impossible
        if n == 0 and r > 0:
            return 0
        # Cas (bord) : peu importe le nombre de classes (n>=0), on a aucun objet à placer → il n’y a qu’une seule façon de tout laisser vide
        if n >= 0 and r == 0:
            return 1
        # Sinon, on utilise la formule du binomial classique
        return self.binom(n + r - 1, r)

# Lecture de deux entiers n et k à partir de l’entrée standard
n, k = map(int, input().split())
# Définition du modulo (classique en combinatoire modulaire : un grand nombre premier)
MOD = 10**9 + 7
# Création d’une instance de Combinatorics avec k comme borne supérieure de précalcul
com = Combinatorics(k, MOD)
# Calcul et stockage du nombre de permutations de k objets pris n à la fois, modulo MOD
ans = com.perm(k, n)
# Affichage du résultat (le nombre de permutations modulo MOD)
print(ans)