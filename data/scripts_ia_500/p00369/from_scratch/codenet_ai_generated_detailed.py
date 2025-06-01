import sys
sys.setrecursionlimit(10**7)

# Problème résumé :
# On doit découper la chaîne donnée en au moins deux segments, chacun représentant un nombre entier (sans zéro),
# afin de minimiser la différence entre la plus grande valeur segmentée et la plus petite valeur segmentée.
# La chaîne est composée uniquement de chiffres de 1 à 9, la longueur peut aller jusqu'à 100000.

# Approche et défi :
# Une recherche exhaustive de toutes les partitions est impossible à cause de la taille.
# Le but est de minimiser la différence max-min entre valeurs segmentées.
# Chaque segment est un nombre formé par un sous-intervalle de la chaîne.
# On doit trouver une partition avec au moins 2 segments.

# Observation importante :
# - La différence max-min sera au moins 0 (si segments égaux), sinon plus.
# - Si on choisit une partition avec 2 segments, on peut essayer toutes les coupures et calculer diff.
# - Le problème est que la taille du nombre segmenté peut être très grande (jusqu'à 100000), surpassant la capacité d'int.
# - Mais chaque segment peut contenir plusieurs chiffres (pas de limitation de taille segment).
#   Cependant, le maximum diff veut dire qu'on doit comparer des entiers très grands.
# - On pourra manipuler l'entier sous forme de chaîne: comparer lexicographiquement comme des nombres
#   et faire la soustraction manuellement pour le minimum absolu.

# Stratégié pour l'efficacité :
# - Comme n peut aller jusqu'à 100000, on ne peut pas tester toutes les partitions (2^(n-1) trop grand).
# - En effet, on peut seulement couper en exactement deux segments : couper la chaîne en position i (1 <= i < n) et comparer.
# - Ceci garanti au moins deux segments, car demandé « plus d’un segment ».
# - On calcule la différence entre la valeur formée par s[:i] et s[i:], et on garde le minimal.

# Comparaison de nombres très grands en chaîne :
# - Pour comparer deux nombres en string sans conversion en int, on compare la longueur.
# - Plus long est plus grand.
# - Si même longueur, on fait une comparaison lexicographique.

# Soustraction de deux nombres très grands en string (pour difference) :
# - La différence à retourner est la valeur absolue de (G - L),
#   où G = max segment, L = min segment.
# - On doit faire une soustraction arithmétique sur strings.

def compare_num_str(a: str, b: str) -> int:
    # Retourne -1 si a < b, 0 si égal, 1 si a > b selon valeur numérique
    if len(a) < len(b):
        return -1
    elif len(a) > len(b):
        return 1
    else:
        # même longueur
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0

def subtract_num_str(a: str, b: str) -> str:
    # Calcule |a - b|, avec a et b >= 0 (représentation numérique sans zéro), en string
    # Procède que a >= b sinon swap
    if compare_num_str(a, b) < 0:
        a, b = b, a
    
    # a >= b
    res = []
    a_len = len(a)
    b_len = len(b)

    carry = 0
    # On soustrait de la droite vers la gauche
    for i in range(1, a_len+1):
        x = int(a[-i])
        y = int(b[-i]) if i <= b_len else 0
        diff = x - y - carry
        if diff < 0:
            diff += 10
            carry = 1
        else:
            carry = 0
        res.append(str(diff))
    
    # Enlever les zéros non significatifs à gauche
    while len(res) > 1 and res[-1] == '0':
        res.pop()
    # Résultat inversé
    res.reverse()
    return ''.join(res)

def main():
    s = input().strip()
    n = len(s)
    
    # Initialiser la différence avec une valeur très élevée (on stocke en string)
    # On va chercher la différence minimale comme int
    min_diff = None
    
    # On teste toutes les coupures possibles
    # i = position de coupe: s[:i], s[i:]
    # i doit être de 1 à n-1 pour avoir au moins deux segments
    for i in range(1, n):
        left = s[:i]
        right = s[i:]
        
        # Comparer les deux segments
        cmp = compare_num_str(left, right)
        if cmp >= 0:
            diff_str = subtract_num_str(left, right)
        else:
            diff_str = subtract_num_str(right, left)
        
        # Convertir diff_str en entier (attention, peut être long mais diff sert à comparer)
        # diff_str sera au maximum la longueur de s (100000 chiffres) donc int conversion classique peut prendre du temps
        # Pour plus performant on peut comparer longueur directement et sinon convertir en int en dernière étape seulement
        # Ici on fait safe conversion car la différence peut être assez grand mais Python gère les grands entiers
        
        diff_int = int(diff_str)
        if min_diff is None or diff_int < min_diff:
            min_diff = diff_int
            
        # Optimisation rapide : si différence est 0, c'est minimal possible
        if min_diff == 0:
            break
    
    print(min_diff)

if __name__ == "__main__":
    main()