import sys
sys.setrecursionlimit(10**7)

def partition(A, p, r):
    x = A[r][1]
    i = p - 1
    for j in range(p, r):
        if A[j][1] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

n = int(sys.stdin.readline())
cards = [tuple(sys.stdin.readline().split()) for _ in range(n)]
cards = [(suit, int(num), i) for i, (suit, num) in enumerate(cards)]

sorted_cards = sorted(cards, key=lambda x: x[1])
cards_qs = cards[:]
quicksort(cards_qs, 0, n - 1)

stable = all(sc[0] == qc[0] and sc[1] == qc[1] and sc[2] == qc[2] for sc, qc in zip(sorted_cards, cards_qs))
print("Stable" if stable else "Not stable")
for suit, num, _ in cards_qs:
    print(suit, num)