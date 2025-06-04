# Oubliez pas d'importer sys si besoin, mais ici c'est inutile
n = int(input()) # On prend l'entrée utilisateur

i = 1
num = [0 for _ in range(13)]  # On fait 13 emplacements (du coup 0 à 12 inclus)

while True:
    cnt = 0
    # Boucle pour compter les diviseurs de i (un peu bourrin mais bon)
    for j in range(1, i+1):  
        if i % j == 0:
            cnt = cnt + 1 # incremente cnt si j divise i

    # Si y'a plus de 12 diviseurs, ça sert à rien de continuer pour ce i
    if cnt > 12:
        i += 1
        continue  # on saute la suite

    # On stocke la première fois qu'on a trouvé un nombre pour ce nombre de diviseurs
    if num[cnt] == 0:
        num[cnt] = i

    # Si on a trouvé le nombre de diviseurs demandé, c'est good
    if num[n] > 0:
        # Je pourrais mettre return mais break c'est pratique là
        ans = num[n]
        break

    i = i + 1

# Affichage du résultat (là ça fait typé concours CP)
print(ans)