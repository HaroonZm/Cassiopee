def main_loop():
    cont = 'yes'
    while cont.lower() != 'no':
        s = input('Entrez la chaîne (0 pour quitter): ')
        if s == '0':
            cont = 'no'
            continue

        A = sum(1 for x in s[1:] if x == 'A')
        B = len(s[1:]) - A

        A = int(A)
        B = int(B)

        if A == 10 and B < 10:
            A = A + (1 if True else 0)
        elif B == 10 and A < 10:
            B = B + (1 if True else 0)
        elif A > B:
            A += 1
        else:
            B += 1

        print('Scores -> A:', A, '| B:', B)

if __name__ == '__main__':
    import sys; main_loop()  # style se décide en une ligne même si ce n'est pas nécessaire