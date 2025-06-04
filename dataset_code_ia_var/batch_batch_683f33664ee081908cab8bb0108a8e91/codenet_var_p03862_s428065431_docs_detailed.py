#!/usr/bin/env python3

def main():
    """
    Contrôle le flux principal du programme :
    - Lit les entrées utilisateur pour déterminer le nombre de cases et la valeur maximale par paire.
    - Ajuste la liste de nombres en appliquant une transformation spécifique et additionne le total retiré.
    - Affiche le résultat final.
    """
    # Lecture des entrées : N (nombre de cases), X (somme maximale autorisée pour toutes les paires adjacentes)
    N, X = map(int, input().split())
    
    # Lecture de la liste des A_i et ajout d'un zéro à la fin pour simplifier le traitement de la dernière paire
    A = list(map(int, input().split())) + [0]

    # Initialise la variable pour accumuler la quantité totale retirée
    result = 0

    # Parcourt chaque case pour vérifier (avec la précédente) si la somme dépasse X
    for i in range(N):
        # Calcule l'excès éventuel à retirer pour que la somme ne dépasse pas X
        # max(0, ...) car il n'y a pas d'excès si la somme est inférieure ou égale à X
        tmp = max(0, A[i] + A[i - 1] - X)
        # Ajoute l'excès retiré au total
        result += tmp
        # Réduit la valeur actuelle de l'excès pour respecter la contrainte de somme maximale
        A[i] -= tmp

    # Affiche le résultat total des quantités retirées
    print(result)

if __name__ == "__main__":
    main()