nombre_entiers = int(input())

liste_entiers = list(map(int, input().split()))

somme_totale = sum(liste_entiers)

if somme_totale % 2 == 0:
    
    resultat = somme_totale // 2
    print(resultat)

else:
    
    liste_entiers.sort()
    
    plus_petit_entier_impair = None
    
    for entier in liste_entiers:
        if entier % 2 == 1:
            plus_petit_entier_impair = entier
            break

    resultat = (somme_totale - plus_petit_entier_impair) // 2
    print(resultat)