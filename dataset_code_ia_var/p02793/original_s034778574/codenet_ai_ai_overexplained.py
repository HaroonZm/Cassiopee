from fractions import gcd  # Importe la fonction gcd (Greatest Common Divisor) du module fractions (note: deprecated en Python 3.5+)

def main():
    # Lit une ligne de l'entrée standard et la convertit en entier
    N = int(input())  # N représente le nombre d'éléments dans la liste

    # Lit la ligne suivante, la découpe en sous-chaînes selon les espaces,
    # convertit chaque sous-chaîne en entier et rassemble le tout dans une liste
    A = list(map(int, input().split()))  # A contiendra la liste d'entiers

    mod = 10 ** 9 + 7  # Définit la valeur du modulo, qui est un grand nombre premier utilisé pour éviter les débordements

    b = 0  # Initialise la variable b à 0, elle sera utilisée pour stocker le résultat de la somme finale
    c = 1  # Initialise la variable c à 1, elle sera utilisée pour calculer le PPCM (Produit Plus Petit Commun Multiple)

    # Cette boucle parcourt chaque élément 'a' dans la liste A pour calculer le PPCM de tous les éléments de la liste
    for a in A:
        # Le PPCM de deux nombres x et y est (x * y) // gcd(x, y)
        # Ici, on met à jour 'c' à chaque itération pour qu'il contienne le PPCM courant
        c = c * a // gcd(c, a)  # 'c * a' multiplie c par a, 'gcd(c, a)' donne leur PGCD

    # On ramène la valeur de 'c' dans la plage [0, mod), c'est-à-dire qu'on fait le modulo mod
    c %= mod

    # Cette boucle parcourt à nouveau chaque élément 'a' pour calculer et ajouter à 'b' la quantité demandée
    for a in A:
        # pow(a, mod-2, mod) calcule l'inverse multiplicatif de a modulo mod, c'est-à-dire un nombre tel que (a * x) % mod == 1
        # En arithmétique modulaire, cela équivaut à a^(mod-2) % mod quand mod est premier, par le petit théorème de Fermat
        inv_a = pow(a, mod-2, mod) # Calcule l'inverse modulaire de a modulo mod

        # c * inv_a donne une valeur qui équivaut à c // a modulo mod
        # On ajoute cette valeur à b, ainsi b accumule les valeurs pour tous les éléments de A
        b += c * inv_a  # On ajoute la quantité pour cet a à la somme totale b

    # Enfin, on affiche la somme totale b modulo mod pour garantir que le résultat tient dans des bornes raisonnables
    print(b % mod)

# Ce bloc conditionnel permet de n'exécuter la fonction main() que si le script est exécuté comme programme principal
if __name__ == "__main__":
    main()  # On appelle la fonction main pour lancer le programme