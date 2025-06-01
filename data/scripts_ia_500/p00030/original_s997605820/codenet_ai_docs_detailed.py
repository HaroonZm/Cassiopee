import sys
# Augmente la limite de récursion pour permettre un plus grand nombre d'appels récursifs
sys.setrecursionlimit(10000)

def solve(i, wa, use):
    """
    Fonction récursive pour compter le nombre de combinaisons d'entiers distincts entre 1 et 9
    qui totalisent exactement la somme s en utilisant exactement n nombres.

    Args:
        i (int): L'entier actuel considéré (de 0 à 9, où i représente les nombres de 1 à 9).
        wa (int): La somme accumulée jusqu'à présent.
        use (int): Le nombre de valeurs utilisées jusqu'à présent.

    Variables globales utilisées:
        ct (int): Compteur global du nombre de combinaisons valides.
        s (int): Somme cible à atteindre.
        n (int): Nombre de valeurs à utiliser pour atteindre la somme s.
    """
    global ct, s, n

    # Condition d'arrêt : si la somme accumulée wa est égale à la somme cible s
    # et si le nombre d'éléments utilisés est exactement n, on a trouvé une combinaison valide
    if wa == s and use == n:
        ct += 1
        return

    # Conditions de coupure pour éviter des calculs inutiles :
    # - si le nombre d'éléments dépassés
    # - si on a considéré tous les nombres possibles (de 1 à 9)
    # - si la somme accumulée dépasse la somme cible
    if use > n or i == 10 or wa > s:
        return

    # Ne pas inclure l'entier courant i dans la combinaison et avancer au suivant
    solve(i + 1, wa, use)

    # Inclure l'entier courant i dans la somme et augmenter le compteur d'éléments utilisés,
    # puis passer à l'entier suivant
    solve(i + 1, wa + i, use + 1)


# Boucle principale qui lit les entrées jusqu'à ce que n et s soient 0
while True:
    # Lecture des deux entiers n et s depuis l'entrée standard
    n, s = map(int, raw_input().split())

    # Condition d'arrêt de la boucle : si n et s sont tous deux 0
    if n == 0 and s == 0:
        break

    # Initialisation du compteur global de solutions à 0
    ct = 0

    # Début de la recherche des combinaisons avec i à 0 (correspond à 1), somme 0 et 0 éléments utilisés
    solve(0, 0, 0)

    # Affiche le nombre total de combinaisons trouvées pour ces valeurs de n et s
    print ct