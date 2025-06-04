# Demande à l'utilisateur de saisir une valeur entière qui sera affectée à la variable n.
# n représente généralement le nombre d'éléments dans la moitié du paquet de cartes.
n = int(input())

# Demande à l'utilisateur de saisir une deuxième valeur entière à stocker dans m.
# m correspond au nombre d'opérations à réaliser sur le paquet de cartes.
m = int(input())

# Crée une liste appelée 'card' qui va contenir les cartes numérotées de 1 à 2*n inclus.
# Utilise la fonction range qui génère les valeurs de 1 à (2*n+1), car la borne supérieure n'est pas incluse.
# La fonction list transforme l'objet range en une véritable liste Python.
card = list(range(1, 2*n + 1))

# Exécute la boucle for exactement m fois, car nous devons réaliser m opérations au total.
for _ in range(m):
    # Pour chaque itération, demande à l'utilisateur d'entrer un entier correspondant à l'opération à effectuer.
    ope = int(input())

    # Si l'entier entré est 0, on effectue un entrelacement parfait (shuffle parfait) du paquet.
    if ope == 0:
        # Division de la liste 'card' en deux parties égales appelées card1 et card2.
        # card1 contient les n premiers éléments (indices de 0 à n-1).
        card1 = card[:n]
        # card2 contient les n derniers éléments (indices de n à 2*n-1).
        card2 = card[n:]
        # On initialise une liste vide pour reconstruire notre paquet après le mélange.
        card = []
        # zip parcourt les deux listes 'card1' et 'card2' simultanément.
        # À chaque itération, c1 prend la valeur d'une carte de card1 et c2 celle de card2 à la même position relative.
        for c1, c2 in zip(card1, card2):
            # On ajoute une carte de la première moitié.
            card.append(c1)
            # Puis la carte correspondante de la deuxième moitié.
            card.append(c2)
    # Si ope n'est pas égal à 0, alors on effectue une coupe du paquet à l'indice 'ope'.
    else:
        # card1 contient les cartes du début du paquet jusqu'à l'indice 'ope' (non inclus).
        card1 = card[:ope]
        # card2 contient le reste du paquet à partir de l'indice 'ope' jusqu'à la fin.
        card2 = card[ope:]
        # On prépare une nouvelle liste vide pour recueillir le paquet après la coupe.
        card = []
        # On ajoute d'abord toutes les cartes de 'card2' (celles après l'indice 'ope').
        card.extend(card2)
        # Puis celles de 'card1' (celles avant l'indice 'ope') pour terminer le mélange.

        card.extend(card1)

# Après toutes les opérations, on affiche chaque carte du paquet final.
# La boucle for parcourt chaque élément de la liste 'card', qui correspondent à des entiers.
for c in card:
    # Affiche la valeur de chaque carte sur une nouvelle ligne.
    print(c)