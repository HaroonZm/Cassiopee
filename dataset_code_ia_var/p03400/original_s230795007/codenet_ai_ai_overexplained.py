import sys  # Importe le module sys, qui fournit des fonctions et des variables utilisées pour manipuler différentes parties de l'environnement d'exécution Python

# Remplace la fonction input intégrée par sys.stdin.readline
# pour une lecture d'entrée standard plus rapide, surtout utile lors de la lecture de grandes quantités de données
input = sys.stdin.readline

def main():  # Définit une fonction principale appelée main, point d'entrée de l'exécution du programme
    # Lit une ligne de l'entrée standard, supprime les espaces blancs (\n, espaces, etc.) en début et fin,
    # puis convertit cette chaîne en entier, ce qui donne le nombre total d'éléments N à traiter
    N = int(input())
    # Lit la ligne suivante de l'entrée standard ; cette ligne doit contenir deux entiers séparés par un espace.
    # Utilise split() pour diviser la ligne en deux chaînes distinctes,
    # map(int, ...) applique la conversion de type int à chacune de ces chaînes,
    # et les deux résultats sont assignés à D (nombre de jours) et X (valeur initiale de la variable ans)
    D, X = map(int, input().split())
    # Initialise une liste A de longueur N, remplie initialement avec la valeur spéciale None.
    # None indique l'absence de valeur et sera remplacé par la suite.
    A = [None] * N
    # Boucle d'itération sur la plage d'indices allant de 0 (inclus) à N (exclu)
    for i in range(N):
        # Pour chaque itération, lit une ligne de l'entrée standard,
        # supprime les espaces inutiles en début et fin,
        # puis convertit la valeur en entier avant de l'affecter dans la liste A à l'indice i
        A[i] = int(input())

    # Initialise la variable ans avec la valeur X.
    # Cette variable servira à accumuler le résultat final qui sera affiché à la fin
    ans = X
    # Boucle sur chaque élément a de la liste A. Ici, 'a' est un entier représentant un intervalle particulier.
    for a in A:
        # Utilise la fonction divmod pour obtenir à la fois le quotient (q) et le reste (r) de la division euclidienne de (D - 1) par a.
        # Cela signifie : combien de fois 'a' rentre dans (D - 1) et quel reste il reste.
        q, r = divmod(D - 1, a)
        # Le nombre de jours où une action doit être effectuée est égal au nombre de tours complets (q) plus 1 pour inclure le jour initial
        ans += q + 1

    # Affiche le résultat final stocké dans la variable ans à la sortie standard
    print(ans)

# Ce bloc vérifie si le script est exécuté en tant que programme principal (et non importé comme module dans un autre script)
if __name__ == "__main__":
    # Si la condition est vraie, appelle la fonction main pour lancer le programme
    main()