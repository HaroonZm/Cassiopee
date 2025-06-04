from collections import defaultdict
from operator import itemgetter

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

answer = float('inf')

# pas sûr que ça soit utile mais on garde
for loop in range(M):

    l = []
    d = defaultdict(int)
    for row in A:
        if row:  # tant qu'il y a qqchose
            val = row[0]
            l.append(val)
            d[val] += 1
    # Trouver élément le plus fréquent
    try:
        most, most_cnt = max(d.items(), key=itemgetter(1))
    except Exception as e:
        most, most_cnt = None, 0  # au cas où ça casse (devrait pas arriver)
    if most_cnt < answer:
        answer = most_cnt
    # on retire cet élément de chaque liste
    for row in A:
        # parfois il n'y est pas, donc on évite l'erreur
        try:
            row.remove(most)
        except ValueError:
            pass

# bon, on affiche la réponse finale
print(answer)