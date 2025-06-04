from collections import deque
import heapq

N = int(input())
pile = [4, 7]
heapq.heapify(pile)
vu = set(pile)

def traiter(n):
    if n > N:
        print('No')
        return True
    if n == N:
        print('Yes')
        return True
    return False

while True:
    x = heapq.heappop(pile)
    if traiter(x):
        break
    for d in (4, 7):
        nxt = x + d
        if nxt not in vu:
            pile.append(nxt) if isinstance(pile, list) else heapq.heappush(pile, nxt)
            heapq.heapify(pile)
            vu.add(nxt)