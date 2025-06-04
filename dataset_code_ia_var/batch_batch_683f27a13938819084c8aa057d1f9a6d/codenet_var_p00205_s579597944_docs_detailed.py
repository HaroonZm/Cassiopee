def read_hand():
    """
    Lit 5 entiers depuis l'entrée standard pour représenter une main.
    Le premier entier est lu avant la boucle principale pour permettre une sortie anticipée.
    Retourne :
        list[int]: Une liste de 5 entiers représentant une main.
    Renvoie None si l'utilisateur entre 0 (signal d'arrêt).
    """
    hands = []
    # Lire le premier entier de la main
    h = int(input())
    if h == 0:
        return None
    hands.append(h)
    # Lire les quatre entiers restants
    for _ in range(4):
        h = int(input())
        hands.append(h)
    return hands

def process_hand(hands):
    """
    Traite une main de 5 cartes selon des règles spécifiques et affiche des sorties.
    - Si la main ne contient pas exactement deux valeurs distinctes, imprime 3 pour chaque carte.
    - Si la main contient 1 et 2, imprime 1 là où c'est 1, sinon 2.
    - Si la main contient 1 et 3, imprime 2 là où c'est 1, sinon 1.
    - Sinon, imprime 1 là où c'est 2, sinon 2.
    Args:
        hands (list[int]): Une liste de 5 entiers représentant une main.
    """
    # Obtenir les valeurs distinctes de la main
    h_uni = list(set(hands))
    # Si la main n'a pas exactement deux valeurs distinctes
    if len(h_uni) != 2:
        for _ in range(5):
            print(3)
        return
    # Trier les valeurs uniques pour simplifier les comparaisons
    h_uni.sort()
    # Cas où les valeurs sont 1 et 2
    if h_uni[0] == 1 and h_uni[1] == 2:
        for h in hands:
            if h == 1:
                print(1)
            else:
                print(2)
    # Cas où les valeurs sont 1 et 3
    elif h_uni[0] == 1 and h_uni[1] == 3:
        for h in hands:
            if h == 1:
                print(2)
            else:
                print(1)
    # Tous les autres cas (forcément 2 et 3)
    else:
        for h in hands:
            if h == 2:
                print(1)
            else:
                print(2)

def main():
    """
    Boucle principale du programme.
    Lit des mains à l'utilisateur et les traite jusqu'à ce que le signal d'arrêt (0) soit reçu.
    """
    while True:
        # Lire une main de 5 cartes.
        hands = read_hand()
        # Si l'utilisateur entre 0, la boucle s'arrête.
        if hands is None:
            break
        # Appliquer le traitement aux cartes.
        process_hand(hands)

if __name__ == "__main__":
    main()