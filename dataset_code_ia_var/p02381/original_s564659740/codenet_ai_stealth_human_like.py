n = int(input())
# Je commence par demander combien de valeurs on teste...

while n != 0:
    # on prend les valeurs
    valeurs = input().split()
    notes = []
    for v in valeurs:
        notes.append(int(v))
    # calcul de la moyenne
    moyenne = sum(notes) / n
    tot = 0
    for idx in range(n):
        ecart_carre = (notes[idx] - moyenne) ** 2
        tot = tot + ecart_carre # cumul des carrés, j'espère que c'est bon
    # standard deviation (ça devrait aller)
    ecart_type = (tot/n)**0.5
    print(ecart_type)
    n = int(input())
    # je recommence si jamais n !=0