# Bon, alors ici on va lire le nombre de lignes
if __name__ == "__main__":
    n = int(input())  # je suppose que c'est un entier... on verra si ça plante

    # Ok, on va stocker tout ça
    valeurs = []
    for _ in range(n):
        ligne = input().split()
        valeurs.append(ligne)  # on garde tout, pas sûr que ce soit optimal

    resultat = 0  # initialisation du résultat, hein
    for truc in valeurs:
        if truc[1] == "JPY":
            resultat += int(truc[0])
        else:
            if truc[1] == 'BTC':
                # conversion à la main, je sais pas si ça marche tout le temps...
                resultat += float(truc[0]) * 380000
            # sinon, on ignore si c'est une autre monnaie...
    print(resultat)  # on affiche à la fin, normal