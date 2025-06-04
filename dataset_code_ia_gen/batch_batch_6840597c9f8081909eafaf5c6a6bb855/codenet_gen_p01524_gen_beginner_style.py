N = int(input())
a = []
for _ in range(N):
    a.append(input())

# On choisit toujours la main 1 (index 1)
# C'est une stratégie simple et directe

for _ in range(1000):
    print(1)
    # On fait flush automatiquement avec print en Python 3
    j_hand = int(input())
    # On ne fait rien avec j_hand, on répète la main 1 à chaque fois