from collections import Counter

def point(lst):
    """
    Calcule la valeur totale d'une main de cartes selon des règles spécifiques.

    Arguments :
    lst -- liste d'entiers représentant les cartes. Les valeurs sont de 1 à 13,
           où 1 représente l'as, 2-9 représentent les cartes numériques, et
           10-13 représentent les figures (valant toutes 10 points).

    Retour :
    Un entier représentant la valeur totale de la main. Si la somme dépasse 21,
    la fonction retourne 0 (indiquant une main perdante).

    Détails de calcul :
    - Les cartes de 2 à 9 valent leur valeur numérique.
    - Les cartes de 10 à 13 valent 10 points chacune.
    - Les as (valeur 1) peuvent valoir soit 1 point soit 11 points, pour optimiser
      la valeur totale sans dépasser 21.
    """

    # Compte le nombre d'occurrences de chaque carte dans la liste
    counter = Counter(lst)

    # Accumulateur pour la somme des valeurs des cartes hors as
    acc = 0

    # Addition des cartes de 2 à 9 -> valeur = valeur de la carte * nombre d'occurrences
    for i in range(2, 10):
        acc += i * counter[i]

    # Addition des cartes de 10 à 13 -> chaque carte vaut 10 points
    for i in range(10, 14):
        acc += 10 * counter[i]

    # Nombre d'as dans la main
    one_num = counter[1]

    # Détermination de la meilleure valeur pour les as (1 ou 11)
    # On essaie toutes les combinaisons possibles d'as valant 1 ou 11
    for i in range(one_num + 1):
        # i est le nombre d'as valant 1, (one_num - i) valant 11
        if i + (one_num - i) * 11 + acc <= 21:
            acc += i + (one_num - i) * 11
            break
    else:
        # Si aucune combinaison n'est <= 21, on ajoute simplement tous les as en valeur 1
        acc += one_num

    # Si la somme dépasse 21, retourne 0 indiquant une main perdante
    if acc > 21:
        return 0
    else:
        return acc

# Boucle principale d'entrée/sortie
while True:
    s = input()  # Lecture d'une ligne d'entrée représentant les cartes

    if s == "0":
        # Si l'entrée est "0", on arrête la boucle et termine le programme
        break

    # Conversion de la chaîne d'entrée en liste d'entiers représentant les cartes
    lst = list(map(int, s.split()))

    # Affichage du résultat du calcul de points pour la main donnée
    print(point(lst))