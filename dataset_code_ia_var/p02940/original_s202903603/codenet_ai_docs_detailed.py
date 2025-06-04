from functools import reduce

# Lecture du nombre de balles N
N = int(input())
# Lecture de la chaîne de couleurs
S = input()

# Constante pour le calcul modulo
MOD = 998244353

class ModInt:
    """
    Classe pour effectuer des opérations arithmétiques sous un modulo donné.

    Attributs :
        x (int) : La valeur entière conservée modulo MOD.

    Méthodes :
        __add__, __sub__, __mul__, __truediv__, __pow__ : Surcharge des opérateurs pour permettre
            les opérations arithmétiques entre instances ModInt et entiers.
        __radd__, __rsub__, __rmul__, __rtruediv__, __rpow__ : Version réfléchie pour la commutativité.
        __str__, __repr__ : Pour l'affichage.
    """

    def __init__(self, x):
        """
        Initialise la valeur à x modulo MOD.
        """
        self.x = x % MOD

    def __str__(self):
        """
        Affiche la valeur entière.
        """
        return str(self.x)

    __repr__ = __str__

    def __add__(self, other):
        """
        Surcharge de l'opérateur +.
        """
        return (
            ModInt(self.x + other.x) if isinstance(other, ModInt) else
            ModInt(self.x + other)
        )

    def __sub__(self, other):
        """
        Surcharge de l'opérateur -.
        """
        return (
            ModInt(self.x - other.x) if isinstance(other, ModInt) else
            ModInt(self.x - other)
        )

    def __mul__(self, other):
        """
        Surcharge de l'opérateur *.
        """
        return (
            ModInt(self.x * other.x) if isinstance(other, ModInt) else
            ModInt(self.x * other)
        )

    def __truediv__(self, other):
        """
        Surcharge de l'opérateur / pour la division entière modulaire (avec inverse).
        """
        return (
            ModInt(self.x * pow(other.x, MOD - 2, MOD)) if isinstance(other, ModInt) else
            ModInt(self.x * pow(other, MOD - 2, MOD))
        )

    def __pow__(self, other):
        """
        Surcharge de l'opérateur ** pour la puissance modulaire.
        """
        return (
            ModInt(pow(self.x, other.x, MOD)) if isinstance(other, ModInt) else
            ModInt(pow(self.x, other, MOD))
        )

    def __radd__(self, other):
        """
        Surcharge réfléchie pour +.
        """
        return ModInt(other + self.x)

    def __rsub__(self, other):
        """
        Surcharge réfléchie pour -.
        """
        return ModInt(other - self.x)

    def __rmul__(self, other):
        """
        Surcharge réfléchie pour *.
        """
        return ModInt(other * self.x)

    def __rtruediv__(self, other):
        """
        Surcharge réfléchie pour /.
        """
        return ModInt(other * pow(self.x, MOD - 2, MOD))

    def __rpow__(self, other):
        """
        Surcharge réfléchie pour **.
        """
        return ModInt(pow(other, self.x, MOD))


def f(s, res, z, r, g, b, rg, gb, br):
    """
    Attribue la balle courante de couleur `s` à la personne éligible qui possède actuellement
    le plus de balles, en tenant compte des paires formées.

    Paramètres :
        s (str) : la couleur de la balle ('R', 'G' ou 'B')
        res (ModInt) : le nombre total de façons jusqu'à présent
        z (int) : nombre de personnes sans balle
        r (int) : nombre de personnes ayant 1 balle rouge
        g (int) : nombre de personnes ayant 1 balle verte
        b (int) : nombre de personnes ayant 1 balle bleue
        rg (int) : nombre de personnes ayant une rouge et une verte
        gb (int) : nombre de personnes ayant une verte et une bleue
        br (int) : nombre de personnes ayant une bleue et une rouge

    Retourne :
        Tuple : état actualisé après distribution de la balle courante.
    """
    # Pour chaque couleur, on priorise l'attribution à ceux qui ont déjà des paires spécifiques,
    # puis à ceux qui ont une balle de la couleur correspondante, ensuite ceux qui peuvent compléter une paire,
    # et enfin à une personne sans balle.
    if s == 'R':
        if gb:
            # Priorité : donner au groupe GB (deviendra RGB)
            return (res * gb, z, r, g, b, rg, gb - 1, br)
        elif g:
            # Ensuite : à une personne avec une verte (devient RG)
            return (res * g, z, r, g - 1, b, rg + 1, gb, br)
        elif b:
            # Ensuite : à une personne avec une bleue (devient BR)
            return (res * b, z, r, g, b - 1, rg, gb, br + 1)
        else:
            # Sinon : à une personne sans balle (devient R)
            return (res * z, z - 1, r + 1, g, b, rg, gb, br)
    elif s == 'G':
        if br:
            # Priorité : donner au groupe BR (devient RGB)
            return (res * br, z, r, g, b, rg, gb, br - 1)
        elif r:
            # Ensuite : à une personne avec une rouge (devient RG)
            return (res * r, z, r - 1, g, b, rg + 1, gb, br)
        elif b:
            # Ensuite : à une personne avec une bleue (devient GB)
            return (res * b, z, r, g, b - 1, rg, gb + 1, br)
        else:
            # Sinon : à une personne sans balle (devient G)
            return (res * z, z - 1, r, g + 1, b, rg, gb, br)
    else:  # s == 'B'
        if rg:
            # Priorité : donner au groupe RG (devient RGB)
            return (res * rg, z, r, g, b, rg - 1, gb, br)
        elif r:
            # Ensuite : à une personne avec une rouge (devient BR)
            return (res * r, z, r - 1, g, b, rg, gb, br + 1)
        elif g:
            # Ensuite : à une personne avec une verte (devient GB)
            return (res * g, z, r, g - 1, b, rg, gb + 1, br)
        else:
            # Sinon : à une personne sans balle (devient B)
            return (res * z, z - 1, r, g, b + 1, rg, gb, br)


# La variable `ans` capture le nombre total de façons possibles d'attribuer les balles,
# le reste de la tuile étant jeté (_).
# On utilise `reduce` pour appliquer la fonction `f` sur chaque balle dans l'ordre,
# en commençant par l'état initial :
# - res=ModInt(1) : 1 façon initiale
# - z=N : tous n'ont pas de balles au départ
# - r, g, b, rg, gb, br = 0 : aucun n'a une balle ou une paire au départ.
ans, *_ = reduce(
    lambda acc, s: f(s, *acc),  # Accumulateur mis à jour pour chaque balle
    S,                          # Itère sur la séquence de couleurs
    (ModInt(1), N, 0, 0, 0, 0, 0, 0)  # État initial
)

# Affiche le nombre de façons (modulo MOD)
print(ans)