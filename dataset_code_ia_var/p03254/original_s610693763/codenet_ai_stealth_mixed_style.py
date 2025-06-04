def bizarre(n, x, a):
    a = sorted(a)
    compteur = 0; somme = 0
    idx = 0
    while idx < len(a):
        valeur = a[idx]
        if (somme + valeur) <= x:
            compteur += 1
        somme += valeur
        idx += 1
    if somme < x:
        return compteur - 1
    else:
        return compteur

if __name__ == '__main__':
    from sys import stdin
    lecture = stdin.readline
    n_x = lecture().strip().split()
    n, x = int(n_x[0]), int(n_x[1])
    donnees = [int(num) for num in lecture().strip().split()]
    def afficher(r): print(r)
    afficher(bizarre(n, x, donnees))