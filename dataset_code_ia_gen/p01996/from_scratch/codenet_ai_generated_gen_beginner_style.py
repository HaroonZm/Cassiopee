N, M = map(int, input().split())
A = list(map(int, input().split()))

count = 0

while True:
    # Vérifier si les sièges 1 à M sont occupés
    # Pour cela, on vérifie que pour chaque i de 1 à M, i est dans A
    flag = True
    for i in range(1, M + 1):
        if i not in A:
            flag = False
            break
    if flag:
        break
    
    # Trouver la position la plus grande occupée (le dernier élève)
    last_seat = max(A)
    # Trouver le premier siège vide
    for seat in range(1, N + 1):
        if seat not in A:
            first_empty = seat
            break
    
    # Déplacer l'élève le plus en arrière vers le premier siège vide le plus avant
    idx = A.index(last_seat)
    A[idx] = first_empty
    A.sort()
    count += 1

print(count)