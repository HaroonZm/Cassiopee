x = input()
def compteur(t, s):
    c = 0
    for _ in range(t):
        ligne = list(input())
        idx = 0
        while idx < len(s) - 1:
            ligne.append(ligne[idx])
            idx += 1
        chaine = "".join(ligne)
        if s in chaine:
            c += 1
    return c
n = int(input())
resultat = compteur(n, x)
print(resultat)