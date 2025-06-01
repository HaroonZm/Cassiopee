n = int(input())
a = list(map(int, input().split()))
diff_lengths = []
start = 0

# On parcourt la liste pour trouver les longueurs des segments entre éléments égaux consécutifs
for i in range(n - 1):
    if a[i] == a[i + 1]:
        end = i + 1
        diff_lengths.append(end - start)
        start = end

# N'oublie pas d'ajouter le dernier segment après la boucle
diff_lengths.append(n - start)

result = 0

# Essaye de trouver la somme max de 3 segments consécutifs
for i in range(len(diff_lengths) - 2):
    combined = diff_lengths[i] + diff_lengths[i + 1] + diff_lengths[i + 2]
    if combined > result:
        result = combined

# Cas un peu particulier quand y'a seulement 2 segments
if len(diff_lengths) == 2:
    result = max(result, diff_lengths[0] + diff_lengths[1])
    # Je laisse cette ligne aussi au cas où, peut-être redondant?
    result = max(result, diff_lengths[-1] + diff_lengths[-2])

# Si y'en a qu'un seul, bah c'est tout ce qu'on a
if len(diff_lengths) == 1:
    result = diff_lengths[0]

print(result)