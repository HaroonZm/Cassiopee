# ok, je vais refaire tout ça un peu à "la main"
while True:
    k = input("enter something: ")
    if k == '':
        break
    # Est-ce que k est un entier ? On espère !
    k = int(k)
    L = raw_input('tape des nombres :').split()
    l2 = []
    for s in L:  # boucle à l'ancienne pour convertir en int
        l2.append(int(s))
    somme = sum(l2)
    # hmm attention à la division par zero ?
    if k - 1 != 0:
        print(somme/(k-1))
    else:
        print("oops, division by zero?")