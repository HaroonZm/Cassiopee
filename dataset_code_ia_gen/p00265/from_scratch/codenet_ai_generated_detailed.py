import sys
import bisect

input = sys.stdin.readline

# Lecture des paramètres N (nombre de cartes) et Q (nombre de questions)
N, Q = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort()  # On trie les cartes pour permettre des recherches efficaces

max_card = cards[-1]  # La plus grande valeur parmi les cartes

for _ in range(Q):
    q = int(input())
    if q > max_card:
        # Si q est plus grand que la plus grande carte,
        # le plus grand reste possible est simplement max_card (puisque max_card % q = max_card)
        print(max_card)
        continue

    ans = 0
    # On va parcourir les multiples de q jusqu'à max_card
    # ds les intervalles [start, end), on cherche le plus grand élément < end dans cards
    start = 0
    while start <= max_card:
        end = start + q
        # Recherche de la position d'insertion de end dans la liste triée cards
        index = bisect.bisect_left(cards, end)
        # On regarde la valeur immédiatement avant index si elle appartient à l'intervalle [start, end-1]
        if index > 0 and cards[index -1] >= start:
            remainder = cards[index -1] % q
            if remainder > ans:
                ans = remainder
        start += q

    print(ans)