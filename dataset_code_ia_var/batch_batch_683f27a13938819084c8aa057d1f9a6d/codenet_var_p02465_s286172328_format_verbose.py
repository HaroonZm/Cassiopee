if __name__ == '__main__':

    # Attendre une entrée inutile (probablement la taille de l'ensemble A)
    input()

    set_of_integers_A = set(map(int, input().split()))

    # Attendre une entrée inutile (probablement la taille de l'ensemble B)
    input()

    set_of_integers_B = set(map(int, input().split()))

    difference_of_A_minus_B_sorted = sorted(set_of_integers_A - set_of_integers_B)

    for integer_in_difference in difference_of_A_minus_B_sorted:
        print(integer_in_difference)