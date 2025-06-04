# Programme pour calculer le nombre de changements de main lors de la frappe d'une chaîne en QWERTY
# L'idée est de déterminer pour chaque caractère s'il est tapé avec la main gauche ou droite,
# puis de compter le nombre de fois où la main utilisée change par rapport au caractère précédent.

def main():
    # Définition des ensembles de caractères tapés à la main gauche et droite en QWERTY
    left_hand = set('qwertasdfgzxcvb')
    right_hand = set('yuiophjklnm')

    while True:
        s = input().strip()
        if s == '#':
            break

        # initialisation d'une variable pour suivre la main utilisée
        prev_hand = None
        switch_count = 0

        for ch in s:
            # déterminer la main utilisée pour ce caractère
            if ch in left_hand:
                current_hand = 'L'
            elif ch in right_hand:
                current_hand = 'R'
            else:
                # le problème garantit que l'entrée est composée uniquement de minuscules alphabétiques,
                # cet else ne devrait donc jamais arriver
                current_hand = None

            # si ce n'est pas le premier caractère,
            # comparer avec la main précédente pour détecter un changement
            if prev_hand is not None and current_hand != prev_hand:
                switch_count += 1

            prev_hand = current_hand

        print(switch_count)

if __name__ == "__main__":
    main()