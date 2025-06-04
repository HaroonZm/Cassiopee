import string
from heapq import heapify, heappop, heappush
from collections import Counter

STR = string.ascii_letters + string.digits

# Utilisation d'un comprehension et Counter pour compter les caractères efficacement
def get_char_counts():
    counts = {}
    # Parallélisme natif non applicable ici car chaque requête dépend d'une entrée utilisateur
    for c in STR:
        print(f'? {c * 128}')
        a = int(input())
        if a < 128:
            counts[c] = 128 - a
    return counts

def optimal_merge(counter):
    # Priorité sur le plus petit nombre de caractères pour minimiser les comparaisons
    heap = [(cnt, [c] * cnt) for c, cnt in counter.items()]
    heapify(heap)
    total_length = sum(counter.values())
    while len(heap) > 1:
        l1, t1 = heappop(heap)
        l2, t2 = heappop(heap)
        # Combine intelligemment avec les deux pointeurs, structure plus claire
        i, j = 0, 0
        while i < len(t1) and j < l2:
            t1.insert(i, t2[j])
            s = ''.join(t1)
            print(f'? {s}')
            a = int(input())
            # Avantage: on ne pop que si la distance s'accroît, sinon on incrémente j
            if len(t1) > total_length - a:
                t1.pop(i)
            else:
                j += 1
            i += 1
        # Ajout de la fin restante si incomplète
        if j < len(t2):
            t1.extend(t2[j:])
        heappush(heap, (l1 + l2, t1))
    return ''.join(heap[0][1])

if __name__ == '__main__':
    char_counts = get_char_counts()
    result = optimal_merge(char_counts)
    print(f'! {result}')