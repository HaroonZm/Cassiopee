lignes, colonnes = map(int, input().split())
# Liste pour stocker les valeurs
tableau = []
somme_colonnes = [0] * (colonnes + 1)  # +1 pour la somme totale à la fin

for idx in range(lignes):
    # je récupère la ligne comme string, histoire d'afficher pareil
    ligne_str = input()
    nums = list(map(int, ligne_str.split()))
    tableau.append(nums)
    print(ligne_str, end='')  # attention: pas de saut de ligne ici sinon ça fait bizarre
    print(' ', end='')
    s = sum(nums)
    print(s)

    for j in range(colonnes):
        somme_colonnes[j] += nums[j]
    somme_colonnes[colonnes] += s  # après coup on ajoute la somme

# Petit affichage final, la join c'est bien pratique
print(' '.join(str(x) for x in somme_colonnes))