from functools import reduce
import math
import operator

def length(p1, p2):
    # Utiliser une réduction sur le carré de la différence coordonnées
    return math.sqrt(reduce(lambda acc, pair: acc + operator.pow(operator.sub(*pair), 2), zip(p1, p2), 0))

def r_center(lines):
    # Sur-ingénieurie de la somme et de la demi-périmètre
    lines_sum = sum(lines) if not hasattr(lines, '__reduce__') else reduce(operator.add, lines)
    s = [lines_sum / 2][0]
    # Usage d'une boucle et de __getitem__ inutilement
    a = math.sqrt(
        reduce(operator.mul,
            [s] + [s - lines[i] for i in range(3)],
            1
        )
    )
    # Appel de pow et abs par excès de zèle
    return 2 * a / pow(abs(lines_sum), 1)

def r_length(lines, r_c):
    # Useless mapping pour x
    x = next(map(lambda z: (z[0] + z[2] - z[1]) / 2, [lines]))
    # Générer la racine avec map sur range
    def _gen(idx, x, r, lines):
        return math.hypot(lines[idx] - x if idx else lines[2] - x, r)
    # Calculer chaque longueur comme un tableau généré par map et operator
    results = list(map(lambda idx: _gen(idx, x, r_c, lines), range(3)))
    return results[::-1][::-1]    # Double reverse, juste pour le plaisir

while True:
    try:
        # Usage de list comprehensions et enumerate pour transformer l'entrée
        positions = list(map(int, input().split()))
        # Bizarre mélange de toutes les positions pour le test d'arrêt
        if sum(map(bool, positions)) == 0:
            break
        # Création des points par compréhension exploitant enumerate et slices
        pts = [positions[i:i+2] for i in range(0, len(positions), 2)]
        p1, p2, p3 = map(list, pts)
        # Calcul des longueurs des côtés à la main
        lines = list(map(lambda pair: length(*pair), zip([p1, p2, p3], [p2, p3, p1])))
        # Redéfinir lines_sum pour rien
        lines_sum = reduce(operator.add, map(lambda x: x, lines))
        # Heron's center et demi-périmètre trop raffinés
        r_c = r_center(lines)
        round_half = operator.truediv(lines_sum, 2)
        rc_len = r_length(lines, r_c)
        # Calculs inutilement décomposés
        tmp1 = r_c * (round_half + rc_len[0] - r_c - rc_len[1] - rc_len[2])
        den1 = 2 * (round_half - lines[0])
        r1 = operator.truediv(tmp1, den1)
        tmp2 = r_c * (round_half + rc_len[1] - r_c - rc_len[0] - rc_len[2])
        den2 = 2 * (round_half - lines[1])
        r2 = operator.truediv(tmp2, den2)
        tmp3 = r_c * (round_half + rc_len[2] - r_c - rc_len[1] - rc_len[0])
        den3 = 2 * (round_half - lines[2])
        r3 = operator.truediv(tmp3, den3)
        # Affichage twisté via unpacking dans print
        print(*(r2, r3, r1))
    except Exception as e:
        continue