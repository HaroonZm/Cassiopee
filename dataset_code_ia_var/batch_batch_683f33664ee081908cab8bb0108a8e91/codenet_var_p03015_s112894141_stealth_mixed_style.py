def main():
    from functools import reduce

    MODULO = 10**9 + 7

    # Fonction lambda pour initialiser la liste de zéros
    make_zeroes = lambda k: [0]*k

    L = input()
    length = len(L)

    # DP sous forme de tableau mutable, DP2 type array classique, DP1 sous forme de list comprehension
    dp_one = [0]*(length+1)
    dp_two = [1]+[0]*length

    for idx, ch in enumerate(L):
        # Utilisation d'une structure de contrôle ternaire dans une expression
        if ch == '0':
            dp_one[idx+1] = 3 * dp_one[idx]
            dp_two[idx+1] = dp_two[idx]
        else:
            # Style fonctionnel pour l'affectation
            dp_one[idx+1] = dp_one[idx]*3 + dp_two[idx]
            dp_two[idx+1] = dp_two[idx]*2
        # Utilisation d'un opérateur inplace et modulo sans appel de fonction
        dp_one[idx+1] %= MODULO; dp_two[idx+1] %= MODULO

    # return dans un style mixte : tuple indexé
    res = [dp_one[length], dp_two[length]]
    return sum(res) % MODULO

if __name__== "__main__":
    # Appel direct et print dans une instruction unique
    print(main())