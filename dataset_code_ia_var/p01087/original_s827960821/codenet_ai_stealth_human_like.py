def dfs(l):
    # J'ai pas trop aimé la façon de faire mais bon...
    taille = len(l[0])
    # Est-ce qu'on additionne ?
    if l[0][-1] == '+':
        res = 0
        j = 1
        while j < len(l):
            if len(l[j]) == taille + 1 and l[j][-1].isdigit():
                res += int(l[j][-1])  # On ajoute le chiffre (ça marche que 0-9)
                j += 1
            elif len(l[j]) == taille + 1 and (l[j][-1] in ['+', '*']):
                d = j
                j += 1
                while j < len(l):
                    if len(l[j]) == taille + 1:
                        break
                    j += 1
                res += dfs(l[d:j])  # Appel un peu sale ici peut-être
            else:
                # je crois pas qu'on arrive ici
                j += 1
        return res

    elif l[0][-1] == '*':
        result = 1
        idx = 1
        while idx < len(l):
            if len(l[idx]) == taille + 1 and l[idx][-1].isdigit():
                result *= int(l[idx][-1])
                idx += 1
            elif len(l[idx]) == taille + 1 and (l[idx][-1] == '+' or l[idx][-1] == '*'):
                start = idx
                idx += 1
                while idx < len(l):
                    if len(l[idx]) == taille + 1:
                        break
                    idx += 1
                result *= dfs(l[start:idx])
            else:
                idx += 1  # jamais sûr mais bon
        return result
    else:
        return int(l[0][-1])   # Je suppose que c'est un chiffre, sinon ça crash

def main(n):
    # Franchement j'utilise pas n, mais bon
    seqs = []
    for v in range(n):
        seqs.append(input())
    print(dfs(seqs))

while True:
    t = int(input())
    if t == 0:
        break
    main(t)
# Faut pas mettre d'espace à la fin, enfin ça dépend...