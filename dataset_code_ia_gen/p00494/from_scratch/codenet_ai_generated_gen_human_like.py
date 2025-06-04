S = input().rstrip()

max_k = 0
N = len(S)

# On parcourt la chaîne pour chercher le plus grand k possible
# où S contient JJ...J OO...O II...I (k fois chacun)
i = 0
while i < N:
    # Chercher une séquence de J consécutifs à partir de i
    if S[i] != 'J':
        i += 1
        continue
    count_j = 0
    while i + count_j < N and S[i + count_j] == 'J':
        count_j += 1

    # Ensuite, vérifier s'il y a au moins count_j O consécutifs juste après
    start_o = i + count_j
    count_o = 0
    while start_o + count_o < N and S[start_o + count_o] == 'O' and count_o < count_j:
        count_o += 1

    if count_o < count_j:
        i += 1
        continue

    # Ensuite, vérifier s'il y a au moins count_j I consécutifs juste après
    start_i = start_o + count_o
    count_i = 0
    while start_i + count_i < N and S[start_i + count_i] == 'I' and count_i < count_j:
        count_i += 1

    if count_i < count_j:
        i += 1
        continue

    # Le niveau k possible est limité par le minimum des trois compteurs
    k = min(count_j, count_o, count_i)
    if k > max_k:
        max_k = k

    # On avance d'au moins 1 pour ne pas boucler indéfiniment
    i += 1

print(max_k)