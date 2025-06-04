n = int(input())

AB = []
for i in range(n):
    a, b = map(int, input().split())
    AB.append((a, b))

# On trie deux listes différentes : par le premier et par le deuxième élément
AB_A = sorted(AB, key=lambda t: t[0])
AB_B = sorted(AB, key=lambda t: t[1])

if n % 2 == 1:
    # Si n est impair, on prend l'élément du milieu
    milieu = n // 2
    a_milieu = AB_A[milieu][0]
    b_milieu = AB_B[milieu][1]
    print(b_milieu - a_milieu + 1)
else:
    # Si n est pair, on prend les deux éléments du milieu et on fait la différence
    gauche = n // 2 - 1
    droite = n // 2
    a_gauche = AB_A[gauche][0]
    a_droite = AB_A[droite][0]
    b_gauche = AB_B[gauche][1]
    b_droite = AB_B[droite][1]
    print((b_gauche + b_droite) - (a_gauche + a_droite) + 1)