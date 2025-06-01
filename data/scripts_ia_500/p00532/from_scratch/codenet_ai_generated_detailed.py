# Lecture des entrées
N = int(input())  # nombre d'amis
M = int(input())  # nombre de parties jouées
A = list(map(int, input().split()))  # cible pour chaque partie

# Initialiser un tableau pour stocker les points cumulés de chaque ami (1-based indexing)
points = [0] * (N + 1)

# Parcourir chaque partie
for i in range(M):
    guesses = list(map(int, input().split()))  # prédictions de chaque ami pour la partie i
    target = A[i]  # le cible de cette partie

    correct_count = 0  # nombre d'amis ayant deviné juste (dont la cible elle-même)
    # On calcule pour chaque ami s'il a deviné juste
    for j in range(N):
        if guesses[j] == target:
            correct_count += 1
            points[j + 1] += 1  # chaque bonne réponse rapporte 1 point

    # Le nombre d'amis qui ont mal deviné
    wrong_count = N - correct_count

    # La cible gagne des points supplémentaires égaux au nombre d'amis qui ont mal deviné
    points[target] += wrong_count

# Affichage des résultats (sans l'indice 0)
for j in range(1, N + 1):
    print(points[j])