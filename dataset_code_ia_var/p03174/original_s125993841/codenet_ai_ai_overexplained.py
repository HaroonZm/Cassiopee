import numpy as np  # Importe le module numpy, une bibliothèque pour effectuer des calculs numériques rapides avec des tableaux multidimensionnels.
from numba import njit  # Importe njit de numba pour compiler plus rapidement, mais la décoration est commentée ici.
MOD = 10**9 + 7  # Définit une constante entière appelée MOD de valeur 10 puissance 9 plus 7, fréquemment utilisée pour le modulo afin d'éviter les débordements d'entiers et d'assurer de petits résultats.

def main():
    # Lit un nombre entier N depuis l'entrée standard (input est une fonction Python intégrée).
    N = int(input())  # input() renvoie une chaîne, int() convertit cela en entier.
    
    # Crée un tableau numpy de forme N x N (tableau carré) pour stocker les affinités.
    # On construit une liste où chaque élément est une ligne entrée et convertie en liste d'entiers,
    # puis on transforme la liste de listes en un tableau numpy (structure de données similaire à une matrice).
    aff = np.array(
        [list(map(int, input().split())) for i in range(N)],
        dtype='int32'  # On utilise le type entier 32 bits pour économiser la mémoire.
    )

    # Crée un tableau numpy nommé dpt de forme (N+1) x (2^N), initialisé à des zéros.
    # dpt[i][j] stockera le nombre de façons d'arranger les affectations jusqu'à l'étape i avec une configuration spécifique j (bitmask).
    dpt = np.zeros((N+1, 1<<N), dtype='int64')  # 1 << N effectue un décalage de bits pour calculer 2 à la puissance N.

    # Initialisation de la position de départ : il existe 1 seule façon de commencer sans aucune affectation (c'est l'état vide).
    dpt[0][0] = 1

    # Calcule la réponse finale en appelant la fonction solve, puis l'affiche.
    print(solve(N, aff, dpt))


# La fonction solve résout le problème principal via la programmation dynamique (DP).
# N  : Le nombre d'éléments à traiter (taille de l'ensemble).
# aff: La matrice d'affinité, c'est-à-dire une matrice qui indique si une personne peut recevoir une tâche.
# dpt: Le tableau de DP tel que décrit ci-dessus.
def solve(N, aff, dpt):
    # Boucle sur chaque personne (ou ligne) dans la matrice d'affinités aff.
    for i, row in enumerate(aff):
        # Pour chaque tâche (ou colonne) dans la ligne courante, on vérifie si la personne i peut effectuer la tâche idx.
        for idx, v in enumerate(row):
            # Vérifie si l'affinité est valide (v == 1 signifie que la tâche peut être assignée à la personne).
            if v == 1:
                # Pour chaque état d'affectation précédent (représenté par les bits dpt[i]),
                # on ajoute les façons d'arriver à chaque nouvel état du masque à dpt[i+1].
                # (1<<idx) déplace un 1 à la place idx ; cela sert à "assigner" la tâche idx.
                # dpt[i][:-(1<<idx)] sélectionne tous les états où cette tâche n'a pas encore été assignée.
                # dpt[i+1][(1<<idx):] correspond aux états où cette tâche est maintenant assignée. 
                dpt[i+1][(1<<idx):] += dpt[i][:-(1<<idx)]
        # Applique le modulo MOD à toute la nouvelle ligne pour éviter les débordements et maintenir les résultats petits.
        dpt[i+1] %= MOD
    # Retourne la réponse finale: le nombre de façons de tout affecter (N personnes à N tâches),
    # c'est-à-dire le nombre de façons d'arriver à l'état (1<<N)-1 (toutes les tâches assignées).
    return dpt[N][(1<<N)-1]


# Ce bloc garantit que le code ci-dessus sera exécuté seulement si le fichier est exécuté directement,
# et pas lorsqu'il est importé comme module.
if __name__ == '__main__':
    main()