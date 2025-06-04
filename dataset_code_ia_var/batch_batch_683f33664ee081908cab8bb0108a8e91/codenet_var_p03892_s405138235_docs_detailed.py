import sys
from fractions import gcd

def main():
    """
    Fonction principale qui lit les entrées, calcule la réponse et l'affiche.
    """
    # Redéfinir la fonction d'entrée pour tirer parti de sys.stdin.readline, qui est plus rapide pour les grandes entrées.
    input = sys.stdin.readline

    # Augmenter la limite de récursion pour permettre des appels récursifs profonds si nécessaire.
    sys.setrecursionlimit(10 ** 7)

    # Lire quatre entiers de l'entrée standard, qui représentent les coordonnées (A,B) et (C,D).
    A, B, C, D = map(int, input().split())

    # Calculer la différence absolue des abscisses.
    dx = abs(A - C)
    # Calculer la différence absolue des ordonnées.
    dy = abs(B - D)

    # Calculer le plus grand commun diviseur (PGCD) des différences pour utiliser dans la formule finale.
    g = gcd(dx, dy)
    # Calculer la réponse selon la formule donnée : (dx + dy) - gcd(dx, dy).
    answer = (dx + dy) - g

    # Afficher la réponse sur la sortie standard.
    print(answer)

if __name__ == "__main__":
    main()