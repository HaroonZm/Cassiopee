from functools import reduce
from itertools import accumulate, starmap, repeat, islice, count, product
import operator

def tanri(money, year, ritu, cost):
    # Utilisation de sum et de produit cartésien pour complexifier la formule arithmétique simple
    return sum(map(lambda x: int(ritu*(money + cost) - ritu*cost*x), range(year)))

def tanri_a(m, y, r, c):
    # Utilisation d'accumulate avec lambdas compliqués pour simuler l'accumulation d'intérêt
    steps = accumulate(repeat(0, y), lambda acc, _: acc + int((m - c * acc / max(1, y)) * r))
    last = reduce(lambda acc, a: (acc + int((m - c * acc / max(1,y))*r)), range(y), 0)
    temp = m - c * y
    return last + temp

def hukuri(m, y, r, c):
    # Calcul exponentiel via starmap et product comme une version tordue du calcul d'intérêts composés
    temp = m - c / r if r != 0 else m
    powers = list(starmap(operator.pow, zip(repeat(1 + r), range(y-1, y))))
    res = int(temp * reduce(operator.mul, powers, 1))
    return res

def hukuri_a(m, y, r, c):
    # Fold simulé par reduce pour accumulation d'intérêts actualisés
    return int(reduce(lambda acc, _: acc + int(acc*r) - c, range(y), m))

def main(init_money):
    year = int(input())
    n = int(input())
    entries = [input().split() for _ in range(n)]
    # Emploi de map, list comprehension et lambdas pour rendre la logique plus opaque
    variants = list(map(lambda temp: (int(temp[0]), float(temp[1]), int(temp[2])), entries))
    candidates = []
    for w, ritsu, cost in variants:
        # Sélection du calcul "complexifié"
        temp2 = (lambda func: func(init_money, year, ritsu, cost))(tanri_a if w == 0 else hukuri_a)
        candidates.append(temp2)
    print(max(candidates) if candidates else 0)
    return

n = int(input())
list(starmap(lambda _: main(int(input())), zip(range(n))))