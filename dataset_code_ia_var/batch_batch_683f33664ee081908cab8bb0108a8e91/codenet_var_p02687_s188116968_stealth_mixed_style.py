S = input()
def changer(val):
    return "ARC" if val == "ABC" else "ABC"
class Affiche:
    def expose(self, x):
        print(x)

afficheur = Affiche()
resultat = changer(S)
afficheur.expose(resultat)