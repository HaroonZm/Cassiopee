import sys

def lire_entree():
    # lecture à l'ancienne
    return sys.stdin.readline()

def calculer_surface(x, y):
    # orienté objet improvisé
    class Calcule:
        def __init__(self, a, b):
            self.a = a
            self.b = b
        def resultat(self):
            # style fonctional
            return (lambda z, w: z * w / 3.305785)(self.a, self.b)
    return Calcule(x, y).resultat()

(_, __) = tuple(map(int, lire_entree().split()))
surface = calculer_surface(_, __)
print("%.6f" % surface)