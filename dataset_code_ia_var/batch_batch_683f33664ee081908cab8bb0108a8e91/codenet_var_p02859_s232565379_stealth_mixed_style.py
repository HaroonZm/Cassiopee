def carré(n): return n**2
class Calcul:
 pass
Calcul.valeur = (lambda: int(input()))()
def afficher_res(res):
    print(res)
afficher_res(carré(Calcul.valeur))