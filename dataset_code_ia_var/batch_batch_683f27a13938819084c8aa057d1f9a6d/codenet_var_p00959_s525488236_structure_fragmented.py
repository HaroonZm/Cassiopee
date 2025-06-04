def lire_entrees():
    return map(int, input().split())

def initialiser_variables():
    return 0, 0, 0

def lire_hauteur():
    return int(input())

def maj_s(s, x):
    return s + x

def maj_x(h):
    return h

def maj_y(h, y):
    return max(h, y)

def calculer_resultat(t, x, s, y):
    valeur = (t - x - s) // y + 2
    return max(valeur, 1)

def afficher_resultat(res):
    print(res)

def boucle(n, t, s, x, y):
    for _ in range(n):
        h = lire_hauteur()
        s_temp = maj_s(s, x)
        x_temp = maj_x(h)
        y_temp = maj_y(h, y)
        res = calculer_resultat(t, x_temp, s_temp, y_temp)
        afficher_resultat(res)
        s, x, y = s_temp, x_temp, y_temp

def main():
    n, t = lire_entrees()
    s, x, y = initialiser_variables()
    boucle(n, t, s, x, y)

main()