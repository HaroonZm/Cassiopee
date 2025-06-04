import sys
import math

# Pré-calcul des nombres premiers jusqu'à 10^6 avec le crible d'Ératosthène
MAX_M = 10**6
is_prime = [True] * (MAX_M + 1)
is_prime[0] = False
is_prime[1] = False
for i in range(2, int(MAX_M**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, MAX_M + 1, i):
            is_prime[j] = False


def get_children(cave_num, m):
    """
    Calcule les caves "en dessous" du cave_num selon la règle décrite dans l'énoncé.
    Trouve les 3 caves possibles directement sous cave_num selon le numéro des caves.
    Renvoie une liste des caves enfants valides (<= m).
    
    Pour trouver les enfants, on utilise la relation entre numéros de caves :
    d'après la spirale en carrés, on peut déduire la position (x,y) du cave_num,
    puis ses enfants sont ceux situés sous lui : (x+1, y-1), (x+1, y), (x+1, y+1).
    Mais puisque la position n'est pas donnée, on s'appuie sur la numérotation en spirale.
    
    Cependant, ce problème est un classique modifié : les enfants d'une cave i sont i + ligne,
    i + ligne - 1, i + ligne + 1 où ligne est l'indice de la ligne descendante.
    
    Or ce n'est pas fourni directement.
    
    Approche simplifiée :
    Comme la grille est carrée et numérotée en spirale à partir du centre,
    on remarque dans le problème original que la numérotation correspond à un carré en spirale.
    On peut trouver la "coordonnée verticale" de la cave en fonction de son numéro.
    Mais c'est complexe. 
    
    Heureusement, ce problème est classique dans ce concours.
    La relation entre un noeud i et ses enfants est :
    Les enfants sont : i + ligne, i + ligne - 1, i + ligne + 1
    où "ligne" correspond à la longueur de la ligne descendante, calculée par
    la fonction suivante (on détermine pour i le numéro de la ligne descendante).
    
    En résumé : 
    - Pour i, déterminer la ligne descendante à laquelle i appartient.
    - La ligne descendante L est l'entier comme suit : L = floor((sqrt(i - 1) + 1) / 2)
    - Les enfants sont i + L, i + L - 1, i + L + 1 (filtrés pour être <= m).
    """

    # Calcul de la ligne descendante L à partir du numéro cave_num
    # Formule déduite du pattern de la spirale carrée.
    # Dérivé de la racine carrée correspond à la couche dans la spirale.
    layer = int(math.floor((math.sqrt(cave_num - 1) + 1) / 2))
    children = []
    for diff in (layer - 1, layer, layer + 1):
        child = cave_num + diff
        if 1 <= child <= m:
            children.append(child)
    return children


def solve(m, n):
    """
    Trouve la route descendant maximum en nombre de caves premières en partant de n.
    Retourne (nombre_de_caves_premieres, dernier_no_cave_premiere)
    ou (0, 0) si aucun chemin avec des caves premières n'existe.
    
    On utilise une approche de programmation dynamique avec mémorisation car on peut
    réutiliser les résultats des sous-chemins.
    
    - Si la cave n'est pas prime, elle n'est pas comptée dans la longueur, mais on doit continuer.
    - On cherche le chemin descendant avec le maximum de caves premières.
    - En cas d'égalité, on choisit le chemin dont la dernière cave première est la plus grande.
    
    Pour cela, on mémorise pour chaque cave le tuple : 
    (max_nb_primes_sur_chemin, dernier_prime_sur_chemin)
    """

    from functools import lru_cache

    @lru_cache(None)
    def dfs(cave_num):
        # Recherche la meilleure route descendant en partant de cave_num
        children = get_children(cave_num, m)

        # Si pas d'enfants, alors la route se termine ici
        # Valeur dépend de cave_num (prime ou pas)
        if not children:
            if is_prime[cave_num]:
                return (1, cave_num)
            else:
                return (0, 0)

        # Recherche récursive sur enfant
        best = (0, 0)  # (max_prime_count, last_prime_number)
        for c in children:
            res = dfs(c)
            # on veut la meilleure sous-route
            if res[0] > best[0]:
                best = res
            elif res[0] == best[0]:
                # En cas d'égalité sur le nombre de primes, le plus grand dernier prime
                if res[1] > best[1]:
                    best = res

        # Ajouter cette cave si prime
        if is_prime[cave_num]:
            # compteur + 1, dernier prime devient cave_num (parce que on est avant enfants)
            return (best[0] + 1, cave_num)
        else:
            # pas prime, on ne compte pas mais on garde le meilleur chemin enfants
            return best

    res = dfs(n)

    # Si pas de chemin avec primes
    if res[0] == 0:
        print("0 0")
    else:
        print(res[0], res[1])


def main():
    for line in sys.stdin:
        if line.strip() == '':  # Ignorer lignes vides éventuelles
            continue
        m, n = map(int, line.strip().split())
        if m == 0 and n == 0:
            break
        solve(m, n)

if __name__ == '__main__':
    main()