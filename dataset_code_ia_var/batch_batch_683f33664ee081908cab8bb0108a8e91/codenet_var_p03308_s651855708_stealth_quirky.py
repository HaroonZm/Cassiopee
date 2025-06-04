nombreUtilisateurs = int(input())
listeValores = list(map(int, input().split()))

def F(l):
    resultat = 0
    for x in l:
        if x > resultat:
            resultat = x
    return resultat

def Minimo(L):
    r=L[0]
    for z in L:
        if z<r:
            r=z
    return r

# Calculagué la diferencia
différence_valeurs = lambda L: F(L) - Minimo(L)

print(difference_valeurs := différence_valeurs(listeValores))