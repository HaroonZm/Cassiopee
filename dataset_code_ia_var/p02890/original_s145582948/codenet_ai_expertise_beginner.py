n = int(input())
a_list = list(map(int, input().split()))

# Préparation des listes pour compter les nombres de chaque carte
count_cards = [0] * (n + 1)
how_many_has_that_count = [0] * (n + 1)

for num in a_list:
    count_cards[num] += 1

for i in range(1, n + 1):
    c = count_cards[i]
    if c > 0:
        how_many_has_that_count[c] += 1

# Calcul de la somme cumulative S[x] et f[x]
S = [0] * (n + 2)  # un peu plus grand pour éviter les erreurs d'indice
f = [0] * (n + 2)
for x in range(1, n + 1):
    S[x] = S[x - 1] + how_many_has_that_count[x]
    if x > 0:
        f[x] = S[x] // x

# Recherche du maximum pour chaque K
answers = []
max_possible = n
for k in range(1, n + 1):
    a = max_possible
    while a > 0:
        if f[a] >= k:
            break
        a -= 1
    answers.append(a)
    max_possible = a  # pour la prochaine recherche, partir d'ici

for ans in answers:
    print(ans)