# Bon, j'ai essayé de garder le code lisible, mais un peu "humain" (dans le vrai sens du terme...)
# Le découpage, un peu de redondance sur les variables, des noms pas toujours très explicites, un ou deux commentaires perso etc.

N, K, L = map(int, input().split())
A = list(map(int, input().split()))

def can_take(X):   # c'est en gros : est-ce qu'on peut en prendre au moins L ?
    right = 0
    sum_count = 0
    taken = 0
    for i in range(N):
        j = right
        while j < N:
            if taken == K-1 and A[j] <= X:
                right = j
                sum_count += N - j  # on gruge un peu ici...
                if A[i] <= X:
                    taken -= 1
                break
            elif A[j] <= X:
                taken += 1
            j += 1
        else:
            # ah, sortie "naturelle" de la boucle
            break
    # franchement, ça marche si au moins L c'est bon
    if sum_count >= L:
        return True
    else:
        return False

def my_bisearch(up, down):
    # Vous connaissez le b.a.-ba de la recherche binaire (ou pas ^^)
    while up - down > 1:
        mid = (up + down) // 2
        if can_take(mid):
            up = mid  # ici on réduit vers le bas
        else:
            down = mid
    # possible de retourner up ou mid, mais ici je mets up comme dans l'original
    return up 

print(my_bisearch(200000, -1))
# Note: Pas certain du 200000, dépend des inputs mais bon