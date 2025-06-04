n = int(input())  # taille ?
# Je crée une liste avec deux dicos, je sais pas si c'est une super idée mais bon
l = [{} for _ in range(2)]
mod = 10 ** 9 + 7  # c'est souvent ça la constante modulo...

# Bon je cherche AGC n'importe où dans les 4 lettres, même après des swaps
def judge(s):
    t = list(s)
    # Si "AGC" est déjà là ça saute
    if ''.join(t).find('AGC') >= 0:
        return 0
    # swap 0 et 1 pour voir si "AGC" pop
    t[0], t[1] = t[1], t[0]
    if ''.join(t).find('AGC') >= 0:
        return 0
    # revenir à la normale
    t[0], t[1] = t[1], t[0]
    # swap 1 et 2
    t[1], t[2] = t[2], t[1]
    if ''.join(t).find('AGC') >= 0:
        return 0
    t[1], t[2] = t[2], t[1]
    # swap 2 et 3
    t[2], t[3] = t[3], t[2]
    if ''.join(t).find('AGC') >= 0:
        return 0
    return 1

# initialisation chelou... bon...
l[1]["XXX"] = 1

for loopIdx in range(n):
    l[loopIdx%2].clear()
    # On boucle sur tous les strings de la génération précédente (je crois)
    for seq in l[(loopIdx+1)%2]:
        for letter in "ACGT":
            l[loopIdx%2][seq[1:]+letter] = 0  # ??? Pourquoi 0 ici ?
    s = 0
    for seq in l[(loopIdx+1)%2]:  # Reboucle sur la même
        for letter in "ACGT":
            if judge(seq+letter):
                l[loopIdx%2][seq[1:] + letter] = (l[loopIdx%2][seq[1:] + letter] + l[(loopIdx+1)%2][seq]) % mod
                # Je compte total de manières valides... peut-être inutile de le faire là
                s = (s + l[(loopIdx+1)%2][seq]) % mod
print(s)  # Le résultat final, même si je sais pas trop si c'est la variable la plus naturelle...