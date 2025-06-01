# Bon, on va faire ça un peu à l'arrache, pas super clean mais ça marche
while True:
    matrice = []
    taille = int(input())  # Lis la taille, 0 ça arrête tout
    if taille == 0:
        break
    
    for _ in range(taille):
        ligne = list(map(int, input().split()))
        matrice.append(ligne)
    
    # Duplication pour manipuler tranquille
    copie = matrice[:]
    # Transpose pour les colonnes (je crois que zip(*) fait ça)
    transposé = list(map(list, zip(*matrice)))
    
    # Ajouter la somme de chaque ligne à la fin
    for l in copie:
        l.append(sum(l))
    
    # Ajouter la somme de chaque "colonne" dans la transposée
    for l in transposé:
        l.append(sum(l))
    
    # Retour à la forme originale mais avec la dernière ligne en plus
    transposé = list(map(list, zip(*transposé)))
    
    # On ajoute la somme de la dernière ligne et une somme de ses éléments (ça fait genre un total)
    copie.append(transposé[-1] + [sum(transposé[-1])])
    
    # Affichage, un peu aligné à droite mais pas trop précis
    for ligne in copie:
        for x in ligne:
            print(str(x).rjust(5), end="")
        print()