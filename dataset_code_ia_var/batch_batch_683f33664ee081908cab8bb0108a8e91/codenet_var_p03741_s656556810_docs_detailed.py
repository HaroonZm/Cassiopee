import sys

def solve():
    """
    Lit la taille de la séquence et la séquence elle-même à partir de l'entrée standard.
    Calcule le nombre minimal de modifications à effectuer sur les éléments de la séquence
    pour obtenir une séquence où la somme partielle à chaque étape change de signe à chaque fois
    (autrement dit, les préfixes alternent entre positif et négatif). Deux cas sont considérés :
    - Le premier cas commence avec une somme positive.
    - Le second cas commence avec une somme négative.
    Affiche le minimum de modifications entre les deux cas.
    """
    n = int(input())  # Lecture du nombre d'éléments dans la séquence
    a = [int(i) for i in input().split()]  # Lecture de la séquence d'entiers

    # Cas 1 : On commence avec une somme préfixe positive
    # On choisit v comme le premier terme > 0 ou sinon 1 pour garantir un début positif
    v = a[0] if a[0] > 0 else 1
    ans1 = abs(a[0] - v)  # Nombre de modifications initiales pour obtenir v à la position 0

    # Pour chaque élément suivant, on s'assure que la somme préfixe alternée change de signe
    for i in range(1, n):
        # Si la nouvelle somme partielle (v + a[i]) change de signe par rapport au précédent, c'est bon
        if v * (v + a[i]) < 0:
            v += a[i]  # On peut accumuler sans modification
            continue
        else:
            if v < 0:
                # Si la somme courante était négative, on ajuste pour obtenir +1 (le prochain préfixe > 0)
                ans1 += abs(v + a[i] - 1)
                v = 1  # On fixe la prochaine valeur préfixe à 1 (positif minimal)
            else:
                # Si la somme courante était positive, on ajuste pour obtenir -1 (le prochain préfixe < 0)
                ans1 += abs(v + a[i] + 1)
                v = -1  # On fixe la prochaine valeur préfixe à -1 (négatif minimal)

    # Cas 2 : On commence avec une somme préfixe négative
    # On choisit v comme le premier terme < 0 ou sinon -1 pour garantir un début négatif
    v = a[0] if a[0] < 0 else -1
    ans2 = abs(a[0] - v)  # Nombre de modifications initiales pour obtenir v à la position 0

    # Même logique que ci-dessus, mais l'alternance commence négatif
    for i in range(1, n):
        if v * (v + a[i]) < 0:
            v += a[i]
            continue
        else:
            if v < 0:
                ans2 += abs(v + a[i] - 1)
                v = 1
            else:
                ans2 += abs(v + a[i] + 1)
                v = -1

    # On choisit le minimum entre les deux cas (début positif ou négatif)
    ans = min(ans1, ans2)

    print(ans)

if __name__ == '__main__':
    solve()