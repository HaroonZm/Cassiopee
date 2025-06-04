N = int(input())
d = []
for _ in range(N):
    d.append(int(input()))

positions = [i * 10 for i in range(N)]

# Fonction pour vérifier si on peut aller de left à right en sautant uniquement vers l'avant
def can_go_forward():
    current = 0
    while current < N - 1:
        jumped = False
        # On cherche un trampoline à sauter vers la droite
        for next_tramp in range(current + 1, N):
            dist = positions[next_tramp] - positions[current]
            if dist <= d[current]:
                current = next_tramp
                jumped = True
                break
        if not jumped:
            return False
    return True

# Fonction pour vérifier si on peut revenir de right à left en sautant uniquement vers l'arrière
def can_go_back():
    current = N - 1
    while current > 0:
        jumped = False
        # On cherche un trampoline à sauter vers la gauche
        for prev_tramp in range(current - 1, -1, -1):
            dist = positions[current] - positions[prev_tramp]
            if dist <= d[current]:
                current = prev_tramp
                jumped = True
                break
        if not jumped:
            return False
    return True

if can_go_forward() and can_go_back():
    print("yes")
else:
    print("no")