# Définition d'une classe nommée Fermat.
# Cette classe va encapsuler les opérations liées au calcul des combinaisons et permutations
# sous un certain modulo, grâce au petit théorème de Fermat pour gérer les inverses modulaire.
class Fermat:

    # Le constructeur de la classe est défini ici.
    # Les arguments 'size' et 'mod' sont requis lors de l'instanciation de l'objet.
    # 'size' représente la taille maximale n pour laquelle on veut pré-calculer les factorielles.
    # 'mod' est le nombre premier modulo pour effectuer tous les calculs.
    def __init__(self, size, mod):
        # On stocke la taille et le modulo en tant qu'attributs de l'instance.
        self.size = size
        self.mod = mod

        # On crée une liste pour stocker les valeurs de factorielles modulo 'mod'.
        # On l'initialise avec [1], c'est-à-dire 0! = 1.
        self.factorial = [1]

        # On crée une liste pour stocker les inverses modulaires des factorielles.
        # On l'initialise aussi avec [1], car l'inverse de 1 est 1.
        self.inverse = [1]

        # On utilise une variable pour conserver la valeur courante de la factorielle lors du calcul en boucle.
        pre_f = 1

        # On va remplir les listes factorial et inverse pour toutes les valeurs de 1 à size (inclus).
        for i in range(1, self.size + 1):
            # On multiplie la valeur précédente de la factorielle par l'entier courant i.
            # On prend immédiatement le résultat modulo 'mod', car sinon les nombres deviennent très grands.
            pre_f = (pre_f * i) % self.mod

            # On ajoute cette nouvelle factorielle à la liste.
            self.factorial.append(pre_f)

            # On calcule l'inverse modulaire de la factorielle courante grâce au petit théorème de Fermat.
            # pow(a, b, c) calcule (a**b) % c de façon efficace même pour b très grand.
            # Ici on utilise pow(pre_f, mod-2, mod), qui donne l'inverse modulaire de pre_f modulo mod,
            # car si mod est premier, a^(mod-2) ≡ a^(-1) [mod mod] selon Fermat.
            self.inverse.append(pow(pre_f, self.mod - 2, self.mod))

    # Fonction pour calculer le nombre de combinaisons ("n choose r") modulo 'mod'.
    # Cela représente le nombre de façons de choisir r objets parmi n, l'ordre n'important pas.
    def comb(self, n, r):
        # Par définition, il n'y a pas de combinaisons valides si on essaie de prendre plus d'objets qu'on en a disponibles.
        if n < r:
            # On renvoie 0 si 'n' est plus petit que 'r'.
            return 0
        else:
            # Sinon, on applique la formule des combinaisons
            # C(n, r) = n! / (r! * (n-r)!)
            # Comme on pré-calculé les factorielles et leurs inverses, on utilise :
            # C(n, r) ≡ n! * (r!)^(-1) * ((n-r)!)^(-1) [mod mod]
            return (self.factorial[n] * self.inverse[r] * self.inverse[n - r]) % self.mod

    # Fonction pour calculer le nombre de permutations ("n perm r") modulo 'mod'.
    # Cela représente le nombre de façons d'organiser r objets parmi n dans un certain ordre.
    def perm(self, n, r):
        # Si r est plus grand que n, il n'y a aucune disposition possible.
        if n < r:
            # On renvoie 0 dans ce cas.
            return 0
        else:
            # Sinon, on applique la formule des arrangements/permutations :
            # P(n, r) = n! / (n - r)!
            # En utilisant le modulo et les inverses précalculés :
            # P(n, r) ≡ n! * ((n-r)!)^(-1) [mod mod]
            return (self.factorial[n] * self.inverse[n - r]) % self.mod

# Ce bloc est appelé uniquement si ce fichier est exécuté directement (et non importé comme module).
if __name__ == "__main__":
    # On crée une instance de la classe Fermat, ici nommée Fermat (avec une majuscule, ce qui n'est pas recommandé en Python).
    # On précalcule les factorielles et inverses jusqu'à 1000, sous le modulo 10**9 + 7 (un nombre premier très utilisé en programmation compétitive).
    Fermat = Fermat(1000, 10**9 + 7)

    # On lit une ligne sur l'entrée standard, supposée contenir deux entiers séparés par un espace.
    # On divise cette ligne en morceaux par split(), et on convertit chaque morceau (i) en entier avec int().
    n, k = [int(i) for i in input().split()]

    # On appel la méthode 'perm' de l'objet Fermat, avec les arguments k et n. 
    # Attention ! L'ordre des arguments dans perm ici est (n, r), mais on passe (k, n).
    # On affiche le résultat retourné, qui est le nombre de permutations de n objets pris parmi k (modulo 10**9 + 7).
    print(Fermat.perm(k, n))