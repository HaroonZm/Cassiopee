"""
Ce script lit une liste de cartes depuis l'entrée standard, traite chaque carte selon une séquence d'indices,
et affiche le résultat pour chaque carte. Il ignore la séquence une fois le symbole '-' rencontré.
"""

def lire_liste_cartes():
    """
    Lit les données de l'utilisateur ligne par ligne jusqu'à ce que la ligne saisie soit un tiret '-'.
    Chaque ligne peut contenir des mots ou des chiffres, séparés par des espaces.
    Construit une liste finale `cardList` contenant tous les éléments lus.
    Returns:
        list: La liste des éléments (cartes, nombres, délimiteurs) saisis.
    """
    cardList = []
    while True:
        temp = input()
        # Si l'utilisateur entre '-', on ajoute ce délimiteur puis on arrête la saisie.
        if temp == "-":
            cardList.append(temp)
            break
        # Si la ligne contient des caractères alphabétiques, on la découpe en mots.
        if any(ch.isalpha() for ch in temp):
            temp = temp.split()
        else:
            # Sinon, on prend chaque caractère séparément (utile pour les chiffres par exemple).
            temp = list(temp)
        # Ajoute les éléments de la ligne à la liste principale.
        cardList += temp
    return cardList

def traiter_cartes(cardList):
    """
    Parcourt la liste des cartes pour traiter chaque carte jusqu'au délimiteur '-'.
    Pour chaque carte (élément alphabétique), suit la logique:
      - Prend le mot
      - Récupère le nombre qui suit (nombre d'indices à traiter)
      - Pour chaque indice, effectue une opération de duplication et de troncature
  
    Args:
        cardList (list): Liste contenant mots, nombres et délimiteurs.
    """
    i = 0
    while i < len(cardList):
        # Arrête le traitement en cas de tiret '-'
        if cardList[i] == "-":
            break
        # Si l'élément actuel est alphabétique, il s'agit d'une carte à traiter
        if cardList[i].isalpha():
            editCard = cardList[i]
            # Le nombre juste après indique combien d'indices seront utilisés
            try:
                nb_indices = int(cardList[i + 1])
            except (IndexError, ValueError):
                # Passe à l'élément suivant si impossibilité de récupérer le nombre
                i += 1
                continue
            # Pour chaque indice donné, on applique la manipulation demandée
            for j in range(i + 2, i + 2 + nb_indices):
                # S'assure de ne pas dépasser la liste ou tomber sur un séparateur/lettre
                if j >= len(cardList) or cardList[j] == "-" or cardList[j].isalpha():
                    break
                indice = int(cardList[j])
                # Duplique le mot (concatène à lui-même)
                editCard = editCard + editCard
                # Tronque cette duplication depuis la position 'indice' sur la longueur initiale
                editCard = editCard[indice:indice + len(cardList[i])]
            print("{0}".format(editCard))
            # Passe au mot suivant (la carte + nb_indices + les indices)
            i += nb_indices + 2
        else:
            # Passe à l'élément suivant si ce n'est pas une carte
            i += 1

def main():
    """
    Point d'entrée principal du programme.
    Lit et traite la liste des cartes, puis affiche le résultat.
    """
    cardList = lire_liste_cartes()
    traiter_cartes(cardList)

if __name__ == "__main__":
    main()