import sys
import numpy as np

# Lecture rapide des entrées depuis l'entrée standard (mode binaire)
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def main(n, a):
    """
    Calcule le nombre de paires (i, j) (avec i < j) tel que i+1 == a[j-1] 
    et j+1 == a[i-1]. Cela revient à dénombrer les indices formant des 
    appariements symétriques dans la permutation 'a'.

    Args:
        n (int): Taille du tableau (nombre d'éléments).
        a (np.ndarray): Tableau numpy des éléments de la permutation (base 1).

    Returns:
        int: Le nombre de ces paires, chaque paire étant comptée une fois.
    """
    cnt = 0  # Compteur de paires valides
    for i, j in enumerate(a):
        # Vérifie si l'indice actuel (i+1), correspond à la valeur à la 
        # position (j-1), ce qui signifie que (i+1, j) forme une telle paire.
        if i + 1 == a[j - 1]:
            cnt += 1
    # Chaque paire est comptée deux fois (une fois pour chaque ordre), on divise donc par 2
    return cnt // 2

# Lecture de la taille du tableau depuis l'entrée standard
n = int(readline())
# Lecture du tableau de permutation, conversion en tableau numpy d'entiers 64 bits
a = np.array(readline().split(), np.int64)
# Calcul du résultat et affichage
print(main(n, a))